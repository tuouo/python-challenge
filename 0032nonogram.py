#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
'''
The implement of game 'nonogram'.
input data:
# Dimensions (len:2, Horizontal len & Vertical len)
# Horizontal (tipnumbers per line, Horizontal's in total)
# Vertical (tipnumbers per line, Horizontal's in total)
# #     example:
# # Dimensions
# 9 9
# # Horizontal
# 2 1 2
# 1 3 1
# 5
# 7
# 9
# 3
# 2 3 2
# 2 3 2
# 2 3 2
# # Vertical
# 2 1 3
# 1 2 3
# 3
# 8
# 9
# 8
# 3
# 1 2 3
# 2 1 3

virgin, cross, black = 0, 1, 2    # means not sure, not, is black for each cell
'''

import logging; logging.basicConfig(level = logging.INFO, filename = '0032.log', filemode = 'w') # CRITICAL INFO
virgin, cross, black = 0, 1, 2    # means not sure, not, is black

def nonogram(numbers):
    logging.info("Let's beginnig nonogram")
    global virgin, cross, black
    HorLen, VerLen  = numbers[0][0], numbers[0][1]
    Horizontal = numbers[1 : 1 + HorLen]
    Vertical = numbers[1 + HorLen :]    
    HorOK = [False] * HorLen    # mark if horizontal line mark ok or not
    VerOK = [False] * VerLen    # mark if vertical line mark ok or not 
    allOK = reduce(lambda a, b: a and b, HorOK + VerOK)

    count, limit = 0, HorLen * VerLen # incase noend loop
    table = [None] * HorLen           # Init
    for i in range(HorLen):
        table[i] = [virgin] * VerLen

    try:
        while not allOK and count < limit:
            for i in range(HorLen):
                if not HorOK[i]:
                    logging.info("scanLine Horizontal line %s: %s\n%s" % (i, Horizontal[i], table[i]))
                    table[i], HorOK[i] = scanLine(VerLen, Horizontal[i], table[i])
            for i in table:
                logging.info("%s %s" % (i, table.index(i)))
            printNo2g(table)
            for i in range(VerLen):
                if not VerOK[i]:
                    line = []     # transfer Vertical to Horizontal for multiplex method scanLine
                    for n in range(HorLen):
                        line.append(table[n][i])
                    logging.info("scanLine Vertical line %s: %s\n%s" % (i, Vertical[i], line))
                    newLine, VerOK[i] = scanLine(HorLen, Vertical[i], line)
                    for n in range(HorLen):
                        table[n][i] = newLine[n]
            for i in table:
                logging.info("%s %s" % (i, table.index(i)))
            printNo2g(table)
            allOK = reduce(lambda a, b: a and b, HorOK + VerOK)
            count += 1
    except Exception as e:
        printNo2g(table)
        raise e

    printNo2g(table)
    return table


def scanLine(lineLen, tipNums, line):
    logging.info("----MostLeft")
    offLeft = getMostLeftLine(lineLen, tipNums, line)   # all black to left as possible
    logging.info("----MostRight")
    offRigh = getMostRightLine(lineLen, tipNums, line)  # all black to right as possible  
    lineOK  = offLeft == offRigh    
    logging.info("\t%s\n%s\n%s" % (lineOK, offLeft, offRigh))
    newLine = mixLeftRight(line, offLeft, offRigh)      # get cell suit both left & right
    logging.info("----mix\n%s" % newLine)
    if not lineOK: 
        newLine = checkCross(newLine, tipNums, offLeft, offRigh) 
        logging.info("----checkCross\n%s\n" % newLine)
    return newLine, lineOK


def checkCross(newLine, tipNums, mostLeft, mostRight):
    '''
    check cross: if virgin block'len less than black block which may appear, must be cross
    '''    
    global virgin, cross, black
    off, blockLen = mostLeft[0][1] + 1, 1
    while off < mostRight[-1][0]:
        if newLine[off] != virgin:
            off += 1
        else:
            while newLine[off + blockLen] == virgin:
                if off + blockLen == mostRight[-1][0]: # == is ok, not need >=
                    return newLine
                blockLen += 1
            if newLine[off - 1] == cross and newLine[off + blockLen] == cross:
                bigThanOneHere = False
                for i in range(len(tipNums)):
                    if off >= mostLeft[i][0]:
                        if off <= mostRight[i][1] and blockLen >= tipNums[i]:
                            bigThanOneHere = True
                            break
                    else:
                        break
                if not bigThanOneHere:
                    for n in range(blockLen):
                        newLine[off + n] = cross
            off += (blockLen + 1)
            blockLen = 1
    return newLine


def mixLeftRight(line, mostLeft, mostRight):    
    global virgin, cross, black
    tipNum, lineLen = len(mostLeft), len(line)
    for n in range(mostLeft[0][0]):
        line[n] = cross
    for i in range(tipNum - 1):
        for n in range(mostRight[i][0], mostLeft[i][1] + 1):
            line[n] = black
        for n in range(mostRight[i][1] + 1, mostLeft[i + 1][0]):
            line[n] = cross  
    for n in range(mostRight[-1][0], mostLeft[-1][1] + 1):
        line[n] = black
    for n in range(mostRight[-1][1] + 1, lineLen):
        line[n] = cross
    return line    


def getMostRightLine(lineLen, tipNums, line):
    offReverse = getMostLeftLine(lineLen, tipNums[::-1], line[::-1])
    offRigh = []
    for n in offReverse:
        offRigh.append((lineLen - 1 - n[1], lineLen - 1 - n[0]))
    return offRigh[::-1]

    
def getMostLeftLine(lineLen, tipNums, line):
    global virgin, cross, black
    nextpos, num, tipLen, lastBlack = 0, 0, len(tipNums), lineLen - 1
    offLeft, newLine = [(0, 0)] * len(tipNums), [virgin] * lineLen
    while line[lastBlack] != black and lastBlack >= 0:
        lastBlack -= 1
    while num < tipLen:
        # logging.info("AAAA: nextpos:%s, num:%s\n%s" % (nextpos, num, newLine))
        nextpos = findNextBlockStart(lineLen, tipNums[num], line, nextpos)            
        # logging.info(" %s, %s" % (nextpos, num))
        newLine, numNew, nextpos = checkBefore(tipNums, num, line, newLine, nextpos)            
        # logging.info(" %s, %s\n%s" % (nextpos, numNew, newLine))
        blockLen = tipNums[numNew]
        for i in range(nextpos, nextpos + blockLen):  
            newLine[i] = black
        # logging.info("BBBB: nextpos:%s, num:%s\n%s" % (nextpos, numNew, newLine))

        if numNew == tipLen - 1 and lastBlack > nextpos + blockLen:
            # logging.info("  num:%s, tipLen%s, lastBlack:%s, nextpos:%s, blockLen:%s" % (num, tipLen, lastBlack, nextpos, blockLen))
            newLine, numNew, nextpos = checkBefore(tipNums, num + 1, line, newLine, lastBlack + 1)
            if newLine[nextpos - 1] == black:
                nextpos += 1
            blockLen = tipNums[numNew]
            for i in range(nextpos, nextpos + blockLen):  
                newLine[i] = black
        offLeft[numNew] = (nextpos, nextpos + blockLen - 1) # add each block's start&end
        nextpos += (blockLen + 1)                
        # logging.info("CCCC: nextpos:%s, num:%s\n%s" % (nextpos, numNew, newLine))
        num = numNew + 1
    return offLeft


def checkBefore(tipNums, num, line, newLine, nextpos):
    '''
    check pre suit block need move right or not
    '''
    global virgin, cross, black
    if num == 0:                          # if pre still have black, means wrong table
        return newLine, num, nextpos
    checkpos = nextpos - 1
    while line[checkpos] != black:        # find pre black in line
        if checkpos == 0:
            return newLine, num, nextpos
        checkpos -= 1
    if newLine[checkpos] == black:        # means every block in line covered, so OK  
        return newLine, num, nextpos
    preBlockEnd = checkpos - 1    
    while newLine[preBlockEnd] != black : # find pre block in newLine, must be there
        preBlockEnd -= 1
   
    checkNum = num - 1
    preBlockLen = tipNums[checkNum]
    skippos = checkpos - preBlockLen + 1
    # logging.info("####%s, %s, checkpos:%s, preBlockEnd:%s, skippos:%s\n%s" % (checkNum, preBlockLen, checkpos, preBlockEnd, skippos, newLine))
    for i in range(preBlockEnd - preBlockLen + 1, preBlockEnd + 1):                            
        newLine[i] = virgin             # remove (pre block)
    for pos in range(checkpos - preBlockLen, checkpos):
        if line[pos] != black:            
            skippos = pos + 1
            return checkBefore(tipNums, checkNum, line, newLine, skippos)
        elif line[pos + preBlockLen + 1] == cross: # and will not suit pre cell cross
            return checkBefore(tipNums, checkNum, line, newLine, checkpos + 1)
    else:                                 # need pre more long block
        return checkBefore(tipNums, checkNum, line, newLine, checkpos + 1)


def findNextBlockStart(lineLen, blockLen, line, start):
    global virgin, cross, black
    pos, find = start, False
    # logging.info("start:%s, blockLen:%s" % (start, blockLen))
    while not find:
        while(line[pos] == cross):      # suit block not start with cross
            pos += 1        
        newpos = pos
        for i in range(1, blockLen):
            if line[pos + i] == cross:  # suit block len short than black
                newpos += (i + 1)       # check current cell's next
                break

        # logging.info("pos:%s, newpos:%s" % (pos, newpos))
        if pos == newpos:
            try:
                if pos == 0:
                    if blockLen == lineLen or line[pos + blockLen] != black:
                        return pos
                    pos += 1  
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
            except Exception as e:                # black block can reach end
                if (pos + blockLen) == lineLen and line[pos - 1] != black:
                    find = True
                else:
                    raise e
        else:
            pos = newpos
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
        print('', table.index(line))
    print()




if __name__ == '__main__':

    import re
    with open("0032up.rtf", 'r') as r:
    # with open("output.rtf", 'r') as r:
        data = r.read()
    
    numberStr = data.split('\n')
    numbers = []
    reg = re.compile(r'(\d+)')
    for i in numberStr:
        if reg.match(i):
            numbers.append(list(map(int, reg.findall(i))))
    #print(numbers)
    nonogram(numbers)