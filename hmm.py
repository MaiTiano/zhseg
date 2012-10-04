# coding: utf-8
from __future__ import unicode_literals
import json
from collections import defaultdict
from math import log

_data = json.load(open('data.json'))
for x in _data: exec("{0} = _data['{0}'];".format(x))

EPS = 1e-10

def _viterbi(obs, states=('B','M','E','S'), start_p=start_p, tran_p=tran_p, emit_p=emit_p):
    V = [{} for i in range(len(obs))]
    path = {}
    
    for y in states:
        V[0][y] = log(start_p[y] or EPS) + log(emit_p[y].get(obs[0], EPS))
        path[y] = [y]

 
    for t in range(1,len(obs)):
        newpath = {}
        for y in states:
            (prob, state) = max([( V[t-1][y0] +
                                   log(tran_p[y0].get(y,EPS)) + 
                                   log(emit_p[y].get(obs[t],EPS))
                                   , y0) for y0 in states])
            V[t][y] = prob
            newpath[y] = path[state] + [y]
        path = newpath

    return max([(V[len(obs)-1][y], path[y]) for y in states])

def cut(chars):
    p, mark = _viterbi(chars)
    print ' '.join(mark)
    next = 0
    for i,c in enumerate(chars):
        if mark[i] == 'S':
            if next < i:
                yield chars[next:i]
            yield chars[i:i+1]
            next = i+1
        elif mark[i] == 'B':
            if next < i:
                yield chars[next:i]
            next = i
        elif mark[i] == 'E':
            yield chars[next:i+1]
            next = i+1
    if next < len(chars):
        yield chars[next:]

if __name__ == '__main__':
    words = list(cut('疾步路过书店隔着玻璃看见埋头阅读的人们很想一砖头砸破他们的平静我就是羡慕嫉妒恨虽然如果我很悠闲但也懒得演绎书店读书一幕'))
    print '|'.join(words).encode('utf-8')
