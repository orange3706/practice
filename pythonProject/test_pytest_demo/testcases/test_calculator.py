# -*-coding:utf-8-*- 
# @Author:chengzi
# @File:test_calculator.py
"""
pytest --alluredir=../results
allure generate ../results -o ./report/ --clean
"""
import pytest
import allure
import yaml


def get_data():
    """
     获取数据return:data
    """
    with open('../data/calc_data.yml') as f:
        data = yaml.safe_load(f)
        return data

@allure.feature("测试计算器功能")
class TestCalculator:

    @allure.story("整数相加")
    @pytest.mark.parametrize('a, b, expect', get_data()['add_int'], ids=get_data()['add_int_ids'])
    def test_add_int(self, a, b, expect,get_calc):
        assert expect == get_calc.add(a, b)

    @allure.story("浮点数相加")
    @pytest.mark.parametrize('a, b, expect', get_data()['add_float'], ids=get_data()['add_float_ids'])
    def test_add_float(self, a, b, expect,get_calc):
        assert expect == round(get_calc.add(a, b), 6)

    @allure.story("包含字符串相加")
    @pytest.mark.parametrize('a, b, expect', get_data()["add_error"], ids=get_data()["add_error_ids"])
    def test_add_error(self, a, b, expect, get_calc):
        with pytest.raises(TypeError):
            expect == get_calc.add(a, b)

    @allure.story("整数相减")
    @pytest.mark.parametrize('a, b, expect', get_data()['sub_int'], ids=get_data()['sub_int_ids'])
    def test_sub_int(self, a, b, expect, get_calc):
        assert expect == get_calc.sub(a, b)

    @allure.story("浮点数相减")
    @pytest.mark.parametrize('a, b, expect', get_data()['sub_float'], ids=get_data()['sub_float_ids'])
    def test_sub_float(self, a, b, expect, get_calc):
        assert expect == round(get_calc.sub(a, b), 6)

    @allure.story("包含字符串相减")
    @pytest.mark.parametrize('a, b, expect', get_data()["sub_error"], ids=get_data()["sub_error_ids"])
    def test_sub_error(self, a, b, expect, get_calc):
        with pytest.raises(TypeError):
            expect == get_calc.sub(a, b)

    @allure.story("整数相乘")
    @pytest.mark.parametrize('a, b, expect', get_data()['mul_int'], ids=get_data()['mul_int_ids'])
    def test_mub_int(self, a, b, expect, get_calc):
        assert expect == get_calc.mul(a, b)

    @allure.story("浮点数相乘")
    @pytest.mark.parametrize('a, b, expect', get_data()['mul_float'], ids=get_data()['mul_float_ids'])
    def test_mub_float(self, a, b, expect, get_calc):
        assert expect == round(get_calc.mul(a, b), 6)

    @allure.story("包含字符串相乘")
    @pytest.mark.parametrize('a, b, expect', get_data()["mul_error"], ids=get_data()["mul_error_ids"])
    def test_mub_error(self, a, b, expect, get_calc):
        with pytest.raises(TypeError):
            expect == get_calc.mul(a, b)

    @allure.story("整数相除")
    @pytest.mark.parametrize('a, b, expect', get_data()['div_int'], ids=get_data()['div_int_ids'])
    def test_div_int(self, a, b, expect, get_calc):
        assert expect == get_calc.div(a, b)

    @allure.story("浮点数相除")
    @pytest.mark.parametrize('a, b, expect', get_data()['div_float'], ids=get_data()['div_float_ids'])
    def test_div_float(self, a, b, expect, get_calc):
        assert expect == round(get_calc.div(a, b), 6)

    @allure.story("包含字符串相除")
    @pytest.mark.parametrize('a, b, expect', get_data()["div_error"], ids=get_data()["div_error_ids"])
    def test_div_error(self, a, b, expect, get_calc):
        with pytest.raises(TypeError):
            expect == get_calc.div(a, b)

    @pytest.mark.parametrize('a, b, expect',
                             get_data()['div_denominator_zero'],
                             ids=get_data()['div_denominator_zero_ids'])
    def test_div_error(self, a, b, expect, get_calc):
        try:
            expect == get_calc.div(a, b)
        except ZeroDivisionError:
            print("除数不能为0")