#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/def/peak.html

pronounce it

'''
import urllib.request as ur, pickle, os
from tools import writeData
url = 'http://www.pythonchallenge.com/pc/def/banner.p'
data = ur.urlopen(url).read()
lists = pickle.loads(data)
with open(os.path.join(os.getcwd(), "output.rtf"), 'w') as r:
    for i in lists:
	    r.write((''.join(map(lambda p: p[0]*p[1], i))) + '\n')