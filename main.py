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
judgement_file_names = os.listdir("./judgement_modules/")
print(judgement_file_names)
for index in range(len(judgement_file_names)):
    operating = judgement_file_names[index]

gv.set("judgement_file_names",judgement_file_names)
#  文件名拼接路径
judgement_file_paths = [os.path.join("./judgement_modules/",file) for file in judgement_file_names]
gv.set("judgement_file_paths",judgement_file_paths)
print(judgement_file_paths)
# 调用子模块，检查规则书是否存在问题并导入
from modules import init_judgement_modules
init_judgement_modules.fullrun()