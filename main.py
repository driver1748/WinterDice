# -*- coding:utf-8-*
# Copyright (C) 2022 WinterUnderTheSnow
version = "v0.0.0_undeveloped"
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
from modules import global_values as gv
gv._init()

#初始化依赖库
import os
import json
import socket
from json_minify import *
import time
import importlib


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
def try_to_get_int():
    try:
        return int(input("> "))
    except TypeError:
        try_to_get_int()

#开始接受指令
print(outputs["init_complete"])
while True:
    command = str(input("> ")) #这是一个指示光标
    if command == "quit" or command == "Q": #输入这个即退出
        sys.exit()
    if command == "reload" or command == "R": #输入这个即重载规则书
        judgement_modules_map, command_reg = init_judgement_modules.fullrun()
        keys_list = list(command_reg.keys())
    if command[0:1] == "." or command[0:1] == "。": #带点的命令全部交给规则书处理
        standard_command = command[1:len(command)+1] #把点去掉
        #因为考虑到不是所有指令都在关键字与参数间有空格，所以判断方法为：用command_reg中的所有命令去遍历字符串
        trigger_list = []
        for i in range(len(keys_list)):
            find_result = standard_command.find(keys_list[i],0,len(keys_list[i])) #检测指令关键字，即第1到第（关键字长度+1）个字符是否为关键字
            if find_result == -1:
                pass
            else:
                trigger_list.append(i) #小Magic，保存匹配上的索引而不是关键词
        if len(trigger_list) > 1: #如果匹配到的关键词多于一个，那就让用户选一个命令执行
            print(outputs["multiple_purposes"])
            trigger_choice_list = ""
            for i in range(len(trigger_list)): #生成列表
                trigger_choice_list = trigger_choice_list + "[" + str(i) + "] " + keys_list[trigger_list[i]] + " "
            print(trigger_choice_list)

