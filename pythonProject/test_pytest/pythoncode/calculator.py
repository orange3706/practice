# -*- coding:utf-8 -*-
# @Author:chengzi
# @File:calculator.py
"""
计算器 加、减、乘、除
"""


class Calculator:

    def add(self, a, b):
        try:
            return a + b
        except ValueError:
            print("输入非数字的内容无法计算")

    def sub(self, a, b):
        try:
            return a - b
        except ValueError:
            return print(ValueError)

    def mul(self, a, b):
        try:
            return a * b
        except ValueError:
            print("输入非数字的内容无法计算")

    def div(self, a, b):
        try:
            if b == 0:
                print("除数不能为0")
            else:
                return a / b
        except ValueError:
            return 0
