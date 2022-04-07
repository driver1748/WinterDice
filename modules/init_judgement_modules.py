# -*- coding:utf-8-*-
# Copyright (C) 2022 WinterUnderTheSnow
#检查并初始化规则书
"""
用于检查并初始化规则书的模块
"""

from configparser import Error


def fullrun():
    """
    检查并初始化规则书程序
    """
    from modules import global_values as gv
    from modules import response_classes
    import importlib

    outputs = gv.get("outputs")

    judgement_modules_map = {"list":[], "name_list":[]}
    command_reg = {} #创建指令注册表空字典
    judgement_file_names = gv.get("judgement_file_names")
    #遍历所有规则书
    for i in range(len(judgement_file_names)):
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
                judgement_modules_map["name_list"].append(judgement_module.init().full_name)
                #遍历注册规则书中的命令，将指令与规则书绑定
                for j in range(len(_init.register_commands)):
                    try: #进行简单的检验，避免规则书问题导致程序崩溃（虽然如果前面就报错了就没用了）
                        check_class = getattr(judgement_module, _init.register_commands[j])().result #检查调用过程是否会报错
                        #检查返回内容是否合规
                        if isinstance(check_class,response_classes.response_with_num) or isinstance(check_class,response_classes.response_with_num_and_success) or isinstance(check_class,response_classes.response_with_success) or isinstance(check_class,response_classes.response):
                            pass
                        else:
                            raise Error
                        #检验规则书是否含有标准的基本信息
                        check_init = getattr(judgement_module, "init")
                        [check_init().full_name,check_init().name,check_init().register_commands]
                        #没问题就继续注册
                        if _init.register_commands[j] in command_reg:
                            conflicted_with = command_reg[_init.register_commands[j]].init() #获取已经注册的指令所对应的规则书
                            #规则书间指令冲突的提示信息
                            print(
                                str(
                                outputs["command_confliction"]["judgement_module"] + "  " +
                                _init.full_name + "  " +
                                outputs["command_confliction"]["in"] + "  " +
                                _init.register_commands[j] + "  " +
                                outputs["command_confliction"]["command"] +
                                outputs["command_confliction"]["is_already"] + "  " +
                                conflicted_with.full_name + "  " +
                                outputs["command_confliction"]["judgement_module"] +
                                outputs["command_confliction"]["is_registered_and_skip"] +
                                outputs["command_confliction"]["useless"]
                                )
                            )
                        else:
                            command_reg[_init.register_commands[j]] = judgement_module #把指令关键字所对应的规则书记录到command_reg小本本上
                    except:
                        print(outputs["judgement_module_error"] % (_init.full_name,_init.register_commands[j]))
            except FileNotFoundError:
                pass
    #完成规则书初始化，返回处理过的结果
    gv.set("judgement_modules_map", judgement_modules_map)
    gv.set("command_reg", command_reg)
    return (judgement_modules_map, command_reg)