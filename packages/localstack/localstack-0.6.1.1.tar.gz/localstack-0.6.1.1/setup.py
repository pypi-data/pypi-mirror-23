#!/usr/bin/env python

from __future__ import print_function

import os
import sys
import re
import subprocess
import setuptools
from setuptools import find_packages, setup
from setuptools.command.install_lib import install_lib

# parameter variables
install_requires = []
dependency_links = []
package_data = {}


# determine version
with open('localstack/constants.py') as f:
    constants = f.read()
version = re.search(r'^\s*VERSION\s*=\s*[\'"](.+)[\'"]\s*$', constants, re.MULTILINE).group(1)


# determine requirements
with open('requirements.txt') as f:
    requirements = f.read()
for line in re.split('\n', requirements):
    if line and line[0] == '#' and '#egg=' in line:
        line = re.search(r'#\s*(.*)', line).group(1)
    if line and line[0] != '#':
        if '://' not in line:
            install_requires.append(line)


# def do_make_install(workdir=None):
#     if workdir:
#         prev_workdir = os.getcwd()
#         os.chdir(workdir)
#     try:
#         subprocess.check_output('make install', shell=True)
#     except subprocess.CalledProcessError as e:
#         print(e.output)
#         raise e
#     if workdir:
#         os.chdir(prev_workdir)


# class InstallLibCommand(install_lib):

#     def run(self):
#         install_lib.run(self)
#         # prepare filesystem
#         main_dir_name = 'localstack'
#         target_dir = '%s/%s' % (self.install_dir, main_dir_name)
#         infra_dir = '%s/infra' % (main_dir_name)
#         # delete existing directory
#         subprocess.check_output('rm -r %s' % (main_dir_name), shell=True)
#         # create symlink
#         subprocess.check_output('ln -s %s %s' % (target_dir, main_dir_name), shell=True)
#         # delete infra directory (if it exists) to force re-install
#         subprocess.check_output('rm -rf %s' % (infra_dir), shell=True)
#         # run 'make install'
#         do_make_install()


package_data = {
    '': ['Makefile', '*.md'],
    'localstack': [
        'package.json',
        'dashboard/web/*.*',
        'dashboard/web/css/*',
        'dashboard/web/img/*',
        'dashboard/web/js/*',
        'dashboard/web/views/*',
        'ext/java/*.*',
        'ext/java/src/main/java/com/atlassian/localstack/*.*',
        'utils/kinesis/java/com/atlassian/*.*'
    ]}


if __name__ == '__main__':

    setup(
        name='localstack',
        version=version,
        description='An easy-to-use test/mocking framework for developing Cloud applications',
        author='Waldemar Hummer (Atlassian)',
        author_email='waldemar.hummer@gmail.com',
        url='https://github.com/localstack/localstack',
        scripts=['bin/localstack'],
        packages=find_packages(exclude=('tests', 'tests.*')),
        package_data=package_data,
        install_requires=install_requires,
        dependency_links=dependency_links,
        test_suite='tests',
        license='Apache License 2.0',
        # cmdclass={
        #     'install_lib': InstallLibCommand
        # },
        zip_safe=False,
        classifiers=[
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.6',
            'License :: OSI Approved :: Apache Software License',
            'Topic :: Software Development :: Testing',
        ]
    )
