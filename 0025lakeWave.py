#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/hex/lake.html
'''
#import urllib.request as ur, re
#urlBase = "http://www.pythonchallenge.com/pc/hex/lake%d.wav"
#mgr = ur.HTTPPasswordMgrWithDefaultRealm()
#for i in range(1, 26):
    #url = urlBase % i
    #mgr.add_password(None, url, 'butter', 'fly')
    #opener = ur.build_opener(ur.HTTPBasicAuthHandler(mgr))
    #req = opener.open(url)
    #with open('0025lake%d.wav' % i, 'wb') as wav:
        #wav.write(req.read())

#url = "http://www.pythonchallenge.com/pc/hex/lake1.wav"
#mgr = ur.HTTPPasswordMgrWithDefaultRealm()
#mgr.add_password(None, url, 'butter', 'fly')
#opener = ur.build_opener(ur.HTTPBasicAuthHandler(mgr))
#req = opener.open(url)
#wav = req.read()
#print(wav[:100])
#print(len(wav))

#import wave
#from PIL import Image
#info = wave.open('0025lake1.wav', 'rb')
##print(len(info.readframes(info.getnframes())))
#im = Image.new('RGB', (500, 500))
#im.paste(Image.fromstring('RGB', (60,60), (info.readframes(info.getnframes()))), (0, 0))
#im.show()

from PIL import Image
import wave
im = Image.new('RGB', (300, 300))
for i in range(25):
    pos = ((i % 5) * 60, (i // 5) * 60)
    info = wave.open('0025lake%d.wav' % (i + 1), 'rb')
    im.paste(Image.fromstring('RGB', (60,60), (info.readframes(info.getnframes()))), pos)
im.show()