#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: interface_home.py
@time: 2020/04/22
"""

bodyChanges = [
    {
     'interface': '辣妈宝宝发育列表接口',
     'msg': '没有参数',
     'url': '/interface/home/bodyChanges',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': '',
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'keyWords', 'keyWord', 'seeing', 'hearing', 'language', 'action',
                      'emotion', 'touching', 'tasting', 'know', 'mind', 'skill'],
     }
]

growChangeByDay = [
    {
     'interface': '辣妈根据怀孕天数 获取宝宝发育',
     'msg': 'week参数为1',
     'url': '/interface/home/growChangeByDay',
     'mode': 'post',
     'h': {'Content-Type': 'application/x-www-form-urlencoded'},
     'd': {'week': int(1)},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'week'],
     },

    {
     'interface': '辣妈根据怀孕天数 获取宝宝发育',
     'msg': 'week参数为a',
     'url': '/interface/home/growChangeByDay',
     'mode': 'post',
     'h': {'Content-Type': 'application/x-www-form-urlencoded'},
     'd': {'week': 'a'},
     'code': 'status',
     'expected_code': '0001',
     'expected_key': ['status', 'msg', 'data', 'week'],
     },

    {
     'interface': '辣妈根据怀孕天数 获取宝宝发育',
     'msg': 'week参数为空',
     'url': '/interface/home/growChangeByDay',
     'mode': 'post',
     'h': {'Content-Type': 'application/x-www-form-urlencoded'},
     'd': {'week': ''},
     'code': 'status',
     'expected_code': '0001',
     'expected_key': ['status', 'msg', 'data', 'week'],
     }
]

motherChanges = [
    {
     'interface': '孕妈妈妈变化列表接口',
     'msg': '没有参数',
     'url': '/interface/home/motherChanges',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': '',
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'keyWords', 'content', 'moodStar', 'moodContent', 'id', 'title',
                      'taiStar', 'taiContent'],
     }
]

babyChanges = [
    {
     'interface': '孕妈胎儿变化列表接口',
     'msg': '没有参数',
     'url': '/interface/home/babyChanges',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': '',
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'title', 'id', 'content'],
     }
]

babyChangeByDay = [
    {
     'interface': '孕妈根据怀孕天数 获取宝宝变化和妈妈变化',
     'msg': '参数为空',
     'url': '/interface/home/babyChangeByDay',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': '',
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'motherChange'],
     },
    {
     'interface': '孕妈根据怀孕天数 获取宝宝变化和妈妈变化',
     'msg': 'babyId=1，momId=1',
     'url': '/interface/home/babyChangeByDay',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'babyId': '1', 'momId': '1'},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'motherChange'],
     },
    {
     'interface': '孕妈根据怀孕天数 获取宝宝变化和妈妈变化',
     'msg': 'babyId=空，momId=1',
     'url': '/interface/home/babyChangeByDay',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'babyId': '', 'momId': '1'},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'motherChange'],
     },
    {
     'interface': '孕妈根据怀孕天数 获取宝宝变化和妈妈变化',
     'msg': 'babyId=1，momId=空',
     'url': '/interface/home/babyChangeByDay',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'babyId': '1', 'momId': ''},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'motherChange'],
     },
    {
     'interface': '孕妈根据怀孕天数 获取宝宝变化和妈妈变化',
     'msg': 'babyId=空，momId=空',
     'url': '/interface/home/babyChangeByDay',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'babyId': '', 'momId': ''},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'motherChange'],
     },
    {
     'interface': '孕妈根据怀孕天数 获取宝宝变化和妈妈变化',
     'msg': 'babyId=a，momId=a',
     'url': '/interface/home/babyChangeByDay',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'babyId': 'a', 'momId': 'a'},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'motherChange'],
     },
    {
     'interface': '孕妈根据怀孕天数 获取宝宝变化和妈妈变化',
     'msg': 'babyId=2.5，momId=2.5',
     'url': '/interface/home/babyChangeByDay',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'babyId': 'a', 'momId': 'a'},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'motherChange'],
     }


]

vaccinList = [
    {
     'interface': '疫苗列表',
     'msg': '没有参数',
     'url': '/interface/home/vaccinList',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': '',
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'title', 'timeInfo', 'bornMonth', 'info',
                      'prvents', 'program', 'warm', 'isAready', 'id'],
     },

    {
     'interface': '疫苗列表',
     'msg': 'babyId=123456,tel=13382822140',
     'url': '/interface/home/vaccinList',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'babyId': '123456', 'tel': '13382822140'},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'title', 'timeInfo', 'bornMonth', 'info',
                      'prvents', 'program', 'warm', 'isAready', 'id'],
     },
    {
     'interface': '疫苗列表',
     'msg': 'babyId=空,tel=13382822140',
     'url': '/interface/home/vaccinList',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'babyId': '', 'tel': '13382822140'},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'title', 'timeInfo', 'bornMonth', 'info',
                      'prvents', 'program', 'warm', 'isAready', 'id'],
     },
    {
     'interface': '疫苗列表',
     'msg': 'babyId=123456,tel=空',
     'url': '/interface/home/vaccinList',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'babyId': '123456', 'tel': ''},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'title', 'timeInfo', 'bornMonth', 'info',
                      'prvents', 'program', 'warm', 'isAready', 'id'],
     },
    {
     'interface': '疫苗列表',
     'msg': 'babyId=int(123456),tel=int(13382822140)',
     'url': '/interface/home/vaccinList',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'babyId': int(123456), 'tel': int(13382822140)},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'title', 'timeInfo', 'bornMonth', 'info',
                      'prvents', 'program', 'warm', 'isAready', 'id'],
     }
]

# vaccinManage = [
#     {
#      'interface': '指定宝宝的疫苗管理 设置完成或未完成',
#      'msg': '没有参数',
#      'url': '/interface/home/vaccinList',
#      'mode': 'post',
#      'h': {'Content-Type': 'application/json'},
#      'd': '',
#      'code': 'status',
#      'expected_code': '0000',
#      'expected_key': ['status', 'msg', 'data', 'title', 'timeInfo', 'bornMonth', 'info',
#                       'prvents', 'program', 'warm', 'isAready', 'id'],
#      },
#
#     {
#      'interface': '疫苗列表',
#      'msg': 'babyId=123456,tel=13382822140',
#      'url': '/interface/home/vaccinList',
#      'mode': 'post',
#      'h': {'Content-Type': 'application/json'},
#      'd': {'babyId': '123456', 'tel': '13382822140'},
#      'code': 'status',
#      'expected_code': '0000',
#      'expected_key': ['status', 'msg', 'data', 'title', 'timeInfo', 'bornMonth', 'info',
#                       'prvents', 'program', 'warm', 'isAready', 'id'],
#      },
#     {
#      'interface': '疫苗列表',
#      'msg': 'babyId=空,tel=13382822140',
#      'url': '/interface/home/vaccinList',
#      'mode': 'post',
#      'h': {'Content-Type': 'application/json'},
#      'd': {'babyId': '', 'tel': '13382822140'},
#      'code': 'status',
#      'expected_code': '0000',
#      'expected_key': ['status', 'msg', 'data', 'title', 'timeInfo', 'bornMonth', 'info',
#                       'prvents', 'program', 'warm', 'isAready', 'id'],
#      },
#     {
#      'interface': '疫苗列表',
#      'msg': 'babyId=123456,tel=空',
#      'url': '/interface/home/vaccinList',
#      'mode': 'post',
#      'h': {'Content-Type': 'application/json'},
#      'd': {'babyId': '123456', 'tel': ''},
#      'code': 'status',
#      'expected_code': '0000',
#      'expected_key': ['status', 'msg', 'data', 'title', 'timeInfo', 'bornMonth', 'info',
#                       'prvents', 'program', 'warm', 'isAready', 'id'],
#      },
#     {
#      'interface': '疫苗列表',
#      'msg': 'babyId=int(123456),tel=int(13382822140)',
#      'url': '/interface/home/vaccinList',
#      'mode': 'post',
#      'h': {'Content-Type': 'application/json'},
#      'd': {'babyId': int(123456), 'tel': int(13382822140)},
#      'code': 'status',
#      'expected_code': '0000',
#      'expected_key': ['status', 'msg', 'data', 'title', 'timeInfo', 'bornMonth', 'info',
#                       'prvents', 'program', 'warm', 'isAready', 'id'],
#      }
# ]