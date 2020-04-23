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


]  # 填入参数也提示参数为空

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

vaccinManage = [
    {
     'interface': '指定宝宝的疫苗管理 设置完成或未完成',
     'msg': '没有参数',
     'url': '/interface/home/vaccinManage',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': '',
     'code': 'status',
     'expected_code': '0001',
     'expected_key': ['status', 'msg'],
     },

    {
     'interface': '指定宝宝的疫苗管理 设置完成或未完成',
     'msg': 'vaccinId=3,babyId=123456,isAready=True,tel=13382822140',
     'url': '/interface/home/vaccinManage',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'vaccinId': '3', 'babyId': '123456', 'isAready': True, 'tel': '13382822140'},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg'],
     },
]  # 填入参数也提示参数错误，需要检查填入参数格式

pregnantExaminationList = [
    {
     'interface': '获取产检列表',
     'msg': '没有参数',
     'url': '/interface/home/pregnantExaminationList',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': '',
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'week', 'time', 'isEffective', 'id', 'plan', 'cgCheck',
                      'tsCheck', 'zdItem', 'warm'],
     },
    {
     'interface': '获取产检列表',
     'msg': 'tel=int(18118458589)',
     'url': '/interface/home/pregnantExaminationList',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': '',
     'code': 'status',
     'expected_code': '0001',
     'expected_key': ['status', 'msg', 'data', 'week', 'time', 'isEffective', 'id', 'plan', 'cgCheck',
                      'tsCheck', 'zdItem', 'warm'],
     },
    {
     'interface': '获取产检列表',
     'msg': 'tel=18118458589',
     'url': '/interface/home/pregnantExaminationList',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'tel': '18118458589'},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'week', 'time', 'isEffective', 'id', 'plan', 'cgCheck',
                      'tsCheck', 'zdItem', 'warm'],
     },
]

pregnantExaminationCheck = [
    {
     'interface': '设置对应宝宝的产检生效或失效',
     'msg': '没有参数',
     'url': '/interface/home/pregnantExaminationCheck',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': '',
     'code': 'status',
     'expected_code': '0001',
     'expected_key': ['status', 'msg'],
     },
    {
     'interface': '设置对应宝宝的产检生效或失效',
     'msg': 'isEffective=1,examinationId=1,tel=13382822140',
     'url': '/interface/home/pregnantExaminationCheck',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'isEffective': '1', 'examinationId': '1', 'tel': '13382822140'},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg'],
    },
    {
     'interface': '设置对应宝宝的产检生效或失效',
     'msg': 'isEffective=10,examinationId=1,tel=13382822140',
     'url': '/interface/home/pregnantExaminationCheck',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'isEffective': '10', 'examinationId': '1', 'tel': '13382822140'},
     'code': 'status',
     'expected_code': '0001',
     'expected_key': ['status', 'msg'],
    },
    {
     'interface': '设置对应宝宝的产检生效或失效',
     'msg': 'isEffective=1,examinationId=10,tel=13382822140',
     'url': '/interface/home/pregnantExaminationCheck',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'isEffective': '1', 'examinationId': '10', 'tel': '13382822140'},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg'],
    },
    {
     'interface': '设置对应宝宝的产检生效或失效',
     'msg': 'isEffective=1,examinationId=10,tel=1338282aaaa2140',
     'url': '/interface/home/pregnantExaminationCheck',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'isEffective': '1', 'examinationId': '10', 'tel': '1338282aaaa2140'},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg'],
    },
]  # 填入参数也提示参数错误，需要检查填入参数格式

articleTitles = [
    {
     'interface': '获取首页 科普文章导航栏的数据',
     'msg': '没有参数',
     'url': '/interface/home/bodyChanges',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': '',
     'code': 'status',
     'expected_code': '0001',
     'expected_key': ['status', 'msg', 'data', 'title', 'category'],
     },
    {
     'interface': '获取首页 科普文章导航栏的数据',
     'msg': 'type=空',
     'url': '/interface/home/bodyChanges',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'type': ''},
     'code': 'status',
     'expected_code': '0001',
     'expected_key': ['status', 'msg', 'data', 'title', 'category'],
    },
    {
     'interface': '获取首页 科普文章导航栏的数据',
     'msg': 'type=1',
     'url': '/interface/home/bodyChanges',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'type': '1'},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'title', 'category'],
    },
    {
     'interface': '获取首页 科普文章导航栏的数据',
     'msg': 'type=2',
     'url': '/interface/home/bodyChanges',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'type': '2'},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'title', 'category'],
    },
    {
     'interface': '获取首页 科普文章导航栏的数据',
     'msg': 'type=10',
     'url': '/interface/home/bodyChanges',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'type': '10'},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'title', 'category'],
    },
]  # 404 可能接口未开发

articleList = [
    {
     'interface': '获取首页分类文章的列表 分页',
     'msg': '没有参数',
     'url': '/interface/home/articleList',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': '',
     'code': 'status',
     'expected_code': '0001',
     'expected_key': ['status', 'msg', 'data', 'title', 'icon', 'subtitle', 'authName', 'authIcon', 'authInfo',
                      'url', 'id', 'totalCount'],
     },
    {
     'interface': '获取首页分类文章的列表 分页',
     'msg': 'category=空,page=空,size=空，type=空',
     'url': '/interface/home/articleList',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'category': '', 'page': '', 'size': '', 'type': ''},
     'code': 'status',
     'expected_code': '0001',
     'expected_key': ['status', 'msg', 'data', 'title', 'icon', 'subtitle', 'authName', 'authIcon', 'authInfo',
                      'url', 'id', 'totalCount'],
     },
    {
     'interface': '获取首页分类文章的列表 分页',
     'msg': 'category=1,page=1,size=1，type=1',
     'url': '/interface/home/articleList',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'category': '1', 'page': '1', 'size': '1', 'type': '1'},
     'code': 'status',
     'expected_code': '000',
     'expected_key': ['status', 'msg', 'data', 'title', 'icon', 'subtitle', 'authName', 'authIcon', 'authInfo',
                      'url', 'id', 'totalCount'],
     },
    {
     'interface': '获取首页分类文章的列表 分页',
     'msg': 'category=1,page=1,size=1，type=2',
     'url': '/interface/home/articleList',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'category': '1', 'page': '1', 'size': '1', 'type': '2'},
     'code': 'status',
     'expected_code': '000',
     'expected_key': ['status', 'msg', 'data', 'title', 'icon', 'subtitle', 'authName', 'authIcon', 'authInfo',
                      'url', 'id', 'totalCount'],
     },
    {
     'interface': '获取首页分类文章的列表 分页',
     'msg': 'category=1,page=1,size=1，type=10',
     'url': '/interface/home/articleList',
     'mode': 'post',
     'h': {'Content-Type': 'application/json'},
     'd': {'category': '1', 'page': '1', 'size': '1', 'type': '110'},
     'code': 'status',
     'expected_code': '000',
     'expected_key': ['status', 'msg', 'data', 'title', 'icon', 'subtitle', 'authName', 'authIcon', 'authInfo',
                      'url', 'id', 'totalCount'],
     },
]  # 404 可能接口未开发

hotSearchKey = [
    {
     'interface': '获取热门搜索和历史搜索',
     'msg': '没有参数',
     'url': '/interface/home/hotSearchKey',
     'mode': 'get',
     'h': '',
     'd': '',
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'data', 'hots'],
     }
]  # 404 可能接口未开发

delSearchKey = [
    {
     'interface': '首页搜索删除历史搜索',
     'msg': '没有参数',
     'url': '/interface/home/hotSearchKey',
     'mode': 'get',
     'h': '',
     'd': '',
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg'],
     }
]  # 404 可能接口未开发

hospitalList = [
    {
     'interface': '医疗地图医院列表',
     'msg': '没有参数',
     'url': '/interface/home/hospitalList',
     'mode': 'post',
     'h': {'Content-Type': 'application/x-www-form-urlencoded'},
     'd': '',
     'code': 'status',
     'expected_code': '0001',
     'expected_key': '',
     },

    {
     'interface': '医疗地图医院列表',
     'msg': 'page=1,size=1,name=1,type=0',
     'url': '/interface/home/hospitalList',
     'mode': 'post',
     'h': {'Content-Type': 'application/x-www-form-urlencoded'},
     'd': {'page': '1', 'size': '1', 'name': '1', 'type': '0'},
     'code': 'status',
     'expected_code': '0000',
     'expected_key': '',
    },
    {
     'interface': '医疗地图医院列表',
     'msg': 'page=1,size=1,name=1,type=10',
     'url': '/interface/home/hospitalList',
     'mode': 'post',
     'h': {'Content-Type': 'application/x-www-form-urlencoded'},
     'd': {'page': '1', 'size': '1', 'name': '1', 'type': '10'},
     'code': 'status',
     'expected_code': '0002',
     'expected_key': '',
    }
]

hospitalDetail = [
    {
     'interface': '医院详细信息',
     'msg': '没有参数',
     'url': '/interface/home/hospitalDetail',
     'mode': 'get',
     'h': '',
     'd': '',
     'code': 'status',
     'expected_code': '0001',
     'expected_key': '',
     },

    {
     'interface': '医院详细信息',
     'msg': 'id=1',
     'url': '/interface/home/hospitalDetail',
     'mode': 'get',
     'h': '',
     'd': 'id=1',
     'code': 'status',
     'expected_code': '0000',
     'expected_key': ['status', 'msg', 'name', 'addr', 'desc', 'telNum', 'icon', 'level', 'tips',
                      'doctors', 'name', 'department', 'info', 'hospitalName', 'desc', 'score', 'year',
                      'icon', 'telNum', 'id', 'goodAt'],
    }
]