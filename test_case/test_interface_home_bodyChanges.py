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
import yaml
"""
辣妈宝宝发育列表接口
"""

_url = "/interface/home/bodyChanges"
url = config.base_url+_url
h = {
    "Content-Type": "application/json"
    }
data = {}

data_path = config.data_path+'111.yml'
with open(data_path, "r+", encoding='utf-8') as file:
    y = yaml.load_all(file, Loader=yaml.FullLoader)
    print(y)


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.r = RequestInterface()
        cls.compare = CompareParm()

    def test(self):
        result = self.r.http_request(interface_url=url, headerdata=h, interface_param=data, request_type="post")
        expected_key = ['status', 'msg', 'data']
        compare_result = self.compare.compare_params_complete(result_interface=result['data'], params_to_compare=json.dumps(expected_key))
        self.assertTrue(result['code'] == '0000', msg="接口返回状态码不是200")
        self.assertTrue(compare_result['code'] == '0000', msg="必须返回的参数不包含在实际返回参数中")
