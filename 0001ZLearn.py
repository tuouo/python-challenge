#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import string
a, b, c = string.punctuation, string.printable, string.whitespace 
print("string.punctuation:", len(a), a)
print("string.printable:", len(b), b)
print("string.whitespace:", len(c), c)
print('end.')

# format