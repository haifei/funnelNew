#!/usr/bin/python
#coding=utf8

__author__ = 'wanghaifei'
"""
 Date: 15-7-23

"""
from pyspark import SparkContext
from operator import add
from com.jr.funnel.properties import conf
from com.jr.funnel.utils.spark_hdfs_read import *
from collections  import namedtuple
from com.jr.funnel.optaion.funnelFilter import FunnelFilter


#定义规则表对象
FunnelRule=namedtuple('FunnelRule',['funnelId','ruleId','level','requestRule','requestUrl',
                                    'refRule','refUrl','startTime','endTime','bizType'])
 #定义 运算过程中的日志对象
FunnelLog=namedtuple('FunnelLog',['funnelId','ruleId','timeStamp','uuid','sessionId','pin','startTime','endTime','bizType'])

funnelFilter=FunnelFilter()

def rowSplit(line):

    return  line.split(conf.delimiter_row)

def buildBean(line):
    lines=line.split(conf.delimiter_column,12)
    row=[]
    row.append(lines[0])
    row.append(lines[1])
    row.append(lines[2])
    row.append(lines[4])
    row.append(lines[5])
    row.append(lines[7])
    row.append(lines[8])
    row.append(lines[9])
    row.append(lines[10])
    row.append(lines[11])

    return FunnelRule._make(row)


def reduceFilter(line):
    #flag=False
    print(line)
    for row in line:
        if row[2]=='1':
            print("-------True")
            print(row)
            return True
    return False

def countSessionKey(line):
    key=line[4]+conf.delimiter_column+line[0]+conf.delimiter_column+line[1]
    return (key,1)

def run(date):

    """"
    加载hdfs上 业务提供的规则
    并封装成 FunnelRule对象
    例如：[FunnelRule(funnelId=u'1496', ruleId=u'896', level=u'1', requestRule=u'contains')]
    """""
    sc = SparkContext(appName="readHdfsFile",master=conf.sparkURL)

    rulesList=readFile(sc,conf.dim_model_url_new).flatMap(lambda line:line.split('\r\n')).map(buildBean).collect() #OrderedDict(

    rules_lookup = sc.broadcast(rulesList)

    """
      setp2:加载点击流日志与规则表比对,剔除无效日志， 生成后期数据分析结构(in 1-----> out N+)
      set4:产生新的key
      set5:
    """

    """
>>>rdd2=sc.parallelize([['1\t1',['1','1','2','a']],['1\t1',['1','1','1','b']],['2\t1',['2','1','1','b']]])
>>>rdd2.groupByKey().map(lambda line:list(line[1])).filter(lambda x:x[0][0]=='1').flatMap(lambda x:x).collect()
     [['1', '1', '2', 'a'], ['1', '1', '1', 'b']]
"""

    #conf.click_jr_log_url_dir+"/dt="+date

    clickLogRDD=readFile(sc,"/funnelNew/input/click_log/000000_0").map(rowSplit)

    clickLogRDD1=clickLogRDD.flatMap(lambda line:funnelFilter.getList(line[0],rules_lookup)).groupByKey()\
        .map(lambda line:line[1]).filter(reduceFilter).flatMap(lambda x:x).map(countSessionKey).\
        partitionBy(1).reduceByKey(add)

    clickLogRDD1.saveAsTextFile("/funnelNew/output/dt="+date)

    #print(result.collect())
    #funnelIDS=result.map(lambda line:(line.funnelId)).collect()

    #result=dimRules.flatMap(lambda x:x.split(conf.delimiter_column)).map(lambda item:(item)).collect();
    #result.saveAsTextFile("/apps/data/funnel_new/output")
    ##加载 点击流日志
   # clickLogs=readFile(conf.click_jr_log_url_dir+conf.hive_table_partition+ACTIVITY_DATE)

     #规则表和点击流日志合并
   # clickLogs.flatMap(lambda line:filterLog(dimRules,line))
