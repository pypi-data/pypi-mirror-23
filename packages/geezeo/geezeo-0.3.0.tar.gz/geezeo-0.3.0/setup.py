#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools.command.test import test as TestCommand
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


class Tox(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'requests==2.17.3',
    'cryptography==1.9',
    'six==1.10.0',
    'PyJWT==1.5.2',
    'setuptools==36.0.1',
    'PyYAML==3.12'
]

test_requirements = [
    'tox>=2.1.1',
    'pytest==3.1.2'
]

setup(
    name='geezeo',
    version='0.3.0',
    description="Connect to the Geezeo API.",
    long_description=readme + '\n\n' + history,
    author="Geezeo",
    author_email='ddonna@amstonstudio.com',
    url='https://github.com/Geezeo/sdk-python',
    packages=[
        'geezeo',
    ],
    package_dir={'geezeo':
                 'geezeo'},
    include_package_data=True,
    install_requires=requirements,
    license="",
    zip_safe=False,
    keywords='geezeo',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    cmdclass={'test': Tox},
)
