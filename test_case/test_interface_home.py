#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: test_interface_home.py
@time: 2020/04/21
"""
import unittest
from common.base_request import RequestInterface
from common.base_compare import CompareParm
from public import config
import json
import ddt
from data import interface_home
from public.test_case import TestCase
"""
常笑母婴-首页相关接口测试
"""


@ddt.ddt
class TestInterfaceHome(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.r = RequestInterface()
        cls.compare = CompareParm()
        cls.testcase = TestCase()

    @ddt.data(*interface_home.bodyChanges)
    def test_interface_home_bodyChanges(self, datalist):
        # url = config.base_url + datalist['url']
        # result = self.r.http_request(interface_url=url, headerdata=datalist['h'],
        #                              interface_param=datalist['d'], request_type=datalist['mode'])
        # compare_code = self.compare.compare_code(result_interface=result['data'], code=datalist['code'],
        #                                          expected_code=datalist['expected_code'])
        # compare_params = self.compare.compare_params_complete(result_interface=result['data'],
        #                                                       params_to_compare=json.dumps(datalist['expected_key']))
        # self.assertTrue(result['code'] == '0000', msg="接口返回状态码不是200")
        # self.assertTrue(compare_code['code'] == '0000', msg="参数值比较不一致")
        # self.assertTrue(compare_params['code'] == '0000', msg="必须返回的参数不包含在实际返回参数中")
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)
