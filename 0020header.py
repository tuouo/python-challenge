#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/hex/idiot.html
http://www.pythonchallenge.com/pc/hex/idiot2.html
'''
import urllib.request as ur, re
url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
mgr = ur.HTTPPasswordMgrWithDefaultRealm()
mgr.add_password(None, url, 'butter', 'fly')
opener = ur.build_opener(ur.HTTPBasicAuthHandler(mgr))
req = opener.open(url)
#print(req.info())
reg = re.compile(r'bytes (\d+)-(\d+)/(\d+)')
start, end, length = [int(i) for i in re.findall(reg, req.info()['Content-Range'])[0]]

#with open('output.rtf', 'wb') as mess:
    #while end:
        #print(req.info()['Content-Range'])
        #mess.write(req.info()['Content-Range'].encode('utf-8'))
        #opener.addheaders = [('Range', 'bytes=%d-' % (end + 1 ))]
        #try:
            #req = opener.open(url)
            #info = req.read()
            #mess.write(info)
            #print(info)
            #if end == length:
                #break;
            #start, end, length = [int(i) for i in re.findall(reg, req.info()['Content-Range'])[0]]           
        #except:
            #end = length
            #continue

#end = length
#with open('output.rtf', 'wb') as mess:
    #while end:
        #mess.write(req.info()['Content-Range'].encode('utf-8'))
        #opener.addheaders = [('Range', 'bytes=%d-' % (end - 1 ))]
        #try:
            #req = opener.open(url)
            #mess.write(req.read())
            #if end == start:
                #break;
            #startt, end, length = [int(i) for i in re.findall(reg, req.info()['Content-Range'])[0]]
            #end = startt        
        #except:
            #end = start
            #continue

#end = 1152983631
#opener.addheaders = [('Range', 'bytes=%d-' % end)]
#req = opener.open(url)
#print(req.info())
##print(req.read())
#print(req.read()[:10])

# PK
with open('0020invader.zip', 'wb') as mess:
    end = 1152983631
    opener.addheaders = [('Range', 'bytes=%d-' % end)]
    req = opener.open(url)
    data = req.read()
    mess.write(data)