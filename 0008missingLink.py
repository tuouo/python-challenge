#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/def/integrity.html

Where is the missing link?
'''	
# un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
# import bz2
# print("name:", bz2.decompress(un.encode('latin1')))
# print("password:", bz2.decompress(pw.encode('latin1')))


un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

# import urllib.request as ur, re
# rega = re.compile(r"(?<=un: ')[ \S]+(?='\n)")
# regb = re.compile(r"(?<=pw: ')[ \S]+(?='\n)")
# url = "http://www.pythonchallenge.com/pc/def/integrity.html"
# data = ur.urlopen(url).read().decode('utf-8')
# a = rega.findall(data)
# b = regb.findall(data)
# un = a[0].encode('latin1').decode('unicode_escape').encode('latin1')
# pw = b[0].encode('latin1').decode('unicode_escape').encode('latin1')

import bz2
print("name:", bz2.decompress(un))
print("password:", bz2.decompress(pw))