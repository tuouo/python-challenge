#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
http://www.pythonchallenge.com/pc/return/5808.html
'''
from PIL import Image
im = Image.open('0011cave.jpg')
w, h = im.size

imgs = [Image.new(im.mode, (w // 2, h // 2)) for i in range(4)]
imgs_load = [i.load() for i in imgs]
org = im.load()

for i in range(w):
    for j in range(h):
        org_pos = (i, j)
        new_pos = (i // 2, j // 2)
        imgs_load[i % 2 + j % 2 * 2 ][new_pos] = org[org_pos]

for i in range(4):
    imgs[i].show()
#[imgs[i].save('0011%d.png' % i) for i in range(4)]