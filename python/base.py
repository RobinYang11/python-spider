# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 15:32:14 2017

@author: Administrator
"""

import pymysql

class base(object):
    
    def __init__(self):
        print("base::init")
        self.sqlConfig={
             'host':'127.0.0.1',
              'port':3306,
              'user':'root',
              'password':'toor',
              'db':'robin',
              'charset':'utf8mb4',
              'cursorclass':pymysql.cursors.DictCursor,
        }
        
    def conncetDB(self):
        print("base::connectDB")
        
    def onRun(self):
        self.conn= pymysql.connect(**self.sqlConfig)
        self.cursor=self.conn.cursor()
        sql="select * from user"
        self.cursor.execute(sql)
        res=self.cursor.fetchall()
        print(res)
        print("base::onRun")
        
    def closeDB(self):
        self.cursor.close()
        self.conn.close()
        print("base::closeDB")
        
        