#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/hex/lake.html
'''
from PIL import Image
from io import BytesIO
import urllib.request as ur, wave
im = Image.new('RGB', (300, 300))
urlBase = "http://www.pythonchallenge.com/pc/hex/lake%d.wav"
mgr = ur.HTTPPasswordMgrWithDefaultRealm()

# for i in range(25):
#     pos = ((i % 5) * 60, (i // 5) * 60)
#     url = urlBase % (i + 1)	
#     mgr.add_password(None, url, 'butter', 'fly')
#     opener = ur.build_opener(ur.HTTPBasicAuthHandler(mgr))
#     req = opener.open(url)
#     # most part of the picture is ok. (cause 10844 VS 10800)
#     im.paste(Image.fromstring('RGB', (60,60), req.read()), pos)
# im.show()

for i in range(25):
    pos = ((i % 5) * 60, (i // 5) * 60)
    url = urlBase % (i + 1)	
    mgr.add_password(None, url, 'butter', 'fly')
    opener = ur.build_opener(ur.HTTPBasicAuthHandler(mgr))
    req = opener.open(url)
    data = wave.open(BytesIO(req.read()))
    patch = Image.frombytes('RGB', (60, 60), data.readframes(data.getnframes()))
    im.paste(patch, pos)
im.show()

