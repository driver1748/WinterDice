# -*- coding:utf-8-*-
version = "v0.0.0_undeveloped"
build = 0
BE = True

#初始化库
print("Initializing system modules...")
import sys
sys.dont_write_bytecode = True
import os
import json

#初始化模块
print("Initializing built-in function modules...")
from modules import global_values as gv
gv._init()

print("Reading setting files...")
with open(r"settings.json", "r", encoding="utf-8") as settings:
    settings = json.load(settings)
gv.setdict("settings",settings)
with open(r"output_texts.json", "r", encoding="utf-8") as outputs:
    outputs = json.load(outputs)
gv.setdict("outputs",outputs)

print(settings['my_name'] +outputs['booting'])

#获取规则书列表
# 获取文件名
file_names = os.listdir("./judgement_modules/")
print(file_names)
# 文件名拼接路径
file_list = [os.path.join("./judgement_modules/",file) for file in file_names]
print(file_list)
#遍历检测规则书文件是否存在问题

#判定运行模式
