# -*- coding:utf-8-*
# Copyright (C) 2022 WinterUnderTheSnow
"""定义规则书回应的类"""

# 要注意的是，只有text里的内容玩家会看到，是否成功和附加的数值都是给程序处理的
class response(object):
    """基本回应，只包含文字"""
    def __init__(self,text=None) -> None:
        self.text = text

class response_with_success(response):
    """文字+是否成功的回应"""
    def __init__(self, successful, text=None) -> None:
        super().__init__(text)
        self.successful = successful

class response_with_num(response):
    """文字+一个需要被程序调用的数值的回应"""
    def __init__(self, num, text=None) -> None:
        super().__init__(text)
        self.num = num

class response_with_num_and_success(response):
    """文字+一个需要被程序调用的数值+是否成功的回应。请注意此类继承respond类"""
    def __init__(self, successful, num, text=None) -> None:
        super().__init__(text)
        self.successful = successful
        self.num = num