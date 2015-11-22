#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/hex/ambiguity.html
'''
from PIL import Image, ImageDraw
im = Image.open("0024maze.png")
for i in range(im.size[1]):	
    #print(im.getpixel((i,0)), '', end = '')
    #print(im.getpixel((i, im.size[1] - 1)), '', end = '')
    if im.getpixel((i,0))[0] == 0:
        pos = (i, 0)
    if im.getpixel((i, im.size[0] - 1))[0] == 0:
        exit = (i, im.size[0] - 1)

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
wall = (255, 255, 255, 255)
path, all_path = [], []

while pos != exit:
    im.putpixel(pos, wall)
    flag = 0    
    for i in direction:
        try:
            next_pos = (pos[0] + i[0], pos[1] + i[1])
            if im.getpixel(next_pos) != wall:
                flag += 1
                new_pos = next_pos
        except:
            print("If here, I think we get out")
    if flag == 1:
        path.append(pos)
        pos = new_pos        
    elif flag > 1:
        all_path.append(path)
        path = [pos]
        pos = new_pos
    else:
        if path == []:
            path = all_path.pop()
            continue
        pos = path[0]
        path = []
else:
    path.append(pos)
    all_path.append(path)

im = Image.open("0024maze.png")
new = Image.new('RGBA', im.size, 'black')
data = [(im.getpixel(k)[0], new.putpixel(k, wall)) for path in all_path for k in path]
new.show()    #new.save('0024out.png')

import struct
with open("0024mazeout.zip", "wb") as out:
    for i in data[1::2]:
        out.write(struct.pack("=B", i[0]))