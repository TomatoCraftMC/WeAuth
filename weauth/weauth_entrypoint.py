#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# WeAuth is released under the GNU GENERAL PUBLIC LICENSE v3 (GPLv3.0) license.
# email: wang@rjack.cn
# datetime： 2025/1/5 20:28
# ide： PyCharm
# file: weauth_entrypoint.py
import argparse
import platform
import sys
from weauth.constants import core_constant
from weauth.constants import exit_code
from weauth.cdkey import CDKey
from weauth.command_line import AdminCLI
from weauth.database import DB

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
	parser.add_argument('-v', '--version', help='Print {} version and exit'.format(core_constant.NAME),
						action='store_true',default=False)
	parser.add_argument('-test', '--test_mode', help='Running in test_mode',
						action='store_true',default=False)
	parser.add_argument('-w', '--wechat_confirm', help='微信验证开发者服务器相应程序',
						action='store_true',default=False)
	parser.add_argument('-t','--token',help='验证用token',default='-1',type=str)
	parser.add_argument('-cp', '--pub_path', help='ssl_证书路径', default='-1', type=str)
	parser.add_argument('-kp', '--key_path', help='ssl_私钥路径', default='-1', type=str)
	parser.add_argument('-op', '--op', help='新增op', default='-1', type=str)
	parser.add_argument('-r', '--url', help='路由地址', default='/wx', type=str)
	parser.add_argument('-g', '--gift', help='生成CDKey',
						action='store_true', default=False)
	parser.add_argument('-sop', '--sop', help='新增超级管理员', default='-1', type=str)
	parser.add_argument('-del', '--delete', help='通过player_id从数据库删除玩家信息',
						action='store_true', default=False)
	parser.add_argument('-list', '--list', help='打印数据库里面的所有Player_id',
						action='store_true', default=False)
	parser.add_argument('-search', '--search', help='数据库中搜索Player_id', type=str, default='-1')
	parser.add_argument('-update', '--update', help='更新数据库中一条,传入玩家ID', type=str, default='-1')
	parser.add_argument('-b', '--b', help='ban', default=False, action='store_true')
	parser.add_argument('-ban', '--ban', help='ban [player_id]', default='-1', type=str)
	parser.add_argument('-s', '--s', help='切换注册状态',
						default=False, action='store_true')
	parser.add_argument('-unban', '--unban', help='unban [player_id]', default='-1', type=str)


	args = parser.parse_args()

	if args.delete:
		AdminCLI.remove_by_player_id()
		sys.exit(0)

	if args.list:
		print(AdminCLI.list_all_player_id())
		sys.exit(0)

	if args.search != '-1':
		AdminCLI.search_db(player_id=args.search)
		sys.exit(0)

	if args.update != '-1':
		update_item(args)
		sys.exit(0)

	if args.update == '-1' and args.ban != '-1':
		AdminCLI.ban_db(player_id=args.ban)
		sys.exit(0)

	if args.update == '-1' and args.unban != '-1':
		AdminCLI.unban_db(player_id=args.unban)
		sys.exit(0)


	if args.url[0] != '/':
		print("路由地址不合法,请检查后重新输入")
		sys.exit(0)

	if args.version:
		print('WeAuth version {}\nBuild time: {}z\nLICENSE: GPLv3\nProject Homepage: {}'
			  .format(core_constant.VERSION, core_constant.BUILD_TIME, core_constant.GITHUB_URL))
		sys.exit(0)

	if args.wechat_confirm:
		if args.token == '-1':
			print('请输入token参数才能运行微信服务器验证\n'
				  '如weauth -t token1234 -w')
			sys.exit(0)
		from weauth.wechat_confirm import confirm
		if args.pub_path == '-1' or args.key_path == '-1':
			confirm(args.token, url=args.url)
			sys.exit(0)
		else:
			confirm(args.token, url=args.url, cer_path=args.pub_path, key_path=args.key_path)
			sys.exit(0)

	if args.op != '-1':
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


def update_item(args: argparse.Namespace) -> None:
	player_item = DB.get_item(player_id=args.update)
	if player_item is None:
		print("-未找到该玩家ID")
		sys.exit(0)
	ban_ = player_item[2]
	sub_ = player_item[3]
	if ban_ == 0:
		ban_stat = '否'
	else:
		ban_stat = '是'
	if sub_ == 0:
		sub_stat = '否'
	else:
		sub_stat = '是'
	print(f'玩家ID: {player_item[0]}, 是否封禁: {ban_stat}, 是否正在订阅: {sub_stat}')
	ans1 = []
	ans2 = []
	_ban = args.b
	_sub = args.s

	if _ban and bool(ban_):
		ans1.append(input(f'-您确认将玩家 {player_item[0]}的封禁状态更改为【否】？ (输入yes/no确认)\n>'))
		ans1.append('0')

	elif _ban or bool(ban_):
		ans1.append(input(f'-您确认将玩家 {player_item[0]}的封禁状态更改为【是】？ (输入yes/no确认)\n>'))
		ans1.append('1')
	else:
		ans1 = ['yes', str(player_item[2])]

	if not (ans1[0] == 'yes' or ans1[0] == 'y'):
		sys.exit(0)

	if _sub and bool(sub_):
		ans2.append(input(f'-您确认将玩家 {player_item[0]}的注册状态更改为【否】？ (输入yes/no确认)\n>'))
		ans2.append('0')

	elif _sub or bool(sub_):
		ans2.append(input(f'-您确认将玩家 {player_item[0]}的注册状态更改为【是】？ (输入yes/no确认)\n>'))
		ans2.append('1')
	else:
		ans2 = ['yes', str(player_item[3])]
	if not (ans2[0] == 'yes' or ans2[0] == 'y'):
		sys.exit(0)

	DB.update_item_by_player_id(player_id=player_item[0],
								ban=ans1[1],
								sub=ans2[1])
	print('-数据库成功更新')
	sys.exit(0)
