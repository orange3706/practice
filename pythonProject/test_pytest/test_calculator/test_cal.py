# -*- coding:utf-8 -*-
# @Author:chengzi
# @File:test_cal.py
import logging
import pytest
from test_pytest.pythoncode.calculator import Calculator
import yaml


class TestCalc:
    def setup_class(self):
        logging.info("开始测试:"+'\n')

    def teardown_class(self):
        print('\n')
        logging.info("结束测试")

    def setup(self):
        logging.info("开始计算")
        self.calc = Calculator()

    def teardown(self):
        logging.info("结束计算")

    #加法测试验证
    @pytest.mark.parametrize('a,b,expect',[[1,1,2], [0.1,0.1,0.2], [-11,-2,-13], [10000000, 9999999, 19999999], [0, 0, 0]
                             ], ids=['int', 'float', 'minus','bignum', 'zero'])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    #减法测试验证
    @pytest.mark.parametrize(["a","b","expect"], yaml.safe_load(open("sub_data.yaml"))
                             , ids=['int', 'float', 'minus', 'bignum', 'zero'])
    def test_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)

    #乘法测试验证
    @pytest.mark.parametrize('a,b,expect',
                             [[1, 1, 1], [0.2, 0.2, 0.04], [-11, 2, -22],  [0, 2, 0]
                              ], ids=['int', 'float', 'minus',  'zero'])
    def test_mul(self, a, b, expect):
        assert expect == self.calc.mul(a, b)

    #除法校验
    @pytest.mark.parametrize('a,b,expect',
                             [[1, 1, 1], [0.1, 0.1, 1], [-11, -2, 5.5], [10, 0, None]
                                 , ['汉子', 3, 0]
                              ], ids=['int', 'float', 'minus',  'zero', 'error'])
    def test_div(self, a, b, expect):
        assert expect == self.calc.div(a, b)