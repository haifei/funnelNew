"""
__author__ = 'wanghaifei'
 Time: 15-7-28 下午9:18
 
"""
import  collections
import  datetime
from com.jr.funnel.optaion.funnelFilter import FunnelFilter


class A:
    def __init__(self):
        self.one="one"

    def read(self):
        print('read int class A')
class B:
    def __init__(self):
        self.two="two"

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
    def printselfnum(self):
        print(self.one,self.two)
    def myread(self):
        print('read in class C')
        A.read(self)








if __name__ == "__main__":
    C().myread()



    line="aaa bbb ccc"
    words=line.split(" ")
    print(words[0])

    date1=datetime.datetime.now()
    date2=date1-datetime.timedelta(days=1)
    print("now date:"+str(date1))
    print("now date:"+date1.strftime("%Y%m%d"))
    print("yesterday :"+date2.strftime("%Y%m%d"))

    d={}
    d['a']='A'
    d['c']='C'
    d['b']='B'

    for k, v in d.items():
        print(k, v)
    print('\nOrderedDict:')
    d = collections.OrderedDict()

    d['a'] = 'A'
    d['c'] = 'C'
    d['b'] = 'B'
    for k, v in d.items():
        print(k, v)

    flag=True
    if not flag:
        print("is true")

    print("--------------------------------------")



