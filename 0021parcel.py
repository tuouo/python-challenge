#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Now for the level:

* We used to play this game when we were kids
* When I had no idea what to do, I looked backwards.
'''
import bz2, zlib
result = []
with open("0020invader/package.pack", "rb") as pack:
    data = pack.read()
    while True:
        if data.startswith(b"x\x9c"):
            data = zlib.decompress(data)
            result.append(" ")
        elif data.startswith(b"BZ"):
            data = bz2.decompress(data)
            result.append("*")
        elif data.endswith(b"ZB"):
            data = data[::-1]
            result.append("\n")
        elif data.endswith(b"\x9cx"):
            data = data[::-1]
            result.append("\n")
        else:
            break
print(data)
print(''.join(result))