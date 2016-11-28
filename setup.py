
#!/usr/bin/python

import ast
from distutils.core import setup
from setuptools import setup, find_packages

def get_version(fname):
    with open(fname) as f:
        source = f.read()
    module = ast.parse(source)
    for e in module.body:
        if isinstance(e, ast.Assign) and \
                len(e.targets) == 1 and \
                e.targets[0].id == '_version_' and \
                isinstance(e.value, ast.Str):
            return e.value.s
    raise RuntimeError('_version_ not found')

setup(name = 'THSet',  
      version = get_version('THset/THSet'),
      keywords = 'Create Track Hub',
      description = 'Create Track Hub', 
      long_description = 'Create Track Hub',
      license = 'GPLv3',
      classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Programming Language :: Python :: 2.7',
      ],

      packages = ['THSet'],
      package_dir = {'THSet': 'THSet'},
      scripts = ['THSet/THSet'],
      package_data = {'THSet': ['configure.txt']}
) 
