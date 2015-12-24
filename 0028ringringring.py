#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/ring/bell.html
repeat
switch
'''
from PIL import Image
im = Image.open("0028bell.png")
#print(im)
r, g, b = im.split()
#r.show()
#g.show()    #ring ring ring
#b.show()
data = list(g.getdata())
#print(data)

outstand = [abs(data[i] - data[i + 1]) for i in range(0, len(data), 2) if abs(data[i] - data[i + 1]) != 42]
# print(outstand)
s = []
for i in outstand:
    s.append(chr(i))
#print(''.join(s))
import tools
tools.writeData(''.join(s))