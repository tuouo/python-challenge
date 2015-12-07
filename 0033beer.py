#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/rock/beer.html
'''
import urllib.request as ur, math
from PIL import Image
url = "http://www.pythonchallenge.com/pc/rock/beer2.png"
mgr = ur.HTTPPasswordMgrWithDefaultRealm()
mgr.add_password(None, url, 'kohsamui', 'thailand')
opener = ur.build_opener(ur.HTTPBasicAuthHandler(mgr))
req = opener.open(url)
data = req.read()
# with open("0033beer.png", 'wb') as r:
#     r.write(data)
im = Image.open("0033beer.png")
color = im.getcolors()

sizes = []
pre = 0
for i in range(0, len(color), 2):
    pre += (color[i][0] + color[i + 1][0])
    sizes.append(int(math.sqrt(pre)))
# print(sizes)

data = im.getdata()
for i in range(32):
    newIm = Image.new('L', (sizes[31 - i], sizes[31 - i]))
    j = 6 * (32 - i) + 1
    data = [d for d in data if d < j]
    # print(sizes[31 - i], int(math.sqrt(len(data))))

    brightest = 6 * (31 - i) + 2    
    out = [0 if p < brightest else 255 for p in data ]
    newIm.putdata(out)
    # newIm.show()
    newIm.save("0033_%s.png" % i)