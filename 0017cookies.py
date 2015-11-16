#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
http://www.pythonchallenge.com/pc/return/romance.html

cookies: Content:	you+should+have+followed+busynothing...

http://www.pythonchallenge.com/pc/return/violin.html
http://www.pythonchallenge.com/pc/stuff/violin.php
'''
#import urllib.request as ur, urllib.parse as up, re, bz2
#url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
#reNext = re.compile(r"(?<=and the next busynothing is )\d+")
#reInfo = re.compile(r'(info=.{0,4};)')
#info, number = [], ['12345']
#
##for i in range(400):
    ##try:
        ##data = ur.urlopen(url + number[0]).read()
        ##print(i, data)
        ##number = re.findall(r"(?<=and the next busynothing is )\d+", data.decode('utf-8'))
    ##except:
        ##print('end\t', data)
        ##break;
#for i in range(120):
    #try:
        #request = ur.urlopen(url + number[0])
        ##print(request.info())
        #print(number[0], reInfo.findall(str(request.info())))
        #info.append(reInfo.findall(str(request.info())))
        #data = request.read()
        #number = reNext.findall(data.decode('utf-8'))
    #except:
        #break;
#info = ''.join(j for i in info for j in i)
#from tools import writeData
#writeData(info)

import errorWrongCookies, bz2, urllib.request as ur, urllib.parse as up
info = errorWrongCookies.infoRight
info = up.unquote_to_bytes(info)
info = bz2.decompress(info)
print(info)
info = "the flowers are on their way"

from xmlrpc.client import ServerProxy
server = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
#print(server.system.methodHelp('phone'))
print(server.phone("Leopold"))

url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
request = ur.Request(url, headers={'Cookie': 'info=' + up.quote(info)})
last = ur.urlopen(request).read()
print(last)