#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

def nonogram(numbers):
    HorLen, VerLen  = numbers[0][0], numbers[0][1]
    Horizontal = numbers[1 : 1 + HorLen]
    Vertical = numbers[1 + HorLen :]    
    HorOK = [False] * HorLen    # mark if horizontal line mark ok or not
    VerOK = [False] * VerLen    # mark if vertical line mark ok or not 
    allOK = reduce(lambda a, b: a and b, HorOK + VerOK)

    virgin, cross, black = 0, 1, 2    # means not sure, not, is black
    count, limit = 0, HorLen * VerLen # incase noend loop
    table = [None] * HorLen           # Init
    for i in range(HorLen):
        table[i] = [virgin] * VerLen

    try:
        while not allOK and count < limit:
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
            count += 1
    except Exception, e:
        printNo2g(table)
        raise e

    printNo2g(table)
    return 


def scanLine(lineLen, tipNums, line):
    mostLeft  = getMostLeftLine(lineLen, tipNums, line)  # all black to left as possible
    mostRight = getMostRightLine(lineLen, tipNums, line) # all black to right as possible
    lineOK    = checkLeftRight(mostLeft, mostRight)      # if blacks are same, OK
    newLine   = mixLeftRight(mostLeft, mostRight)        # get cell suit both left & right
    return newLine, lineOK


def getMostLeftLine(lineLen, tipNums, line):
    pos, num, newLine = 0, 0, []
    while num < len(tipNums):
        blockLen = tipNums[num]
        nextpos = findNextBlockStart(lineLen, blockLen, line, pos)
        newLine.append(line[pos, nextpos])
        newLine.append([blcak] * blockLen)
        newLine.append(line[nextpos + blockLen + 1])
        newLine, num, pos = checkBefore(tipNums, num, line, newLine, nextpos)



def checkBefore(tipNums, num, line, newLine, nextpos):
    '''
    check pre suit block need move right or not
    '''
    if num == 0:               # if nextpos still have black, means wrong table
        return newLine, num + 1, nextpos
    checkpos, num = nextpos - 1, num - 1
    preEnd = 0
    while checkpos >= 0:
        while line[checkpos] != black and checkpos >= 0: # find pre block
            checkpos -= 1
        if newLine[checkpos] == black or checkpos < 0:
            num += 2
            break              # means every block covered, so OK
        else:                  # means before this block, must have no-black in line
            checkSta = checkpos - 1
            while line[checkSta] == black:
                checkSta -= 1  # see pre, checkSta won't be negative
            blockLen = checkpos - checkSta



    return newLine, num, nextpos






def findNextBlockStart(lineLen, blockLen, line, start):
    pos, find = start, False
    while not find:        
        newpos = pos
        while(line[pos] == cross):      # suit block not start with cross
            pos += 1
        for i in range(1, blockLen):
            if line[pos + i] == cross:  # suit block len short than black
                newpos += (i + 1)       # check current cell's next
                break
        if pos == newpos:
            try: 
                while line[pos + blockLen] == blcak or line[pos - 1] == blcak:          
                    pos += 1                      # black block's next shouldn't be black  
                    while line[pos + blockLen] == blcak :
                        pos += 1
                    if line[pos - 1] == blcak:    # black block's pre shouldn't be black 
                        if line[pos + blockLen] == cross:
                            pos += (blockLen + 1) # suit block len not suit black
                            break
                        else:
                            pos += 1              # continue check next is blcak
                find = True
            except Exception, e:                  # black block can reach end
                if (pos + blockLen - 1) == lineLen and line[pos - 1] != blcak:
                    find = True
                else:
                    raise e
    return pos


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