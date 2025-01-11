#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/11 08:35 
# ide： PyCharm
# file: admin_cli.py
from weauth.constants.core_constant import VERSION, GITHUB_URL
from weauth.utils.add_op import add_op, add_super_op

class AdminCLI:
    def __init__(self):
        pass

    @staticmethod
    def admin_cli_entry(command: str, player_id: str) -> (int, str):

        pass

    @staticmethod
    def admin_cli(command: str) -> (int, str):
        command_list = command.split()
        if command_list[0] == 'op':
            op_id = command_list[1]
            if add_op(op_id=op_id) == 0:
                return 0, f'已成功添加 {op_id} 为WeAuth管理员'
            else:
                return 0, '添加失败'
        elif command_list[0] == 'sop':
                op_id = command_list[1]
                if add_super_op(op_id=op_id) == 0:
                    return 0, f'已成功添加 {op_id} 为WeAuth超级管理员'
                else:
                    return 0, '添加失败'

        elif command_list[0] == 'v':
            msg = f'WeAuth version {VERSION}\nLICENSE: GPLv3\nProject Homepage: {GITHUB_URL}'
            return 0, msg
        elif command_list[0] == 'g':
            pass
        else:
            return -1, None


if __name__ == '__main__':
    AdminCLI.admin_cli('-op   d')
