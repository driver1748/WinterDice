# -*- coding:utf-8-*
# Copyright (C) 2021 WinterUnderTheSnow

"""
Event体系主模块
"""

def _init() -> None:
    global gv
    from modules import global_values as gv
    global get_type
    from modules.get_type import get_type
    global time
    import time
    gv.set("ex-notify",None)
    gv.set("notify",None)
    global events
    from modules import events

def announce(self, event:object) -> None:
    """
    公布Event的工具
    """
    gv.set("ex-notify",gv.get("notify"))
    gv.set("notify",event)
        

class event(object):
    def __init__(self) -> None:
        super().__init__()
        try:
            self.event_name = self.event_name + "event"
        except:
            self.event_name = "event"
    def announce(self) -> None:
        pass