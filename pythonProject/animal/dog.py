# -*- coding:utf-8 -*-
# @Author:chengzi
# @File:dog.py

"""
创建子类【狗】，继承【动物类】
复写父类的__init__方法，继承父类的属性
添加一个新的属性，毛发=长毛
添加一个新的方法， 会看家
复写父类的【会叫】的方法，改成【汪汪叫】
"""

import animal


class Dog(animal.Animal):
    hair = "长毛"

    def __init__(self, name, colour, age, gender, hair):
        super().__init__(name, colour, age, gender)
        self.hair = hair

    def look_house(self):
        # 打印【狗狗的姓名，颜色，年龄，性别，毛发】
        print(f"{self.name},{self.colour},{self.age},{self.gender},{self.hair}")

    def call(self):
        print(f"{self.name}汪汪叫")
