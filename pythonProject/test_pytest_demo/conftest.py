# -*-coding:utf-8-*- 
# @Author:chengzi
# @File:conftest.py

import logging
import pytest

from test_pytest.pythoncode.calculator import Calculator


@pytest.fixture(scope='class',autouse=True)
def stat_end():
    logging.info("开始测试:" )
    yield
    logging.info( "结束测试")


@pytest.fixture(autouse=True)
def get_calc():
    logging.info("开始计算")
    calc = Calculator()
    yield calc
    logging.info("结束计算")
