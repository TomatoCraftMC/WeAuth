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
from weauth.constants import exit_code
from weauth.cdkey import CDKey

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
						action='store_true',default=False)
	parser.add_argument('-test', '--test_mode', help='Running in test_mode',
						action='store_true',default=False)
	parser.add_argument('-w', '--wechat_confirm', help='微信验证开发者服务器相应程序',
						action='store_true',default=False)
	parser.add_argument('-t','--token',help='验证用token',default='-1',type=str)
	parser.add_argument('-op', '--op', help='新增op', default='-1', type=str)
	parser.add_argument('-r', '--url', help='路由地址', default='/wx', type=str)
	parser.add_argument('-g', '--gift', help='生成CDKey',
						action='store_true', default=False)
	parser.add_argument('-sop', '--sop', help='新增超级管理员', default='-1', type=str)
	args = parser.parse_args()
	if args.url[0]!='/':
		print("路由地址不合法,请检查后重新输入")
		sys.exit(0)

	if args.version:
		print('WeAuth version {}\nBuild time: {}\nLICENSE: GPLv3\nProject Homepage: {}'
			  .format(core_constant.VERSION, core_constant.BUILD_TIME, core_constant.GITHUB_URL))
		sys.exit(0)

	if args.wechat_confirm:
		if args.token == '-1':
			print('请输入token参数才能运行微信服务器验证\n'
				  '如weauth -t token1234 -w')
			sys.exit(0)
		from weauth.wechat_confirm import confirm
		confirm(args.token,url=args.url)
		sys.exit(0)

	if args.op !='-1':
		from weauth.utils.add_op import add_op
		print('-正在添加玩家{}为WeAuth管理员'.format(args.op))
		add_op(op_id=args.op)
		sys.exit(0)

	if args.sop != '-1':
		from weauth.utils.add_op import add_super_op
		print('-正在添加玩家{}为WeAuth超级管理员'.format(args.sop))
		add_super_op(op_id=args.sop)
		sys.exit(0)

	if args.gift:
		CDKey.create_gift_entrypoint()
		sys.exit(0)


	main(args)

