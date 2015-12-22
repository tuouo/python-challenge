#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/return/evil.html
'''

#content = open("0012evil2.gfx", 'rb').read()
#[open("0012_%d.jpg" %i, "wb").write(content[i::5]) for i in range(5)] 

with open("0012evil2.gfx", 'rb') as source:
    content = source.read()

# import urllib.request as ur
# url = "http://www.pythonchallenge.com/pc/return/evil2.gfx"
# mgr = ur.HTTPPasswordMgrWithDefaultRealm()
# mgr.add_password(None, url, 'huge', 'file')
# opener = ur.build_opener(ur.HTTPBasicAuthHandler(mgr))
# content = opener.open(url).read()


for i in range(5):
    with open("0012_%d.jpg" %i, "wb") as new:
        new.write(content[i::5])