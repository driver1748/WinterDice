# -*- coding:utf-8-*
# Copyright (C) 2022 WinterUnderTheSnow
version = "0.0.0_undeveloped"
build = 0
BE = True
debug_level = 999

#Import sys
try:
    import sys
except:
    print("Fatal : Failed to import sys!!")
    raise Exception("Failed to import sys!Exiting...")
sys.dont_write_bytecode = True
for reading_argv_num in range(len(sys.argv)):
    reading_argv = sys.argv[reading_argv_num]
    reading_argv = reading_argv.split("=", 1)

#初始化模块
from aifc import Error
from modules import global_values as gv, response_classes
gv._init()

gv.set("version",version)
gv.set("build",build)
gv.set("BE",True)
if BE:
    gv.set("BE_str"," *Pre-release*")
else:
    gv.set("BE_str",None)

#初始化依赖库
import os
import json
import socket
from json_minify import *
import time


#读取设置和回应字典
with open(r"settings.jsonc", "r", encoding="utf-8") as settings:
    settings = settings.read()
    settings = json.loads(json_minify(settings))
gv.set("settings",settings)
with open(r"output_texts.jsonc", "r", encoding="utf-8") as outputs:
    outputs = outputs.read()
    outputs = json.loads(json_minify(outputs))
gv.set("outputs",outputs)

print("# Copyright (C) 2022 WinterUnderTheSnow All rights reserved")
print("# This program is licensed under GPLv3 !")
print("")

# 显示更新日志
if settings["show_update_log"]:
    try:
        with open(r"update_log.txt", "r", encoding="utf-8") as update_log:
            update_log = update_log.read()
            print(update_log)
    except FileNotFoundError:
        pass


print(outputs['my_name'] +outputs['booting'])

#打开log端口
#socket_logger = socket.socket()
#socket_logger.bind((settings["logger_address"],settings["logger_port"]))

#初始化规则书
# 获取规则书列表
#  获取文件名
judgement_folder_names_raw = os.listdir("./judgement_modules/")
judgement_folder_names = []
avoided_files = []
for i in range(len(judgement_folder_names_raw)):
    if judgement_folder_names_raw[i] == "__init__.py":
        judgement_folder_names_raw[i] = "pass"
    else:
        judgement_folder_names.append(judgement_folder_names_raw[i])
gv.set("judgement_file_names",judgement_folder_names)

# 调用子模块，初始化规则书
from modules import init_judgement_modules
judgement_modules_map, command_reg = init_judgement_modules.fullrun()
keys_list = list(command_reg.keys())

#封装一些需要用的函数
def try_to_get_int(a,b):
    """获取需求范围内的整数"""
    try:
        result = int(input("> "))
        if a <= result and b >= result:
            return result
        else:
            raise ValueError("Number entered out of range.")
    except  ValueError:
        print(outputs["please_enter_int_between"] % (a,b))
        try_to_get_int(a,b)

#开始接受指令
print(outputs["init_complete"] % len(judgement_modules_map["list"]))
while True:
    raw_command = str(input("> ")) #这是一个指示光标
    command = raw_command.lower() #全部改成小写方便程序判断
    if command == "quit" or command == "q": #输入这个即退出
        sys.exit()
    if command == "help" or command == "h": #HALP
        for i in range(len(outputs["help"])):
            print(outputs["help"][i])
    if command == "list" or command == "l": #显示已加载的规则书
        print(judgement_modules_map["name_list"])
    if command == "version" or command == "v": #显示版本
        print("WinterDice version %s , build %i" % (version,build))
        if BE:
            print("Pre-release")
    if command == "commands" or command == "c": #显示已加载的规则书指令
        print(keys_list)
        print(outputs["remind_dot"])
    if command[0:1] == "." or command[0:1] == "。": #带点的命令全部交给规则书处理
        standard_command = raw_command[1:len(command)+1] #把点去掉
        #因为考虑到不是所有指令都在关键字与参数间有空格，所以判断方法为：用command_reg中的所有命令去遍历字符串
        trigger_list = []
        for i in range(len(keys_list)):
            find_result = standard_command.find(keys_list[i],0,len(keys_list[i])) #检测指令关键字，即第1到第（关键字长度+1）个字符是否为关键字
            if find_result == -1:
                pass
            else:
                trigger_list.append(i) #小Magic，保存匹配上的索引而不是关键词
            # 到这里判断就完成了，下面是让用户选择执行
        if len(trigger_list) > 1: #如果匹配到的关键词多于一个，那就让用户选一个命令执行
            print(outputs["multiple_purposes"])
            trigger_choice_list = ""
            for i in range(len(trigger_list)): #生成列表
                #拼接提示字符串
                trigger_choice_list = trigger_choice_list + "[" + str(i) + "] " + keys_list[trigger_list[i]] + " "
            print(trigger_choice_list)
            #拿到合法的数回复
            choice = try_to_get_int(0,len(trigger_list)-1)
        else: #如果匹配到的关键词只有一个那就取列表中唯一的一项
            choice = 0
        try: #加上try，防止用户输入一个不存在的指令程序就报错推出
            command_to_trigger = getattr(command_reg[keys_list[trigger_list[choice]]],keys_list[trigger_list[choice]])
            parameter = raw_command[len(keys_list[trigger_list[choice]]):len(raw_command)]
            judgement = command_to_trigger(parameter).result
            num = successful = text = None #清除上一次的结果

            #解包结果
            if isinstance(judgement,response_classes.response_with_num_and_success):
                num = judgement.num
                successful = judgement.successful
            elif isinstance(judgement,response_classes.response_with_num):
                num = judgement.num
            elif isinstance(judgement,response_classes.response_with_success):
                successful = judgement.successful
            elif isinstance(judgement,response_classes.response):
                pass
            else:
                raise Error("THIS IS IMPOSSIBLE")
            text = judgement.text
            #输出结果
            print(text)
        except IndexError: #不是合法指令那就不做回应
            pass