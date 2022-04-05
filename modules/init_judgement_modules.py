# -*- coding:utf-8-*-
# Copyright (C) 2022 WinterUnderTheSnow
#检查并初始化规则书
"""
用于检查并初始化规则书的模块
"""

def fullrun():
    """
    检查并初始化规则书程序
    """
    from modules import global_values as gv
    import importlib

    command_confliction = gv.get("outputs")["command_confliction"]

    judgement_modules_map = {"list":[]}
    command_reg = {} #创建指令注册表空字典
    judgement_file_names = gv.get("judgement_file_names")
    #遍历所有规则书
    for i in range(len(judgement_file_names)):
        index = 0 #初始化一个数字方便后续操作指令绑定表
        if judgement_file_names[i] == "pass":
            pass
        else:
            try:
                #通过动态加载模块的方式导入规则书
                judgement_module = importlib.import_module("judgement_modules."+judgement_file_names[i]+".main")
                #调用规则书模块
                _init = getattr(judgement_module,"init")
                _init = _init() #初始化init类（执行__init__函数）
                #进行初始化
                judgement_modules_map["list"].append(judgement_module)
                #遍历注册规则书中的命令，将指令与规则书绑定
                for j in range(len(_init.register_commands)):
                    if _init.register_commands[j] in command_reg:
                        conflicted_with = command_reg[_init.register_commands[j]].init()
                        #规则书间指令冲突的提示信息
                        print(
                            str(
                            command_confliction["judgement_module"] + "  " +
                            _init.full_name + "  " +
                            command_confliction["in"] + "  " +
                            _init.register_commands[j] + "  " +
                            command_confliction["command"] +
                            command_confliction["is_already"] + "  " +
                            conflicted_with.full_name + "  " +
                            command_confliction["judgement_module"] +
                            command_confliction["is_registered_and_skip"] +
                            command_confliction["useless"]
                            )
                        )
                    else:
                        command_reg[_init.register_commands[j]] = judgement_module #把指令关键字所对应的规则书记录到command_reg小本本上
                index += 1 #每次成功导入就把index加1，方便下一个规则书的指令绑定
            except FileNotFoundError:
                pass
    #完成规则书初始化，返回处理过的结果
    gv.set("judgement_modules_map", judgement_modules_map)
    gv.set("command_reg", command_reg)
    return (judgement_modules_map, command_reg)