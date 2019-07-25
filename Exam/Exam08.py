## 문제 8

import random as rd
from pprint import pprint
tile = []
for i in range(5):
    row = []
    for k in range(5):
        tmp = rd.randint(1, 4)
        row.append(tmp)
        print(tmp, end=' ')
    tile.append(row)
    print()
#pprint(tile, indent=2)
tpTile = [list(x) for x in zip(*tile)]

def findPung(line):  # 한 라인을 매개변수로 받아, 결과, 시작, 끝 인덱스 반환
    start = 0
    stop = 0
    pung = False
    for i in range(3):
        if line[i] != line[i+1] or line[i+1] != line[i+2]:
            continue
        pung = True
        start = i
        stop = i+2
        if i == 2:
            break
        if line[i+2] != line[i+3]:
            break
        stop = i+3
        if i == 1:
            break
        if line[i+3] == line[i+4]:
            stop = i+4
        break
    return pung, start, stop

def copyLine(pung, start, stop, line):
    newLine = line.copy()
    if pung:
        for i in range(start, stop+1):
            newLine[i] = 8
    return newLine

rowResult = []
for i in range(5):
    pung, start, stop = findPung(tile[i])
    #print(pung, start, stop, tile[i])
    rowResult.append(copyLine(pung, start, stop, tile[i]))
#pprint(rowResult, indent=2)

colResult = []
for i in range(5):
    pung, start, stop = findPung(tpTile[i])
    #print(pung, start, stop, tpTile[i])
    colResult.append(copyLine(pung, start, stop, tpTile[i]))
#pprint(colResult, indent=2)
tpColResult = [list(x) for x in zip(*colResult)]

print('   ==>')
for i in range(5):
    for k in range(5):
        if rowResult[i][k] == 8 or tpColResult[i][k] == 8:
            tile[i][k] = '*'
            print('*', end=' ')
        else:
            tile[i][k] = str(tile[i][k])
            print(tile[i][k], end=' ')
    print()
#pprint(tile, indent=2)