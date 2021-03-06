#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/hex/copper.html
<!-- or maybe white.gif would be more bright-->
'''
from PIL import Image, ImageSequence, ImageDraw
import urllib.request as ur, io
url = "http://www.pythonchallenge.com/pc/hex/white.gif"
mgr = ur.HTTPPasswordMgrWithDefaultRealm()
mgr.add_password(None, url, 'butter', 'fly')
opener = ur.build_opener(ur.HTTPBasicAuthHandler(mgr))
data = opener.open(url).read()
im = Image.open(io.BytesIO(data))

# im = Image.open("0022white.gif")
#print(im.size)

new = Image.new('RGB', (400, 100), "black")
ned = ImageDraw.Draw(new)  
x, y = -40, 20    # -> (20, 20)
for s in ImageSequence.Iterator(im):
    left, upper, right, lower = im.getbbox()
    dx = (left - 100)
    dy = (upper - 100)
    x += dx
    y += dy
    if dx == dy == 0:
        x += 60
    ned.point((x,y))
    #print(x, y)
  
new.show()   