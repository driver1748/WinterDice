# -*- coding:utf-8-*-
# 全局变量管理模块
"""
用于程序间变量通信的模块 或者说，用于管理全局变量的模块
"""

def _init() -> None:
    """
    初始化全局变量管理模块
    """
    global global_dict
    global_dict = {}

def set(name:str, value) -> bool:
    """
    手动设置全局变量
    """
    try:
        global_dict[name] = value
        return True
    except KeyError:
        return False

def get(name:str):
    """
    读取全局变量
    """
    try:
        return global_dict[name]
    except KeyError:
        return "Not Found"
