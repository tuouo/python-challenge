#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/hex/bonus.html
'''
import string
alphablet = string.ascii_lowercase
riddle = 'va gur snpr bs jung'

for i in range(26):
    tranAlph = alphablet[i:] + alphablet[:i]
    mapAlph = str.maketrans(alphablet, tranAlph)
    print(riddle.translate(mapAlph), i)


import this