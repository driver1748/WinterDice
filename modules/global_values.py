# -*- coding:utf-8-*-
# 全局变量管理模块
 
#初始化
def _init():
    global GLOBALS_DICT
    GLOBALS_DICT = {}

#设置全局变量
def set(name, value):
    try:
        GLOBALS_DICT[name] = value
        return True
    except KeyError:
        return False

#避免字典报错
def setdict(name, value):
    try:
        GLOBALS_DICT[name] = [value]
        return True
    except KeyError:
        return False

#读取全局变量
def get(name):
    try:
        return GLOBALS_DICT[name]
    except KeyError:
        return "Not Found"