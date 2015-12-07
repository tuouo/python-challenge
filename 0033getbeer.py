#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/rock/beer.html
'''
import urllib.request as ur, math
from PIL import Image
from io import BytesIO
url = "http://www.pythonchallenge.com/pc/rock/beer2.png"
mgr = ur.HTTPPasswordMgrWithDefaultRealm()
mgr.add_password(None, url, 'kohsamui', 'thailand')
opener = ur.build_opener(ur.HTTPBasicAuthHandler(mgr))
req = opener.open(url)
data = req.read()
im = Image.open(BytesIO(data))
color = im.getcolors()

sizes = []
pre = 0
for i in range(0, len(color), 2):
    pre += (color[i][0] + color[i + 1][0])
    sizes.append(int(math.sqrt(pre)))

data = im.getdata()
for i in range(32):
    newIm = Image.new('L', (sizes[31 - i], sizes[31 - i]))
    j = 6 * (32 - i) + 1
    data = [d for d in data if d < j]
    brightest = 6 * (31 - i) + 2    
    out = [0 if p < brightest else 255 for p in data ]
    newIm.putdata(out)
    newIm.show()