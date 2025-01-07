#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# author： NearlyHeadlessJack
# email: wang@rjack.cn
# datetime： 2025/1/6 21:04 
# ide： PyCharm
# file: add_op.py
import yaml
import sys
import re

def add_op(op_id:str):
    op_list:list
    if check_op_id_input(op_id):
        print('-输入ID不合法!')
        sys.exit(0)

    try:
        with open('ops.yaml','r') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
            op_list = result['ops']
            op_list.append(op_id)
        with open('ops.yaml','w') as f:
            context = {
                'ops':op_list
            }
            yaml.dump(data=context, stream=f, allow_unicode=True)
    except FileNotFoundError:
        with open('ops.yaml','w') as f:
            with open('ops.yaml', 'w') as f:
                context = {
                    'ops': [op_id]
                }
                yaml.dump(data=context, stream=f, allow_unicode=True)
def check_op_id_input(op_id:str)->bool:
    pattern = re.compile(r'\W')
    if re.match(pattern, op_id) is None:
        return False
    else:
        return True
