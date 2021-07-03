# -*- coding:utf-8 -*-
# @Author:chengzi
# @File:main.py

"""
在入口函数中创建类的实例
创建一个猫猫实例
调用捉老鼠的方法
打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】
创建一个狗狗实例
调用【会看家】的方法
打印【狗狗的姓名，颜色，年龄，性别，毛发】
"""

import cat
import dog


if __name__ == '__main__':
    # 创建一个猫猫实例
    cat = cat.Cat("花花", "黑色", 3, "母", "短毛")
    # 调用捉老鼠的方法
    cat.catching_mice()

    # 创建一个狗狗实例

    dog = dog.Dog("旺财", "白色", 2, "公", "长毛")
    # 调用【会看家】的方法
    dog.look_house()
