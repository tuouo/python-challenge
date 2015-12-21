#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request as ur, re
reg = re.compile(r'<!--[\s\S]+<!--([\s\S]+)-->')
url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
data = ur.urlopen(url).read().decode('utf-8')
a = reg.findall(data)
# a = reg.findall(data, re.M)

result = {}
alph = ''
for i in a[0]:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
        alph += i
print(result)
for i in alph:
    if result[i] == 1:
        print(i, end = '')