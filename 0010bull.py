#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/return/bull.html

len(a[30]) = ?
'''	
import re
reg = re.compile(r'((?P<w>\d)(?P=w)*)')
n = '1'
for i in range(30):
    n = "".join(list(map(lambda x: '%s%s' % (len(x[0]), x[1]), reg.findall(n))))

print(len(n))