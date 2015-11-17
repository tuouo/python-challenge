#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Difference
'''

import re
reg = re.compile(r'(?P<w>\d)(?P=w)*')
#reg = re.compile(r'((?P<w>\d)(?P=w)*)')
n = '111221'
print(reg.findall(n))
n = '11112221'
print(reg.findall(n))
n = '12'
print(reg.findall(n))