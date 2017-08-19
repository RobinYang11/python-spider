# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os,sys
from qccSpider import *
from sgSpider import *

if __name__=="__main__":
    sys.path.append("python")
    abs="python"
    files=os.listdir(abs)
    for cls in files:
        clsName= os.path.splitext(cls)[0]
        print(clsName)
        if clsName !="base" and clsName!="__pycache__":
            api=eval(clsName+"()")
            api.onRun()
         
