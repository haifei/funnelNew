#!/usr/bin/python
#coding=utf8
__author__ = 'wanghaifei'
"""
 Date: 15-7-23
"""

from com.jr.funnel.properties import conf

def  readFile(sc=None,path=None,nameNodeHost=conf.nameNodeHost):
    if path is None:
      print("path is not setting")
    #读取文本文件
    return sc.textFile("hdfs://"+nameNodeHost+path)

def  readLocalFile(sc=None,path=None):
    if path is None:
        print("path is not setting")
        #读取文本文件

    return sc.textFile(path)

def readDirFiles(sc=None,path=None,nameNodeHost=conf.nameNodeHost):
    if path is None:
        print("path is not setting")
    #sc1 = SparkContext(appName="readHDFSFiles",master=sparkURL)

    #读取目录下的所有文件
    return sc.wholeTextFiles("hdfs://"+nameNodeHost+path)
