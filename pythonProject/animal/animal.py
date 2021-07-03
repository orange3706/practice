# -*- coding:utf-8 -*-
# @Author:chengzi
# @File:animal.py

"""
创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
"""

class Animal:

    # 构造函数，在类实例化的时候先执行
    def __init__(self, name, colour,age,gender):
        self.name = name
        self.colour = colour
        self.age = age
        self.gender =gender

    #类方法：会跑
    def run(self):
        print(f"{self.name}会跑")

    # 类方法：会叫
    def call(self):
        print(f"{self.name}会叫")