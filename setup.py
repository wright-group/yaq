#! /usr/bin/env python


# --- import -------------------------------------------------------------------------------------


import os
import sys

from setuptools import setup, find_packages


# --- define -------------------------------------------------------------------------------------


here = os.path.abspath(os.path.dirname(__file__))


# --- setup --------------------------------------------------------------------------------------


data_files = []
if sys.platform.startswith('linux'):
    data_files.append(('/usr/share/applications', ['scripts/yaq.desktop']))


extra_files = []
extra_files.append(os.path.join(here, 'CONTRIBUTORS'))
extra_files.append(os.path.join(here, 'LICENSE'))
extra_files.append(os.path.join(here, 'README.rst'))
extra_files.append(os.path.join(here, 'requirements.txt'))
extra_files.append(os.path.join(here, 'VERSION'))


with open(os.path.join(here, 'requirements.txt')) as f:
    required = f.read().splitlines()


with open(os.path.join(here, 'VERSION')) as version_file:
    version = version_file.read().strip()


setup(
    name='yaq',
    packages=find_packages(),
    package_data={'': extra_files},
    data_files=data_files,
    install_requires=required,
    version=version,
    description='Yet another acquisition.',
    author='Blaise Thompson',
    author_email='blaise@untzag.com',
    license='MIT',
    url='https://github.com/wright-group/yaq',
    keywords='spectroscopy science multidimensional',
    classifiers=['Development Status :: 1 - Planning',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Topic :: Scientific/Engineering'],
    entry_points={'gui_scripts': ['yaq=yaq.widgets.start:main']}
)
