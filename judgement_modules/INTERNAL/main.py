# -*- coding:utf-8-*-
# Copyright (C) 2022 WinterUnderTheSnow
"""
内置掷骰命令
"""
import re
from modules import global_values as gv
from modules import response_classes
import random

class init(object):
    """
    定义规则书基本信息，并进行初始化
    """
    def __init__(self):
        """
        自动初始化
        """

        #规则书全名
        self.full_name = "INTERNAL JUDGEMENT MODULE"
        #规则书简称
        self.name = "INTERNAL"
        
        #将要注册的命令
        self.register_commands = ["r","bot"]


        #生成字典方便操作
        self.info_dict = {
            "full_name": self.full_name,
            "name": self.name,
            "register_commands": self.register_commands
        }

class r(object): #.r指令
    def __init__(self, parameter:str=None):
        r_parameter = parameter.lower()


class bot(object): #.bot指令
    def __init__(self,parameter:str=None):
        self.result = response_classes.response("WinterDice on python by WinterUnderTheSnow.\n一个轻量级、可自定义规则书、开源的命令行TRPG掷骰机器人,\n版本:"+gv.get("version")+gv.get("BE_str")+"\n遵循GPLv3开源协议，项目地址:\nhttps://github.com/driver1748/WinterDice")