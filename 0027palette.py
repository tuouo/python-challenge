#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/hex/decent.html

keyword different between Python 2.X and Python 3.X
'''
from PIL import Image
import struct, bz2, keyword
im = Image.open("0027zigzag.gif")
#print(im)    # imgae mode=P
data = im.tobytes()
#palette = im.palette.getdata()
#print(type(palette), len(palette),len(palette[1]))
palette = im.palette.getdata()[1][::3]    # RGB, same, get one
Karr = bytearray()
for i in range(0, 256):
    Karr += struct.pack("=B", i)
trans = bytearray.maketrans(Karr, palette)
datatran = data.translate(trans)
# print(len(datatran), datatran[:100])
# print(len(data), data[:100])
deltas = filter(lambda p : p[0] != p[1], zip(data[1:], datatran[:-1]))

old, new = b'', b''
for i in deltas:
    old += struct.pack("=B", i[0])
    new += struct.pack("=B", i[1])
#print(old[:100])    #BZh91
#print(new[:100])
# texts = bz2.BZ2Decompressor().decompress(old).decode().split("")
textold = bz2.decompress(old).split(b' ')
#print(textold)

img = Image.new('1', im.size, 0)
img.putdata([p[0] == p[1] for p in zip(data[1:], datatran[:-1])])
img.show()

with open("output.rtf", 'w') as r:
    for i in set(textold):
        if not keyword.iskeyword(i.decode('utf-8')):
            r.write(i.decode('utf-8') + '\n')

#switch
#exec  #not keyword in python 3.X
#print #not keyword in python 3.X
#repeat
#../ring/bell.html
