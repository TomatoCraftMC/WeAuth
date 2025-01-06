#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/5 20:28 
# ide： PyCharm
# file: weauth_entrypoint.py
import platform
import sys
from weauth.constants import core_constant

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

	from weauth.weauth_boostrap import main
	import argparse
	parser = argparse.ArgumentParser(description='启动参数')
	parser.add_argument('-p','--port',help='监听端口',default='80',type=str)
	parser.add_argument('-v', '--version', help='Print {} version and exit'.format(core_constant.NAME),
						action='store_true',default='False')
	args = parser.parse_args()
	if args.version:
		print('WeAuth version {}\nLICENSE: GPLv3\nProject Homepage:{}'
			  .format(core_constant.VERSION,core_constant.GITHUB_URL))
		sys.exit(0)
	main(args)

