# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os,sys
sys.path.append("python")


if __name__=="__main__":
    files=os.listdir("python")
    for cls in files:
        clsName= os.path.splitext(cls)[0]
        print(clsName)
        if clsName !="base" and clsName!="__pycache__":
            importModule="from "+clsName+" import *"
            exec(importModule)
            api=eval(clsName+"()")
            api.onRun()
         
