#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/return/balloons.html
<!-- it is more obvious that what you might think -->

http://www.pythonchallenge.com/pc/return/brightness.html
'''

import urllib.request as ur, re, gzip, io, difflib, struct
from PIL import Image
with gzip.open('0018deltas.gz', 'r') as gz:
    deltas = gz.read()
deltas = deltas.splitlines()    
left, right = [], []
for line in deltas:
    left.append(line[:53].decode('utf-8'))
    right.append(line[56:].decode('utf-8'))
# import urllib.request as ur, re, gzip, io, difflib, base64
# from PIL import Image
# url = 'http://www.pythonchallenge.com/pc/return/deltas.gz'
# mgr = ur.HTTPPasswordMgrWithDefaultRealm()
# mgr.add_password(None, url, 'huge', 'file')
# opener = ur.build_opener(ur.HTTPBasicAuthHandler(mgr))
# data = opener.open(url).read()
# left, right = [], []
# with gzip.GzipFile(fileobj = io.BytesIO(data)) as gz:
#     for line in gz:
#         left.append(line[:53].decode('utf-8'))
#         right.append(line[56:].decode('utf-8'))
result = list(difflib.ndiff(left,right))
# print(len(result))

arr = {" ": 0, "+": 1, "-":2}
png = [bytearray(), bytearray(), bytearray()]
for row in result:    
    a = row[1:].split()
    for i in range(len(a)):
        png[arr[row[0]]] += struct.pack("=B", int(a[i], 16))

for i in range(3):
    # print(png[i][:100])
    open('0018_%d.png' % i, 'wb').write(png[i])