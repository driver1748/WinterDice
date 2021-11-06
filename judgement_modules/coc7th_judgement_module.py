# -*- coding:utf-8-*-
class importing:
    def __init__(self):
        self.base_rule = True
        self.based_on = "nothing"
        self.full_name = "Call Of Cthulu 7th"
        self.name = "COC7th"
    def init(self):
        return [self.base_rule ,self.based_on ,self.full_name ,self.name]
    def dictinit(self):
        return {
            "base_rule": self.base_rule,
            "based_on": self.based_on,
            "full_name": self.full_name,
            "name": self.name
        }
