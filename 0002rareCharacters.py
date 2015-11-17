#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/def/ocr.html

recognize the characters. maybe they are in the book, 
but MAYBE they are in the page source.

 General tips: •Use the hints. They are helpful, most of the times.
•Investigate the data given to you.
•Avoid looking for spoilers.

 Forums: Python Challenge Forums, read before you post. 
 IRC: irc.freenode.net #pythonchallenge 

 To see the solutions to the previous level, replace pc with pcc, i.e. go to: http://www.pythonchallenge.com/pcc/def/ocr.html
'''

import os
from html.parser import HTMLParser
class exampleHTMLParser(HTMLParser):
    def __init__(self):
        super(exampleHTMLParser, self).__init__()
        self.result = {}
        #self.find = 'yutileaq'
        self.alph = ''

    def handle_comment(self, data):
        # len = 41:find rare characters in the mess below:
        if len(data) != 41:
            self.result = {}
            for i in data:
                if i in self.result:
                    self.result[i] += 1
                else:
                    self.result[i] = 1
                    self.alph += i
        return self.result, self.alph
        
parser = exampleHTMLParser()
with open (os.path.join(os.getcwd(), '0002ocr.html'), 'r') as html:
    parser.feed(html.read())

result, alph = parser.result, parser.alph
print(result)
print(alph)
name = []
for i in alph:
    if result[i] == 1:
        print(i, end = '')
        name.append(i)
from tools import writeData
writeData(''.join(name))