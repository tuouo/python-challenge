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
    except Exception as e:
        printNo2g(table)
        raise e

    printNo2g(table)
    return table


def scanLine(lineLen, tipNums, line):
    offLeft = getMostLeftLine(lineLen, tipNums, line)       # all black to left as possible
    offRigh = getMostRightLine(lineLen, tipNums, line)      # all black to right as possible  
    lineOK  = offLeft == offRigh    
    newLine = mixLeftRight(line, tipNums, offLeft, offRigh) # get cell suit both left & right
    if not lineOK:
        newLine = checkCross(newLine, tipNums, offLeft, offRigh) 
    return newLine, lineOK


def checkCross(newLine, tipNums, mostLeft, mostRight):
    '''
    check cross: if virgin block'len less than black block which may appear, must be cross
    '''
    off, blockLen = mostLeft[0][1] + 1, 1 
    while off < mostRight[-1][1]:
        if newLine[off] == virgin:
            while newLine[off + blockLen] == virgin:
                blockLen += 1
            if newLine[off - 1] != cross or newLine[off + blockLen] != cross:
                off += blockLen
            else:
                for i in range(len(tipNums)):
                    if off > mostLeft[i][1]:
                        if off < mostRight[i][0] and blockLen < tipNums[i]:
                            for n in range(blockLen):
                                newLine[off + n] = cross
                    else:
                        break
    return newLine


def mixLeftRight(line, mostLeft, mostRight):
    tipNum, lineLen = len(mostLeft), len(lineLen)
    for n in range(mostLeft[0][0]):
        line[n] = cross
    for i in range(tipNum - 1):
        for n in range(mostRight[i][0], mostLeft[i][1] + 1):
            line[i] = black
        for n in range(mostRight[i][1] + 1, mostLeft[i + 1][0]):
            line[i] = cross    
    for n in range(mostRight[-1][0], mostLeft[-1][1] + 1):
        line[n] = black
    for n in range(mostRight[-1][1] + 1, lineLen):
        line[i] = cross    
    return line    


def getMostRightLine(lineLen, tipNums, line):
    return getMostLeftLine(lineLen, tipNums, line[::-1])[::-1]


def getMostLeftLine(lineLen, tipNums, line):
    pos, num, offLeft, newLine = 0, 0, [(0, 0)] * len(tipNums), [virgin] * lineLen
    while num < len(tipNums):
        nextpos = findNextBlockStart(lineLen, tipNums[num], line, pos)
        newLine, numNew, nextpos = checkBefore(tipNums, num, line, newLine, nextpos)
        blockLen = tipNums[numNew]
        for i in range(nextpos, nextpos + blockLen):  
            newLine[i] = blcak
        offLeft[num] = (nextpos, nextpos + blockLen - 1) # add each block's start&end
    return offLeft


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
            except Exception as e:                  # black block can reach end
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
            elif cell == 1:
                print(" ", end = '')
            else:
                print("?", end = '')
        print()




if __name__ == '__main__':

    import re
    with open("output.rtf", 'r') as r:
        data = r.read()
    
    numberStr = data.split('\n')
    numbers = []
    reg = re.compile(r'(\d+)')
    for i in numberStr:
        if reg.match(i):
            numbers.append(list(map(int, reg.findall(i))))
    
    nonogram(numbers)