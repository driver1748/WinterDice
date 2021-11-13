# -*- coding:utf-8-*-
#检查并初始化规则书

from modules import global_values as gv
def fullrun(dont_skip_checking = True):
    """
    检查并初始化规则书
    """
    names = gv.get("judgement_file_names")
    paths = gv.get("judgement_file_paths")
    if dont_skip_checking:    
        for count in range(len(names)):
            name = names[count]
            if name == "list.json" or name == "__init.py__":
                pass
            else:
                __import__("judgement_modules.",name.rsplit('.',1)[0])