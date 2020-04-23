#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: test_case.py
@time: 2020/04/22
"""
from public import config
import json
import unittest
from common.base_request import RequestInterface
from common.base_compare import CompareParm
from public import config
import json
import ddt
from data import interface_home

r = RequestInterface()
compare = CompareParm()


class TestCase(object):
    def test_case(self, datalist):
        print(datalist['interface'])
        print(datalist['msg'])
        url = config.base_url + datalist['url']
        result = r.http_request(interface_url=url, headerdata=datalist['h'],
                                interface_param=datalist['d'], request_type=datalist['mode'])
        compare_code = compare.compare_code(result_interface=result['data'], code=datalist['code'],
                                            expected_code=datalist['expected_code'])
        compare_params = compare.compare_params_complete(result_interface=result['data'],
                                                         params_to_compare=json.dumps(datalist['expected_key']))
        if result['code'] == '0000' and compare_code['code'] == '0000' and compare_params['code'] == '0000':
            return True
        else:
            return False
