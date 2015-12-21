#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/def/equality.html

One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
'''

import os, re
reg = re.compile('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]')
reg = re.compile('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]')
latters = ''
with open (os.path.join(os.getcwd(), '0003re.html'), 'r') as html:
    for line in html:
        a = reg.findall(line)
        if a:
            for l in a:
                latters += l[4]
            #print(a)
print(latters)

from tools import writeData
writeData(latters)

#import urllib.request as ur, re
#reg = re.compile('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]')
#url = 'http://www.pythonchallenge.com/pc/def/equality.html'
#data = ur.urlopen(url).read().decode('utf-8')
#a = reg.findall(data)
#latters = ''
#for i in a:
    #latters += i[4]
##print(a)
#print(latters)