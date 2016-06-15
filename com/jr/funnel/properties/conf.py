#!/usr/bin/python
#coding=utf8
"""
__author__ = 'wanghaifei'
 Time: 15-7-23 下午6:02
 
"""
#spark集群 访问地址
sparkURL="spark://spark-jrdata-12.pekdc1.jdfin.local:7077"

#hadoop集群namenodehost
nameNodeHost="ns1"

#读取hdfs上的规则
dim_model_url_new="/funnelNew/input/dim/funnel_model_rule_info.txt"

#点击流日志
click_jr_log_url_dir="/user/hive/warehouse/db1.db/jdjr_click_log_test_1"

#分区表示字段
hive_table_partition="/dt="

#行    分隔符
delimiter_row='\r\n'

#字段信息以及表内容 分隔符
delimiter_column='\t'

