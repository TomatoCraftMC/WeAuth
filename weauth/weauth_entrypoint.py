#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/5 20:28 
# ide： PyCharm
# file: weauth_entrypoint.py
import platform
import sys

__all__ = ['entrypoint']


def __environment_check():
	"""
	This should even work in python 2.7+
	"""
	# only mcdreforged.constants is allowed to load before the boostrap() call
	from weauth.constants import core_constant

	if sys.version_info < (3, 8):
		print('Python 3.8+ is needed to run {}'.format(core_constant.NAME))
		print('Current Python version {} is too old'.format(platform.python_version()))
		sys.exit(1)


def entrypoint():
	"""
	The one and only entrypoint for WeAuth

	All WeAuth launches start from here
	"""
	__environment_check()

	from weauth.weauth import main

	main()

