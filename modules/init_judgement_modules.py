# -*- coding:utf-8-*-
#检查并初始化规则书
"""
用于检查并初始化规则书的模块
"""

from modules import global_values as gv
import importlib
import hashlib

judgement_modules_map = {"list":[],"list2module":{},"module2list":{}}
def fullrun():
    """
    检查并初始化规则书程序
    """
    command_reg = {} #创建指令注册表空字典
    judgement_file_names = gv.get("judgement_file_names")
    #遍历所有规则书
    for i in range(len(judgement_file_names)):
        index = 0 #初始化一个数字方便后续操作指令绑定表
        if judgement_file_names[i] == "pass":
            pass
        else:
            try:
                file_path = ".\\judgement_modules\\"+ judgement_file_names[i] +"\\main.py"
                #计算文件MD5作为规则书ID
                with open(file_path, "r", encoding="utf-8") as raw_file:
                    literal_name = hashlib.md5(str(raw_file).encode()).hexdigest()
                    print(literal_name)
                #通过动态加载模块的方式导入规则书
                judgement_module = importlib.import_module("judgement_modules."+judgement_file_names[i]+".main")
                #调用规则书模块
                _init = getattr(judgement_module,"init")
                _init = _init()
                #进行初始化
                judgement_modules_map["list"].append(literal_name) #往规则书列表中写入规则书ID
                judgement_modules_map["list2module"][literal_name] = judgement_module #将ID指向规则书模块
                judgement_modules_map["module2list"][judgement_module] = "a"
                judgement_modules_map[literal_name] = _init.getdict() #将规则书的基本信息写入字典中
                #遍历注册规则书中的命令，将指令与规则书绑定
                for j in range(len(_init.register_commands)):
                    command_reg[_init.register_commands[j]] = judgement_modules_map["list"][index]
                index += 1 #每次成功导入就把index加1，方便下一个规则书的指令绑定
            except FileNotFoundError:
                pass
    #完成规则书初始化，返回处理过的结果
    gv.set("judgement_modules_map", judgement_modules_map)
    gv.set("command_reg", command_reg)