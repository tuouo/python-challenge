#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
http://www.pythonchallenge.com/pc/return/disproportional.html

phone that evil 
'''
from xmlrpc.client import ServerProxy
server = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(server)
#print(server.system.listMethods())
#print(server.system.methodHelp('phone'))
#print(server.phone("evil"))
print(server.phone("Bert"))