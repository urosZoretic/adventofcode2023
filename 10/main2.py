# inputFile = "./10/input_example_6.txt" ## example 3, 4, 5, 6
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

'''
F---7 --> on the line not crossing
L---J --> on the line not crossing
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
        # print('checking f: ', currentP, nextPosition, sign)
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
            # print('went wrong F: ', previousPosition, currentPosition)
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


    # print(firstLoop, secondLoop, positionS)
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

    ## edges
    pipeEdges = {}
    for edge in firstLoop:
        pipeEdges[edge] = {}
    for edge in secondLoop:
        pipeEdges[edge] = {}

    sType = ''
    x1, y1 = firstLoop[0]
    x2, y2 = secondLoop[0]

    # is |
    if (x1 + 2, y1) == (x2, y2) or (x1 - 2, y1) == (x2, y2):
        print('|')
        sType = '|'

    # is -
    if (x1, y1 + 2) == (x2, y2) or (x1, y1 - 2) == (x2, y2):
        print('-')
        sType = '-'

    # is L
    if ((x1 + 1, y1 + 1) == (x2, y2) or (x1 - 1, y1 - 1) == (x2, y2)) and x1 < x2:
        print('L')
        sType = 'L'

    # is J
    if ((x1 + 1, y1 - 1) == (x2, y2) or (x1 - 1, y1 + 1) == (x2, y2)) and y1 > y2:
        print('J')
        sType = 'J'

    # is 7
    if ((x1 + 1, y1 + 1) == (x2, y2) or (x1 - 1, y1 - 1) == (x2, y2)) and x2 < x1:
        print('7')
        sType = '7'

    # is F
    if ((x1 - 1, y1 + 1) == (x2, y2) or (x1 + 1, y1 - 1) == (x2, y2)) and y2 > y1:
        print('F')
        sType = 'F'


    mapGround[positionS[0]][positionS[1]] = sType
    pipeEdges[positionS] = {}

    nbTiles = 0
    for x in range (0, len(mapGround)):
        for y in range (0, len(mapGround[x])):
            currentPosition = (x, y)
            if currentPosition in pipeEdges:
                continue

            isInside = False
            onEdge = []
            # print(currentPosition)
            for lookupY in range(y, len(mapGround[x])):
                # print('--------------')
                # print('lookup: ', (x, lookupY))
                if (x, lookupY) in pipeEdges:
                    if mapGround[x][lookupY] == '|':
                        isInside = not isInside
                        # print('vertical edge: ')
                    else:
                        onEdge.append(mapGround[x][lookupY])
 
                    if len(onEdge) > 1:
                        # print('nenene:: ', onEdge)
                        if onEdge[0] == 'F' and onEdge[len(onEdge)-1] == '7':
                            # print(onEdge, 'on edge upper', currentPosition)
                            onEdge = []
                        elif onEdge[0] == 'L' and onEdge[len(onEdge)-1] == 'J':
                            # print(onEdge, 'on edge down', currentPosition)
                            onEdge = []
                        elif onEdge[0] == 'F' and onEdge[len(onEdge)-1] == 'J':
                            # print(onEdge, 'on edge up go ahead', currentPosition)
                            isInside = not isInside
                            # print('chaning omg omg: ', isInside)
                            onEdge = []
                        elif onEdge[0] == 'L' and onEdge[len(onEdge)-1] == '7':
                            # print(onEdge, 'on edge down go ahead', currentPosition)
                            isInside = not isInside
                            onEdge = []
                        elif onEdge[len(onEdge)-1] == '-':
                            pass
                        else:
                            print('horrible wrong')
                            exit(1)
                # print('status: ', isInside, onEdge)
            if isInside:
                # print('inside: ', currentPosition)
                nbTiles += 1
    
    print("part 2 rs: ", nbTiles)
