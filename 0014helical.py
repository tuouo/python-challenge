#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
http://www.pythonchallenge.com/pc/return/italy.html

http://www.pythonchallenge.com/pc/return/cat.html
and its name is uzi. you'll hear from him later. 
'''
from PIL import Image
source = Image.open("0014wire.png")
souData = source.load()
im = Image.new(source.mode, (100, 100))
imData = im.load()

steps = [[i, i-1, i-1, i-2] for i in range(100, 0, -2)]
direction = [(1,0), (0, 1), (-1, 0), (0, -1)]
d, sp, ip = 0, 0, (-1, 0)

for helical in steps:
    #helical = [i // 2 for i in range(200, 0, -1)]
    for section in helical:
        for s in range(section):
            ip = tuple(map(lambda x, y: x + y, ip, direction[d]))
            imData[ip] = souData[(sp, 0)]
            sp += 1
        d = (d + 1) % 4    # len(direction)
im.show()