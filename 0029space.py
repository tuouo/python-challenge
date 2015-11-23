#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/ring/guido.html
'''
import urllib.request as ur, struct, bz2
url = "http://www.pythonchallenge.com/pc/ring/guido.html"
mgr = ur.HTTPPasswordMgrWithDefaultRealm()
mgr.add_password(None, url, 'repeat', 'switch')
opener = ur.build_opener(ur.HTTPBasicAuthHandler(mgr))
req = opener.open(url)
data = req.read()
#print(data)
data = data.split(b'</html>')[1]
#print(data)

info = data.split(b'\n')
#print(info)
number = list(map(lambda x: x.count(b' '), info))
# print(len(number), number)
number = number[1:]    # see at web page 

s = b''
for i in number:
    s += struct.pack('=B', i)
#print(s)
data = bz2.decompress(s)
with open("output.rtf", 'wb') as r:
        r.write(data)