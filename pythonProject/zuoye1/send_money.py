# -*- coding:utf-8 -*-
# @Author:chengzi
# @File:send_money.py

import money

#发工资
def send_money(wages):
    if wages>0:
        print(f"本次发工资:{wages}")
        money.saved_money =money.saved_money+wages
        print(f"工资已到账，余额: {money.saved_money}")
    else:
        print(f"发放工资失败，发放金额异常{wages}")

