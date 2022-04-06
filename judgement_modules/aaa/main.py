# -*- coding:utf-8-*-
"""
COC7th 规则书程序
"""

class init(object):
    """
    定义规则书基本信息，并进行初始化
    """
    def __init__(self):
        """
        自动初始化
        """
        global randint
        global gv
        from random import randint
        from modules import global_values as gv
        global _self
        global response_classes
        from modules import response_classes


        #基本信息
        self.base_rule = True
        self.based_on = "nothing"
        self.full_name = "aaa"
        self.name = "bbb"
        
        #将要注册的命令
        self.register_commands = ["ra","r","coc","rac"]


        #生成字典方便操作
        self.info_dict = {
            "base_rule": self.base_rule,
            "based_on": self.based_on,
            "full_name": self.full_name,
            "name": self.name,
            "register_commands": self.register_commands
        }
    def getdict(self):
        """
        返回字典格式的基本信息
        """
        return self.info_dict