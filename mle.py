# coding: utf-8
from __future__ import unicode_literals
import json
import collections
from math import log

EPS = 1
SCALE = 5
d=collections.defaultdict(lambda:EPS)
d.update(json.load(open('dict.json')))
#d.update(json.load(open('sogou.json')))
 
def fenci(s):
    l=len(s)
    p=[1 for i in range(l + 1)]
    t=[1 for i in range(l)]
    for i in range(l-1, -1, -1):
        for k in range(1, l-i+1):
            if(log(d[s[i:i+k]] * SCALE) + p[i+k] > p[i]):
                p[i]=log(d[s[i:i+k]] * SCALE) + p[i+k]
                t[i]=k
    print 'sum:',p[0]
    i=0
    while i<l:
        yield s[i:i+t[i]]
        i=i+t[i]
 
 
if __name__ == '__main__':
    s='疾步路过书店隔着玻璃看见埋头阅读的人们很想一砖头砸破他们的平静我就是羡慕嫉妒恨虽然如果我很悠闲但也懒得演绎书店读书一幕'
    print '|'.join(list(fenci(s))).encode('utf-8')
