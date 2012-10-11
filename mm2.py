# coding: utf-8
from __future__ import unicode_literals
from __future__ import division
import json
import math

d = json.load(open('dict.json'))
#d = json.load(open('sogou.json'))
total = sum(d.itervalues())
log = lambda x: float('-inf') if not x else math.log(x)


def prob(w):
    if w in d:
        return d[w]
    else:
        return 1 if len(w) == 1 else 0


def fenci(s):
    l = len(s)
    p = [0 for i in range(l + 1)]
    t = [None for i in range(l)]

    for i in range(l - 1, -1, -1):
        p[i], t[i] = max((log(prob(s[i:i + k]) / total) + p[i + k], k)
                          for k in range(1, l - i + 1))

    print 'sum:', p[0]
    i = 0
    while i < l:
        yield s[i:i + t[i]]
        i = i + t[i]

if __name__ == '__main__':
    s = '每个人心里都有一个坑不小心掉进去半天才能爬出来'
    print '|'.join(fenci(s)).encode('utf-8')
