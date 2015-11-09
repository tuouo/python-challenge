#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

def writeData(data, currentFile = "output.rtf"):
    with open(os.path.join(os.getcwd(), currentFile), 'w') as r:
        r.write(data)
