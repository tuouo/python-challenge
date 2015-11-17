#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/return/mozart.html
'''
from PIL import Image, ImageChops

im = Image.open('0016mozart.gif')
w, h = im.size
#color = {}
#for i in range(w):
    #a = im.getpixel((i, 0))
    #if a in color:
        #color[a] += 1
    #else:
        #color[a] = 1
#for k, v in color.items():
    #if v < 10 and v > 2:
        #print('%s:%s' % (k, v))
#print(color)

magic = 195    # do not ask me how did i know 195 means the color(pink?)
for j in range(h):
    box = 0, j, w,  j + 1
    row = im.crop(box)
    #byterow = row.tostring()
    #i = byterow.index(chr(magic))    
    line = [im.getpixel((x, j)) for x in range(im.size[0])]    
    i = line.index(magic)
    row = ImageChops.offset(row, -i)
    im.paste(row, box)
im.show()