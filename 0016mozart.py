#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/return/mozart.html
'''
from PIL import Image, ImageChops

im = Image.open('0016mozart.gif')
w, h = im.size
color = {}
pre, con = im.getpixel((0, 0)), 0
color[pre] = [0, 1]    # deal with i == 0
for i in range(w):
    a = im.getpixel((i, 0))
    if a == pre:        
        color[a][0] += 1
        con += 1
        continue
    if a not in color:
        color[a] = [1, 1]
    if color[pre][1] < con:
        color[pre][1] = con
    con, pre = 1, a

linePoint = 0
print(color, '\n')
for k, v in color.items():
    # # if v[0] < 10 and v[0] > 2:
    if v[0] > 2:
        print('%s:%s' % (k, v))
        if v[0] == v[1]:
            print("together:", k)
            linePoint = k

# magic = 195    # do not ask me how did i know 195 means the color(pink?)
magic = linePoint    #which color appear together
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


