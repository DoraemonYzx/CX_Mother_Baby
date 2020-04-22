#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: interface_home.py
@time: 2020/04/22
"""

bodyChanges = [
    {'url': '/interface/home/bodyChanges',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': '',
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data'],
     },

    {'url': '/interface/home/bodyChanges',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': '',
     'code': 'status',
     'expected_code': '0001',
     'expected_key': ['status', 'msg', 'data'],
     }
]
