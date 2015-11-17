#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
http://www.pythonchallenge.com/pc/return/uzi.html
'''
from datetime import date
#for i in range(1016, 2016, 20):
    #d = date(i, 1, 27)
    #if d.weekday() == 1:    #Tuesday
        #print(d)

print([i for i in range(1016, 2016, 20) if date(i, 1, 27).weekday() == 1])