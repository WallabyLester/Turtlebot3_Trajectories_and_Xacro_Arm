from setuptools import setup
from catkin_pkg.python_setup import generate_distutils_setup
'''
setup(name='homework2',
version='0.1',
description='package for computing trajectories and giving inputs',
url='#',
author='andru',
author_email='andruliu2022@u.northwestern.edu',
license='',
packages=['homework2'],
zip_safe=False)
'''

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['homework2'],
    package_dir={'': 'src'})

setup(**setup_args)