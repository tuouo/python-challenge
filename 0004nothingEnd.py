#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
http://www.pythonchallenge.com/pc/def/linkedlist.php

<!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
end. 400 times is more than enough. -->

Your hands are getting tired and the next nothing is 
There maybe misleading numbers in the text. One example is 82683. Look only for the next nothing and the next nothing is
'''
import urllib.request as ur, re
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
number = ['12345']
number = ['8022']
#number = ['82683']
#You've been misleaded to here. Go to previous one and check.

for i in range(400):
    try:
        data = ur.urlopen(url + number[0]).read()
        print(i, data)
        #number = re.findall('[0-9]+$', data.decode('utf-8'))
        number = re.findall(r"(?<=and the next nothing is )\d+", data.decode('utf-8'))	# (?<=...)
    except:
        print('end\t', data)
        break;