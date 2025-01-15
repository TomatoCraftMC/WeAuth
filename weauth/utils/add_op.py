#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# WeAuth is released under the GNU GENERAL PUBLIC LICENSE v3 (GPLv3.0) license.
# datetime： 2025/1/6 21:04 
# ide： PyCharm
# file: add_op.py
import yaml
import sys
import re


def add_op(op_id: str) -> int:
    op_list:list
    if check_op_id_input(op_id):
        print('-输入ID不合法!')
        return -1
    try:
        with open('ops.yaml', 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
        result['ops'].append(op_id)
        with open('ops.yaml','w') as f:
            context = result
            yaml.dump(data=context, stream=f, allow_unicode=True)
        return 0
    except FileNotFoundError:
        with open('ops.yaml', 'w+') as f:
            context = {'ops': [op_id]}
            yaml.dump(data=context, stream=f, allow_unicode=True)
        return 0



def check_op_id_input(op_id:str)->bool:
    pattern = re.compile(r'\W')
    if re.search(pattern, op_id) is None:
        return False
    else:
        return True


def add_super_op(op_id: str) -> int:
    op_list = [str]
    if check_op_id_input(op_id):
        print('-输入ID不合法!')
        return -1
    try:
        with open('ops.yaml', 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
        super_op_list = [str]
        try:
            op_list = result['ops']
            super_op_list = result['super_ops']
        except KeyError:
            with open('ops.yaml', 'w') as f:
                op_list.append(op_id)
                super_op_list = [op_id]
                context = {
                    'ops': op_list,
                    'super_ops': super_op_list}
                yaml.dump(data=context, stream=f, allow_unicode=True)
            return 0
        with open('ops.yaml', 'w') as f:
            op_list.append(op_id)
            super_op_list.append(op_id)
            context = {
                'ops': op_list,
                'super_ops': super_op_list
            }
            yaml.dump(data=context, stream=f, allow_unicode=True)
        return 0
    except FileNotFoundError:
        with open('ops.yaml', 'w+') as f:
            context = {'ops': [op_id], 'super_ops': [op_id]}
            yaml.dump(data=context, stream=f, allow_unicode=True)
        return 0

# if __name__ == '__main__':
#     # add_op('1212d')
#     # add_op('12222212d')
#     # add_super_op('9902')
#     # add_op('12222212dfnfn')
