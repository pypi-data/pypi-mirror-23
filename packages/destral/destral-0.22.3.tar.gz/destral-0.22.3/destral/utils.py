from ast import literal_eval
import imp
import logging
import os
import re
import sys
import subprocess
import tempfile
import shutil

__all__ = [
    'update_config',
    'detect_module',
    'module_exists',
    'get_dependencies',
    'find_files',
    'install_requirements',
    'coverage_modules_path'
]


def update_config(config, **kwargs):
    """Updates config dictionary from keyword arguments.
    """
    for key, value in kwargs.iteritems():
        config[key] = value
    return config


def detect_module(path):
    """Detect if a path is part of a openerp module or not

    :param path: to examine
    :return: None if is not a module or the module name
    """
    stack = path.split(os.path.sep)
    if not stack[0]:
        stack[0] = os.path.sep
    stack = [x for x in stack if x]
    while stack:
        path = os.path.join(*stack)
        module = stack.pop()
        if not os.path.isdir(path):
            continue
        files = os.listdir(path)
        if '__terp__.py' in files:
            return module
    return None


def module_exists(module):
    """Check if a python module exists.

    This is used to check if a module have its own tests defined, Eg:
    `addons.module_name.tests`
    
    :param module: Module name to check
    :return: True if exists or False if not
    """
    modlist = module.split('.')
    pathlist = None
    for mod in modlist:
        try:
            openfile, pathname, desc = imp.find_module(mod, pathlist)
            pathlist = [pathname]
            # Clean netsvc Services
            import netsvc
            netsvc.SERVICES.clear()
        except ImportError:
            return False
        else:
            if openfile:
                openfile.close()
                return True


def get_dependencies(module, addons_path=None, deps=None):
    """Get all the dependencies of a module without database

    Using `__terp__.py` files and is used to check requirements.txt in the
    dependencies.

    :param module: Module to find the dependencies
    :param addons_path: Path to find the modules
    :return: a listt of dependencies.
    """
    if deps is None:
        deps = []
    if addons_path is None:
        from destral.openerp import OpenERPService
        service = OpenERPService()
        addons_path = service.config['addons_path']
    pj = os.path.join
    module_path = pj(addons_path, module)
    if not os.path.exists(module_path):
        raise Exception('Module {} not found in {}'.format(
            module, addons_path
        ))
    terp_path = pj(module_path, '__terp__.py')
    if not os.path.exists(terp_path):
        raise Exception(
            'Module {} is not a valid module. Missing __terp__.py file'.format(
                module
            )
        )
    with open(terp_path, 'r') as terp_file:
        terp = literal_eval(terp_file.read())

    for dep in terp['depends']:
        deps.append(dep)
        deps += get_dependencies(dep, addons_path, deps)

    return list(set(deps))


def find_files(diff):
    """Return all the files implicated in a diff
    """
    paths = []
    for line in re.findall("--- a/.*|\+\+\+ b/.*", diff):
        line = '/'.join(line.split('/')[1:])
        paths.append(line)
    return list(set(paths))


def install_requirements(module, addons_path):
    """Install module requirements and its dependecies
    """
    logger = logging.getLogger('destral.utils')
    modules_requirements = get_dependencies(module, addons_path)
    modules_requirements.append(module)
    for module_requirements in modules_requirements:
        req = os.path.join(
            addons_path,
            module_requirements,
            'requirements.txt'
        )
        pip = os.path.join(sys.prefix, 'bin', 'pip')
        if os.path.exists(req) and os.path.exists(pip):
            logger.info('Requirements file %s found. Installing...', req)
            subprocess.check_call([pip, "install", "-r", req])


def coverage_modules_path(modules_to_test, addons_path):
    return [
        os.path.relpath(os.path.realpath(os.path.join(addons_path, m))) for m in
        modules_to_test
    ]


def compare_pofiles(pathA, pathB):
    """
    :param pathA: path to pot/po file
    :param pathB: path to pot/po file
    :param translate: whether translation should be checked or not
    :return: True if all strings in pathA are in pathB
    """
    from babel.messages import pofile
    from os.path import isfile
    import logging
    logger = logging.getLogger('destral.utils.compare_pofiles')
    if not isfile(pathA):
        logger.info('Could not get po/pot file: {}'.format(pathA))
        return None, None
    elif not isfile(pathB):
        logger.info('Could not get po/pot file: {}'.format(pathB))
        return None, None
    try:
        with open(pathA, 'r') as potA:
            fileA = pofile.read_po(potA)
    except ValueError:
        # If bad formatted data, replace it
        with open(pathA, 'r') as potA:
            data = potA.read()
        from re import sub
        data = sub(r"(POT-Creation-Date: )(.*):..\+(.*)\\", r"\1\2\\", data)
        data = sub(r"(PO-Revision-Date: )(.*):..\+(.*)\\", r"\1\2\\", data)
        with open(pathA, 'w') as potA:
            potA.write(data)
        with open(pathA, 'r') as potA:
            fileA = pofile.read_po(potA)
        logger.warning(
            'Data of POfile {} has bad formatted '
            'creation or revision dates'.format(pathA)
        )
    try:
        with open(pathB, 'r') as potB:
            fileB = pofile.read_po(potB)
    except ValueError:
        # If bad formatted data, replace it
        with open(pathB, 'r') as potB:
            data = potB.read()
        from re import sub
        data = sub(r"(POT-Creation-Date: )(.*):..\+(.*)\\", r"\1\2\\", data)
        data = sub(r"(PO-Revision-Date: )(.*):..\+(.*)\\", r"\1\2\\", data)
        with open(pathB, 'w') as potB:
            potB.write(data)
        with open(pathB, 'r') as potB:
            fileB = pofile.read_po(potB)
        logger.warning(
            'Data of POfile {} has bad formatted '
            'creation or revision dates'.format(pathB)
        )
    not_found = []
    not_translated = []
    for msgA in fileA:
        if msgA.id == '':
            continue
        msgB = fileB.get(msgA.id)
        if not msgB:
            not_found.append(msgA.id)
            continue
        if not msgB.string:
            not_translated.append(msgA.id)
    return not_found, not_translated


class TempDir(object):
    def __init__(self):
        self.dir = tempfile.mkdtemp()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        shutil.rmtree(self.dir)
