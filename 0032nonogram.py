#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

def nonogram(numbers):
    HorLen，VerLen  = numbers[0][0]，numbers[0][1]
    Horizontal = numbers[1 : 1 + HorLen]
    Vertical = numbers[1 + HorLen :]    
    HorOK = [False] * HorLen    # mark if horizontal line mark ok or not
    VerOK = [False] * VerLen    # mark if vertical line mark ok or not 
    allOK = reduce(lambda a, b: a and b, HorOK + VerOK)

    virgin, cross, black = 0, 1, 2    # means not sure, not, is black 
    table = [None] * HorLen             # Init
    for i in range(HorLen):
        table[i] = [virgin] * VerLen

    while not allOK:
        for i in range(HorLen):
            if not HorOK[i]:
                table[i], HorOK[i] = scanLine(VerLen, Horizontal[i], table[i])
        for i in range(VerLen):
            if not VerOK[i]:
                line = []     # transfer Vertical to Horizontal for multiplex method scanLine
                for n in range(HorLen):
                    line.append(table[n][i])
                newLine, VerOK[i] = scanLine(HorLen, Horizontal[i], line)
                for n in range(HorLen):
                    table[n][i] = newLine[n]
        allOK = reduce(lambda a, b: a and b, HorOK + VerOK)

    printNo2g(table)
    return 


def scanLine(lineLen, tipNums, line):
	lineOK = False
    for i in range(lineLen):
        while(line[i] == cross):
            j++        
        
                

def printNo2g(table):
    for line in table:
        for cell in line:
            if cell == 2:
                print("*", end = '')
            elif cell = 1:
                print(" ", end = '')
            else:
                print("?", end = '')
        print()