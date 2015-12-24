#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/ring/yankeedoodle.html
http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv
'''
import re, struct
from PIL import Image
with open("0030yankeedoodle.csv", "r") as csv:
    data = csv.read()
# print(type(data), len(data))
numstr = re.findall("(0.\d*)", data)
# #print(len(numstr), numstr[-10:])
# numbers = list(map(lambda i: int(256 * float(i)), numstr))
# #print(len(numbers), numbers[-10:])
# im = Image.new('L', (53, 139))
# im.putdata(numbers)
# im = im.transpose(Image.ROTATE_90)
# im = im.transpose(Image.FLIP_TOP_BOTTOM)
# im.show()

# ss = [int(numstr[i][5] + numstr[i][5] + numstr[i][6]) for i in range(0, len(numstr) - 2, 1)]
# print(ss)
s = ''.join([chr(int(numstr[i][5] + numstr[i + 1][5] + numstr[i + 2][6])) for i in range(0, len(numstr) - 2, 3)])
print(s)