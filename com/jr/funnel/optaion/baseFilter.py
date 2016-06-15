#!/usr/bin/python
#coding=utf8
__author__ = 'wanghaifei'
"""
 Time: 15-7-31 上午9:58
"""
import re

class BaseFilter(object):



    def getList(self,line,rules):
        pass

    def match(self,url,matchUrl,matchRule):
        if  "equal"==matchRule:   #进行 等于判断
            return url==matchUrl
        elif "contains"==matchRule:     #进行 包含判断
             return matchUrl in url
        elif "pattern"==matchRule:    #进行 正则匹配
            return self.__regexMatch(url,matchUrl)
        else:
            return False

    def __regexMatch(self,url,matchUrl):
       pattern = re.compile(matchUrl)
       match=pattern.match(url)
       if match:
           return True
       return  False

