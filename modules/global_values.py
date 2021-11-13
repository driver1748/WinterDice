# -*- coding:utf-8-*-
# 全局变量管理模块
import time

def _init(with_min_mode:bool = False):
    """
    初始化全局变量管理模块
    """
    global global_dict
    global_dict = {}
    #加入附加信息
    if not with_min_mode:
        global_dict["init_time"] = time.strftime(r'%Y-%m-%d %H:%M:%S', time.localtime())
    global min_mode
    min_mode = with_min_mode

def seto(name:str, value, with_time_stamp:bool=True, ts:bool=True):
    """
    设定带有额外信息的全局变量
    最小化模式中无法使用。
    """
    try:
        if name in global_dict:
            if global_dict[name][1]:
                return False
        global_dict[name] = {"value":value}
        if with_time_stamp or ts:
            global_dict[name]["timestamp"] = time.strftime(r'%Y-%m-%d %H:%M:%S', time.localtime())
        return True
    except:
        return False

def set(name:str, value):
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
    读取原始的全局变量
    """
    try:
        return global_dict[name]["value"]
    except KeyError:
        return "Not Found"
    except TypeError:
        return global_dict[name]

def geto(name:bool):
    """
    读取带有额外信息的全局变量
    """
    try:
        return global_dict[name]
    except KeyError:
        return "Not Found"
