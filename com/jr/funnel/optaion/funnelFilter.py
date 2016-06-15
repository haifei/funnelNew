#!/usr/bin/python
#coding=utf8
import re

__author__ = 'wanghaifei'
"""
 Time: 15-7-31 上午11:13
"""
from  com.jr.funnel.optaion.baseFilter import BaseFilter
from com.jr.funnel.properties import conf



class FunnelFilter(BaseFilter):

    def getList(self,line,rules):
        p=re.compile(r' +')
        lines=p.split(line)
        requestUrl=lines[13]
        refUrl=lines[8]

        funnelLogs=[]

        keyList=[] #用户存储， 判断数据唯一性的 标示
        for rule in rules.value:
            #判断同一级别 有没有被判断过，判断立即 跳出该次
            key=rule.funnelId+conf.delimiter_column+rule.ruleId
            if key in keyList:
                continue

            requestFlag=BaseFilter.match(self,requestUrl,rule.requestUrl,rule.requestRule)

           #1.requestURl没有匹配上直接 退出本次循环
            if not requestFlag:
                continue

            refFlag=BaseFilter.match(self,refUrl,rule.refUrl,rule.refRule)

            #2. refurl匹配上或者 该规则为第一层级
            if refFlag or (rule.level=='1'):

                row=[]
                row.append(rule.funnelId) #0-----------漏斗id
                row.append(rule.ruleId)   #1-----------规则id -----与层级同一个意思
                row.append(rule.level)    #2-----------层级
                row.append(lines[0])     #3------------时间戳  timestamp
                row.append(lines[3])     #4------------uuid
                row.append(lines[4])     #5------------session ID
                row.append(lines[5])     #6-------------pin
                row.append(rule.startTime) #7-----------开始时间
                row.append(rule.endTime)  #8 -----------结束时间
                row.append(rule.bizType)  #9-------------业务类型


                #将新的key放入list中
                keyList.append(key)


                #FunnelLog._make(row)
                reduceKey=lines[4]+conf.delimiter_column+rule.funnelId
                funnelLogs.append((reduceKey,row))
        return  funnelLogs


    def isMatch(self,url,matchUrl,rule):
        return  BaseFilter.match(url,matchUrl,rule)