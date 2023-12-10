# inputFile = "./10/input_example_1.txt" # exmplae 1, 2
inputFile = "./10/input.txt"

'''
| --> north-south
-  --> east-south
L  --> north-east
J   --> north-west
7   --> south-west
F   --> south-east
.   --> ground
'''

def isConnected(currentP, nextPosition, sign):
    # print(currentP, nextPosition, sign)
    x, y = currentP
    x1, y1 = nextPosition
    if sign == '|':
        return abs(x - x1) == 1
    if sign == '-':
        return abs (y - y1) == 1
    if sign == 'L':
        if x1 - x == 1:
            return True
        if y - y1 == 1:
            return True
    if sign == '7':
        if y1 - y == 1:
            return True
        if x1 - x == 1:
            return True
    if sign == 'J':
        if y1 - y == 1:
            return True
        if x1 - x == 1:
            return True
    if sign == 'F':
        if y - y1 == 1:
            return True
        if x - x1 == 1:
            return True

    return False

def getNextPosition(previousPosition, currentPosition, sign):
    # print('p: ', previousPosition, 'c: ', currentPosition, sign)
    pX, pY = previousPosition
    cX, cY = currentPosition

    if sign == '|':
        if pX < cX:
            return (cX + 1, cY)
        else:
            return (cX - 1, cY)
    if sign == '-':
        if pY < cY:
            return (cX, cY + 1)
        else:
            return (cX, cY - 1)
    if sign == 'L':
        if cX > pX:
            return (cX, cY + 1)
        elif cY < pY:
            return (cX - 1, cY)
        else:
            print('somethig went wrong L')
            exit(1)
    if sign == '7':
        if cX < pX:
            return (cX, cY - 1)
        elif cY > pY:
            return (cX + 1, cY)
        else:
            print('went wrong 7')
            exit(1)
    if sign == 'J':
        if cX > pX:
            return (cX, cY - 1)
        elif cY > pY:
            return (cX - 1, cY)
        else:
            print('wet wrong J')
            exit(1)
    if sign == 'F':
        if cX < pX:
            return (cX, cY +1)
        elif cY < pY:
            return (cX +1, cY)
        else:
            print('went wrong F')
            exit(1)
    
    print('ground went wrong')
    exit(1)


if __name__ == '__main__':
    mapGround = []
    with open(inputFile, "r") as f:
        mapGround = [ [*x.strip()] for x in  f.read().strip().split("\n")]

    firstLoop = []
    secondLoop = []

    positionS = ()
    # print(mapGround)
    for x, l in enumerate(mapGround):
        for y, l in enumerate(l):
            if mapGround[x][y] == 'S':
                positionS = (x, y)
                break
        
        if not positionS:
            continue
        else:
            break

    ## check first loop connections
    x, y = positionS

    if x+1 < len(mapGround):
        isPosition = isConnected(positionS, (x+1, y), mapGround[x+1][y])
        if isPosition:
            firstLoop.append((x+1, y))

    if x-1 >= 0:
        isPosition = isConnected(positionS, (x-1, y), mapGround[x-1][y])
        if isPosition and len(firstLoop) == 0:
            firstLoop.append((x-1, y))
        elif isPosition:
            secondLoop.append((x-1, y))

    if y+1 < len(mapGround[0]):
        isPosition = isConnected(positionS, (x, y+1), mapGround[x][y+1])
        if isPosition and len(firstLoop) == 0:
            firstLoop.append((x, y+1))
        elif isPosition:
            secondLoop.append((x, y+1))

    if y - 1 >= 0:
        isPosition = isConnected(positionS, (x, y-1), mapGround[x][y-1])
        if isPosition:
            secondLoop.append((x, y-1))

    # print(firstLoop, secondLoop)
    nbIteration = 1
    while firstLoop[len(firstLoop)-1] != secondLoop[len(secondLoop) -1]:
        nbIteration += 1
        firstPrevious = ()
        secondPrevious = ()
        if len(firstLoop) == 1:
            firstPrevious = positionS
            secondPrevious = positionS
        else:
            firstPrevious = firstLoop[len(firstLoop)-2]
            secondPrevious = secondLoop[len(secondLoop)-2]

        currentPositionFirst = firstLoop[len(firstLoop)-1]
        currentPositionSecond = secondLoop[len(firstLoop)-1]

        firstLoop.append(getNextPosition(firstPrevious, currentPositionFirst, mapGround[currentPositionFirst[0]][currentPositionFirst[1]]))
        secondLoop.append(getNextPosition(secondPrevious, currentPositionSecond, mapGround[currentPositionSecond[0]][currentPositionSecond[1]]))

    # print("f: ", firstLoop, "s: ", secondLoop, nbIteration)
    print("part 1 rs: ", nbIteration)
