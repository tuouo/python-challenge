#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/rock/arecibo.html
'''
import urllib.request as ur, re
url = "http://www.pythonchallenge.com/pc/rock/warmup.txt"
mgr = ur.HTTPPasswordMgrWithDefaultRealm()
mgr.add_password(None, url, 'kohsamui', 'thailand')
opener = ur.build_opener(ur.HTTPBasicAuthHandler(mgr))
req = opener.open(url)
data = req.read()
#print(data)
# with open("output.rtf", 'wb') as r:
#         r.write(data)

numbers = data.split(b'\n')
#print(numbers)
lines = []
reg = re.compile(b'(\d+)')
for i in numbers:
    if reg.match(i):
        lines.append(list(reg.findall(i)))
# print(lines)