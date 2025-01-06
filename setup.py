#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/6 11:01 
# ide： PyCharm
# file: setup.py
from setuptools import find_packages, setup
from weauth.constants import core_constant
import os
NAME = core_constant.PACKAGE_NAME
VERSION = core_constant.VERSION_PYPI
DESCRIPTION = 'A python tool to managing your whitelist through WeChat.'
PROJECT_URLS = {
	'Homepage': core_constant.GITHUB_URL,
	'Documentation': core_constant.DOCUMENTATION_URL,
}
AUTHOR = 'NearlyHeadlessJack'
REQUIRES_PYTHON = '>=3.8'

CLASSIFIERS = [
	# https://pypi.org/classifiers/
	'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE v3 (GPLv3)',
	'Operating System :: OS Independent',
	'Programming Language :: Python',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.8',
	'Programming Language :: Python :: 3.9',
	'Programming Language :: Python :: 3.10',
	'Programming Language :: Python :: 3.11',
	'Programming Language :: Python :: 3.12',
	'Programming Language :: Python :: 3.13',
]

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'requirements.txt')) as f:
	REQUIRED = list(filter(None, map(str.strip, f)))
	print('REQUIRED = {}'.format(REQUIRED))

ENTRY_POINTS = {
	'console_scripts': [
		'{} = {}.weauth_entrypoint:entrypoint'.format(core_constant.CLI_COMMAND, core_constant.PACKAGE_NAME)
	]
}
print('ENTRY_POINTS = {}'.format(ENTRY_POINTS))

with open(os.path.join(here, '/docs/README.md'), encoding='utf8') as f:
	LONG_DESCRIPTION = f.read()



setup(
    name=NAME,
	version=VERSION,
	description=DESCRIPTION,
    author=AUTHOR,
	python_requires=REQUIRES_PYTHON,
	long_description=LONG_DESCRIPTION,
	long_description_content_type='text/markdown',
    project_urls=PROJECT_URLS,
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*', 'tests.*']),
    include_package_data=True,
    install_requires=REQUIRED,
    entry_points=ENTRY_POINTS,
	license="GPLv3",
)
