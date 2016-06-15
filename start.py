#!/usr/bin/python
#coding=utf8
__author__ = 'wanghaifei'
"""
__author__ = 'wanghaifei'
 Time: 15-7-29 下午4:28

"""
import sys
import com.jr.funnel.funnelMain as funnelMain
import datetime

if __name__ == "__main__":
    print("start funnel activity")
    args=sys.argv
    print("length :%s"% len(args))
    #获取脚本启动日期，默认为前一天，形式为：20150722
    defaultDatetime=datetime.datetime.now()-datetime.timedelta(days=1)
    date=defaultDatetime.strftime("%Y%m%d")
    for index in range(len(args)):
        if args[index].startswith('-d'):
            date=args[index+1]
            print("content :%s"%args[index+1])
    funnelMain.run(date)