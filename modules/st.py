# -*- coding:utf-8-*-
# Copyright (C) 2022 WinterUnderTheSnow
"""将.st指令转换为json的形式方便保存"""


def run(command: str, outputs: dict, _dict: dict):
    parameter = command[3:len(command)]
    parameter = parameter.replace(" ", "")  # 去掉空格
    if parameter == "clear" or parameter == " clear":  # 清空属性值
        print(outputs["skills_cleared"])
        return {}
    elif parameter[0:4] == "show" or parameter[0:5] == " show":  # 展示属性值
        if parameter[0:4] == "show" and len(parameter) == 4:
            print(_dict)
        else:  # 显示单独的属性值（也可以同时显示多个）
            skill_name = parameter[4:len(parameter)]
            for i in _dict.keys():
                if i == skill_name:
                    print(outputs["show_skill"] % (i, _dict[i]))
                    break
        return _dict
    strange_chars = '@#$&*()"%-+=/;:,.€£¥_[]}{§|~…\<>!?'
    legal = True
    word = ""
    is_word_int = False
    last_word = ""
    for i in strange_chars:
        if i in parameter:
            print(outputs["illegal_char"])
            legal = False
    if legal:
        try:
            for i in parameter:  # 遍历字符串中的每一个字符，通过拼接字符串并判断数据类型，写入字典
                try:
                    int(i)  # 判断这个字符是否为数字，是则继续执行，否则报错进入except
                    if is_word_int:  # 上个字符是数字，这个字符也是数字
                        word = word + str(i)
                    else:  # 上个字符是文字，这个字符是数字
                        last_word = word
                        word = str(i)
                        is_word_int = True
                except ValueError:  # 如果这个字符不是数字就触发ValueError
                    if is_word_int:  # 上个字符是数字，这个字符是文字
                        if not last_word == "":
                            try:
                                _dict[last_word] = int(word)
                                last_word = word
                            except ValueError:
                                break
                        word = i
                        is_word_int = False
                    else:
                        word = word + i
            _dict[last_word] = int(word)
            print(outputs["skill_set"])
            return _dict
        except:
            print(outputs["wrong_expression"])
            return _dict
