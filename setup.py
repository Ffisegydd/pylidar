import re
import os

from setuptools import setup, find_packages

package_name = 'pylidar'

try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    requirements = []

try:
    with open(os.path.join(os.path.dirname(__file__), package_name, '__init__.py')) as f:
        version = re.search(r"__version__ = '(.*)'", f.read()).group(1)
except FileNotFoundError:
    version = 'test'

classifiers = ['Development Status :: 3 - Alpha',

               'Operating System :: OS Independent',
               'Intended Audience :: Developers',
               'Intended Audience :: Education',
               'Intended Audience :: Science/Research',

               'License :: OSI Approved :: MIT License',

               'Natural Language :: English',

               'Programming Language :: Python',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: Implementation :: CPython',

               'Topic :: Scientific/Engineering',
               ]

setup(
      name=package_name,
      packages=find_packages(),
      url='https://github.com/Ffisegydd/pylidar',
      license='MIT',
      author='Keiron J. Pizzey',
      author_email='kjpizzey@gmail.com',
      description='Python package for loading LIDAR geospatial Digital Surface Models (DSM). Started as a project at the Bath:Hacked "Summers of Data" hack day.',
      install_requirements=requirements,
      classifiers=classifiers,
      version=version
)
