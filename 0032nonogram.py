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
    # check cross, if len less than all tipnumber
    return newLine, lineOK


def getMostLeftLine(lineLen, tipNums, line):
    pos, num, newLine = 0, 0, [virgin] * lineLen
    while num < len(tipNums):
        blockLen = tipNums[num]
        nextpos = findNextBlockStart(lineLen, blockLen, line, pos)
        newLine, numNew, nextpos = checkBefore(tipNums, num, line, newLine, nextpos)
        # if num change
        if numNew == num:
            for i in range(nextpos, nextpos + blockLen + 1):
                newLine[i] = blcak
        else:




def checkBefore(tipNums, num, line, newLine, nextpos):
    '''
    check pre suit block need move right or not
    '''
    if num == 0:               # if pre still have black, means wrong table
        return newLine, num, nextpos
    checkpos, preBlockEnd = nextpos - 1, nextpos - 1
    while newLine[preBlockEnd] != black : # find pre block in newLine, must be there
        preBlockEnd -= 1
    while checkpos > preBlockEnd:
        while line[checkpos] != black:    # find pre block in line
            checkpos -= 1
        if checkpos == preBlockEnd:       # means every block covered, so OK            
            return newLine, num, nextpos            
        else:                  
            num -= 1
            preBlockLen, skippos = tipNums[num], checkpos - preBlockLen + 1
            for pos in range(checkpos - preBlockLen, checkpos):
                if line[pos] != black:
                    skippos = pos
                    break
                elif line[pos + preBlockLen + 1] == cross: # and will not suit pre cell cross
                    for i in range(preBlockEnd - preBlockLen + 1, preBlockEnd + 1):                            
                        newLine[i] = [virgin]              # remove pre block in new line
                    return checkBefore(tipNums, num - 1, line, newLine, pos + preBlockLen + 1)
            for i in range(preBlockEnd - preBlockLen + 1, skippos):                            
                newLine[i] = [virgin]                      # remove (pre block -- skippos)
            return checkBefore(tipNums, num, line, newLine, skippos)



    






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
                while line[pos + blockLen] == black or line[pos - 1] == black:          
                    pos += 1                      # black block's next shouldn't be black  
                    while line[pos + blockLen] == black :
                        pos += 1
                    if line[pos - 1] == black:    # black block's pre shouldn't be black 
                        if line[pos + blockLen] == cross:
                            pos += (blockLen + 1) # suit block len not suit black
                            break
                        else:
                            pos += 1              # continue check next is black
                find = True
            except Exception, e:                  # black block can reach end
                if (pos + blockLen - 1) == lineLen and line[pos - 1] != black:
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