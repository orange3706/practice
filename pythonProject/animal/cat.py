# -*- coding:utf-8 -*-
# @Author:chengzi
# @File:cat.py

"""
创建子类【猫】，继承【动物类】
重写父类的__init__方法，继承父类的属性
添加一个新的属性，毛发=短毛
添加一个新的方法， 会捉老鼠，
重写父类的‘【会叫】的方法，改成【喵喵叫】
"""

import animal


class Cat(animal.Animal):
    hair = "短毛"

    def __init__(self, name, colour, age, gender, hair):
        super().__init__(name, colour, age, gender)
        self.hair = hair

    def catching_mice(self):
        # 印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】

        print(f"{self.name},{self.colour},{self.age}，{self.gender},{self.hair},捉到了老鼠")

    def call(self):
        print(f"{self.name}喵喵叫")
