#!/usr/bin/python
#coding=utf8
import re
from datetime import datetime,  timedelta
__author__ = 'wanghaifei'
"""
 Time: 15-8-12 下午5:51
"""

li=[[[1,2],[3,4]],[[5,6]],[[7,8]]]
print ([j for i in li for j in i])
print('----------------------------------')
#or
li2=[[[[1,2],[3,4]]],[[5,6]],[[7,8]]]
from itertools import chain
print(list(chain(chain(*li2))))
print('----------------------------------')
#or
a=[[1,2],[3,4],[5,6]]
t=[]
[t.extend(i) for i in a]
print(t)
print('----------------------------------')
#or
li1=[[[[1,2],[3,4]]],[[5,6]],[[7,8]]]
print(sum(sum(li1,[]),[]))
print('----------------------------------')
li3=[[1,2,3],[4,5,6]]
print("-----------------------------------")
line='1436098944527   www.100000      27.194.6.88     03fd9c9dcee705a010ab99651289b2db        03fd9c9dcee705a010ab99651289b2db|2      -1      UA-J2011-12     http://m.z.jd.com/topicListDetail.action?projectId=12786        http://m.z.jd.com/project/details/12786.html    je%3d0$sc%3d24-bit$sr%3d1080x1920$ul%3dzh-cn$cs%3dUTF-8$dt%3d%e4%ba%ac%e4%b8%9c%e4%bc%97%e7%ad%b9%e8%a7%a6%e5%b1%8f%e7%89%88$hn%3dm.z.jd.com$fl%3d-$os%3dlinux$br%3dsafari$bv%3d4.0$wb%3d1428932491017$xb%3d1428932491017$yb%3d1436098923$zb%3d2$cb%3d1$usc%3dm.z.jd.com$ucp%3d-$umd%3dreferral$uct%3d-$lt%3d0$ct%3d1436098922545$tad%3d-$pinid%3d-     c108d9716dc24772b1bcbb8d94008dc9        -1      1436098944527   http://jr.jd.com/'
p=re.compile(r' +')
lines=p.split(line)
print(lines)

day=datetime.today() - timedelta(days=1)
print(day)

