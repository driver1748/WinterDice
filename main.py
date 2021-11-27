# -*- coding:utf-8-*
# Copyright (C) 2021 WinterUnderTheSnow
version = "v0.0.0_undeveloped"
build = 0
BE = True
debug_level = 999

#初始化变量
F = False
T = True

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


#初始化依赖库
if debug_level >= 1:
    print("Initializing modules...")
import os
import json
import socket
from json_minify import *
import time
import importlib
import threading

#初始化模块
if debug_level >= 1:
    print("Initializing built-in modules...")
from modules import global_values as gv
gv._init()

#读取设置和回应字典
if debug_level >= 2:
    print("Reading settings...")
with open(r"settings.json", "r", encoding="utf-8") as settings:
    settings = settings.read()
    settings = json.loads(json_minify(settings))
gv.set("settings",settings)
if debug_level >= 2:
    print("Reading outputs...")
with open(r"output_texts.json", "r", encoding="utf-8") as outputs:
    outputs = outputs.read()
    outputs = json.loads(json_minify(outputs))
gv.set("outputs",outputs)

print(outputs['my_name'] +outputs['booting'])

#打开log端口
#socket_logger = socket.socket()
#socket_logger.bind((settings["logger_address"],settings["logger_port"]))

#初始化规则书
# 获取规则书列表
#  获取文件名
judgement_folder_names_raw = os.listdir("./judgement_modules/")
judgement_folder_names = []
print(judgement_folder_names_raw)
avoided_files = []
for i in range(len(judgement_folder_names_raw)):
    if judgement_folder_names_raw[i] == "__init__.py":
        judgement_folder_names_raw[i] = "pass"
    else:
        judgement_folder_names.append(judgement_folder_names_raw[i])
gv.set("judgement_file_names",judgement_folder_names)

# 调用子模块，初始化规则书
from modules import init_judgement_modules
init_judgement_modules.fullrun()