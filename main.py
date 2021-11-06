version = "v0.0.0"

import sys
import os
import json
from modules import json_operating as jsonM

#获取骰娘设定
with open(r"settings.json", "r", encoding="utf-8") as settings:
	settings = json.load(settings)
from modules.init import init_dice_settings
init_dice_settings.run()

print(my_name +"正在初始化哦！")
#获取规则书列表

#判定运行模式
