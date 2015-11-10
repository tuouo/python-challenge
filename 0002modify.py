#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
result = {}
alph = ''
with open (os.path.join(os.getcwd(), '0002ocrModify.html'), 'r') as html:
    for line in html:
        for letter in range(len(line)):
            if line[letter] in result:
                    result[line[letter]] += 1
            else:
                result[line[letter]] = 1
                alph += line[letter]
print(result)
for i in alph:
    if result[i] == 1:
        print(i, end = '')