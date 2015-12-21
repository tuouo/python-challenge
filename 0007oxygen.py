#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/def/oxygen.html
'''	
from PIL import Image
im = Image.open("0007oxygen.png")
#print(im.format, im.size, im.mode, im.info)
#print(im.getpixel((0, 0)))

w, h = im.size
#for i in range(h):
    #for j in range(13):
        #r, g, b, a = im.getpixel((j, i))
        #if r == g and r == b:
           #print('%s\t%s\t%s' % (i , j ,r))

info = [im.getpixel((i, h // 2))[0] for i in range(0, w, 7)]	# 47 -- 95
print(info)
info = ''.join(map(chr, info))
print(info)

import re
end = re.findall("\d+", info)
print(end)
end = ''.join(map(chr, map(int, end)))
print(end)

# from PIL import Image
# import urllib.request as ur, io, re
# url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
# im = Image.open(io.BytesIO(ur.urlopen(url).read()))
# w, h = im.size

# info = [im.getpixel((i, h // 2))[0] for i in range(0, w, 7)]    # 47 -- 95
# info = ''.join(map(chr, info))
# print(info)

# end = re.findall("\d+", info)
# print(end)
# end = ''.join(map(chr, map(int, end)))
# print(end)