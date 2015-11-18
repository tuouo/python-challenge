#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/return/balloons.html
<!-- it is more obvious that what you might think -->

http://www.pythonchallenge.com/pc/return/brightness.html
'''
import urllib.request as ur, re, gzip, io, difflib, base64
from PIL import Image
url = 'http://www.pythonchallenge.com/pc/return/deltas.gz'

mgr = ur.HTTPPasswordMgrWithDefaultRealm()
mgr.add_password(None, url, 'huge', 'file')
opener = ur.build_opener(ur.HTTPBasicAuthHandler(mgr))
data = opener.open(url).read()
left, right = [], []
with gzip.GzipFile(fileobj = io.BytesIO(data)) as gz:
    for line in gz:
        left.append(line[:53].decode('utf-8'))
        right.append(line[56:].decode('utf-8'))
result = list(difflib.ndiff(left,right))
print("List ok.")
png = ['', '', '']
for row in result:
    byte = [chr(int(byte, 16)) for byte in row[2:].split()]
    if row[0] == '-':
        png[0] += ''.join(byte)
    elif row[0] == '+':
        png[1] += ''.join(byte)
    elif row[0] == ' ':
        png[2] += ''.join(byte)
print("Prepare to Image.")
for i in range(3):
    mes = base64.b64decode(png[i])
    open('0018_%d.png' % i, 'wb').write(mes)

#import urllib.request as ur, re, gzip, io, difflib
#from PIL import Image
#with gzip.open('0018deltas.gz', 'r') as gz:
    #deltas = gz.read()
#deltas = deltas.splitlines()    
#left, right = [], []
#for line in deltas:
    #left.append(line[:53].decode('utf-8'))
    #right.append(line[56:].decode('utf-8'))
#result = list(difflib.ndiff(left,right))
#print(len(result))
#
#png = ['', '', '']
#for row in result:
    #byte = [chr(int(byte, 16)) for byte in row[2:].split()]
    #if row[0] == '-':
        #png[0] += ''.join(byte)
    #elif row[0] == '+':
        #png[1] += ''.join(byte)
    #elif row[0] == ' ':
        #png[2] += ''.join(byte)
#
#for i in range(3):
    #open('0018_%d.png' % i, 'wb').write(png[i])