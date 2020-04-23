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
    def test_01_bodyChanges(self, datalist):
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_home.growChangeByDay)
    def test_02_growChangeByDay(self, datalist):
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_home.motherChanges)
    def test_03_motherChanges(self, datalist):
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_home.babyChanges)
    def test_04_babyChanges(self, datalist):
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_home.babyChangeByDay)
    def test_05_babyChangeByDay(self, datalist):
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)

    @ddt.data(*interface_home.vaccinList)
    def test_06_vaccinList(self, datalist):
        result = self.testcase.test_case(datalist)
        self.assertTrue(result)
