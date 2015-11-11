#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
http://www.pythonchallenge.com/pc/def/channel.html
'''
#import os, re
#filePath = os.path.join(os.getcwd(), '0006channel')
#name = ['90052']
#reg = re.compile(r"(?<=Next nothing is )\d+")
#for i in range(1000):
    #try:
        #with open(os.path.join(filePath, name[0] + '.txt'), 'r') as f:
            #data = f.read()
            #print(i, data)
            #name = reg.findall(data)
    #except:
        #print('end\t', data)
        #break;

#import zipfile, re, os
#filePath = os.path.join(os.getcwd(), '0006channel.zip')
#reg = re.compile(r"(?<=Next nothing is )\d+")
#name = ['90052']
#info = ''
#with zipfile.ZipFile(os.path.join(filePath), 'r') as zf:
    #zipLen = len(zf.namelist())    
    #for i in range(zipLen):
        #try:
            #info += zf.getinfo(name[0] + '.txt').comment.decode('utf-8')            
            #data = zf.read(name[0] + '.txt')
            #name = reg.findall(data.decode('utf-8'))
        #except:
            #break;
#print(info)

import urllib.request as ur, zipfile, io, re
url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
reg = re.compile(r"(?<=Next nothing is )\d+")
name = ['90052']
info = ''
with zipfile.ZipFile(io.BytesIO(ur.urlopen(url).read()), 'r') as zf:
    zipLen = len(zf.namelist())    
    for i in range(zipLen):
        try:
            info += zf.getinfo(name[0] + '.txt').comment.decode('utf-8')            
            data = zf.read(name[0] + '.txt')
            name = reg.findall(data.decode('utf-8'))
        except:
            print("i:", i)
            break;
print(info)