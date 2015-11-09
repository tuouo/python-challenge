#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
http://www.pythonchallenge.com/pc/def/map.html

everybody thinks twice before solving this.

g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. 
 

General tips: 

Use the hints. They are helpful, most of the times. 
Investigate the data given to you. 
Avoid looking for spoilers. 
Forums: Python Challenge Forums 

'''


import string
alphablet = string.ascii_letters	# ascii_lowercase ascii_uppercase
#print(alphablet)

riddle = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#result = []
#alpLen = len(alphablet)
#for word in riddle:
    #index = alphablet.find(word)
    #if index == -1:
        #result.append(word)
    #else:
        #result.append(alphablet[index + 2 - alpLen]) 
#result = ''.join(result)
#print(result)
#print(result.title())

tranAlph = alphablet[2:] + alphablet[:2]
mapAlph = str.maketrans(alphablet, tranAlph)
result = riddle.translate(mapAlph)
print(result)

from tools import writeData
writeData(result)