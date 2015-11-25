#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/ring/grandpa.html
kohsamui：thailand
http://www.pythonchallenge.com/pc/rock/grandpa.html
'''
def mendelbrot(left = 0.34, top = 0.57, width = 0.036, height = 0.027, iterations = 128, size = (640,480)):
    dx, dy = width / size[0], height / size[1]
    for y in range(size[1] - 1, -1, -1):
        for x in range(size[0]):
            c = complex(left + x * dx, top + y * dy)
            z = 0 + 0j
            for i in range(iterations):
                z = z * z + c
                if abs(z) > 2:
                    break;
            yield i
    
from PIL import Image
im = Image.open("0031mandelbrot.gif")
new = im.copy()
new.putdata(list(mendelbr0t())[:640 * 480])
#new.show()

diff = [(b - a) for a, b in zip(im.getdata(), new.getdata()) if a != b]
#print(len(diff), diff[:100])
#print(diff)

# result = Image.new("L", (23, 73))
# result.putdata([i for i in diff])
# result.show()
result = Image.new("1", (23, 73))
result.putdata([i < 16 for i in diff])
result.show()