#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: test_interface_home_bodyChanges.py
@time: 2020/04/21
"""
import unittest
import ddt
from common.base_request import RequestInterface
from common.base_compare import CompareParm
import requests
from public import config
import json
"""
辣妈宝宝发育列表接口
"""

_url = "/interface/home/bodyChanges"
url = config.base_url+_url
h = {
    "Content-Type": "application/json"
    }
data = {}


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.r = RequestInterface()
        cls.compare = CompareParm()

    def test(self):
        result = self.r.http_request(interface_url=url, headerdata=h, interface_param=data, request_type="post")
        print(result['data'])
        expected_key = ['status', 'msg', 'data']
        compare_result = self.compare.compare_params_complete(result_interface=result['data'], params_to_compare=json.dumps(expected_key))
        self.assertTrue(result['code'] == '0000')
        self.assertTrue(compare_result['code'] == '0000')
