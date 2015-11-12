#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
PIL Image ImageDraw Draw line 

group by two, treat as dots coordinate. connect one bye one
'''	

number = [1, 100, 250, 30, 200, 200]

from PIL import Image, ImageDraw
im = Image.new('RGB', (300, 300))
draw = ImageDraw.Draw(im)
draw.line(number)
del draw
im.show()
