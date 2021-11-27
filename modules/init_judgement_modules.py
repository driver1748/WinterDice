# -*- coding:utf-8-*-
#检查并初始化规则书
"""
检查并初始化规则书的模块
"""
import sys
from modules import global_values as gv
import importlib

judgement_modules_map = []
def fullrun(dont_skip_checking = True):
    """
    检查并初始化规则书程序
    """
    names = gv.get("judgement_file_names")
    paths = gv.get("judgement_file_paths")
    if dont_skip_checking:
        for count in range(len(names)):
            name_operating = names[count]
            suffix_name_operating = name_operating[1]
            name_operating = name_operating.rsplit('.',1)[0]
            if name_operating == "list.json" or name_operating == "__init.py__" or not suffix_name_operating ==  "py":
                pass
            else:
                name_operating = "judgement_modules." + name_operating
                print(name_operating)
                importlib.import_module(name_operating,)