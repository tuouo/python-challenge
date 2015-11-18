#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/hex/bin.html
butter
fly
'''
#import urllib.request as ur, re, wave, base64
#url = "http://www.pythonchallenge.com/pc/hex/bin.html"
#mgr = ur.HTTPPasswordMgrWithDefaultRealm()
#mgr.add_password(None, url, 'butter', 'fly')
#opener = ur.build_opener(ur.HTTPBasicAuthHandler(mgr))
#src = opener.open(url).read().decode('utf-8')
#c = re.compile(r"<!--\n(.*)\n-->", re.DOTALL)
#data = c.findall(src)[0]
#
##message = email.message_from_string(data)
##audio = message.get_payload(0).get_payload(decode = True)
##wav = wave.open(io.StringIO(audio))
##print(wav.getsampwidth())
##channels = 2
##
##fmt = ossaudiodev.AFMT_S16_BE
##channels = 2
##last = ossaudiodev.open('w')
##last.setparameters(fmt, channels, wav.getframerate())
##last.write(audio)
#c = re.compile(r"Content-transfer-encoding: base64\n\n(.*)\n--===============1295515792==--", re.DOTALL)
#data = c.findall(src)[0]
##print(data[:6], data[-6:])
#with open('0019india.wav', 'wb') as india:
    #india.write(base64.b64decode(data))
## sorry, '''- "what are you apologizing for?"'''

import wave
with wave.open('0019india.wav', 'rb') as india:
    with wave.open('0019aidni.wav', 'wb') as aidni:
        aidni.setparams(india.getparams())
        for i in range(india.getnframes()):
            aidni.writeframes(india.readframes(1)[::-1])