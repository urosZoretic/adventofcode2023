
import math

# inputFile = "./08/input_example_3.txt"
inputFile = "./08/input.txt"

if __name__ == '__main__':
    
    with open(inputFile, "r") as f:
        lines = f.read().strip().split("\n")


    instructions = lines[0]
    mapDict = {}

    currentNodes = []
    for i, l in enumerate(lines):
        if i >= 2:
            nodes = l.strip().split(' = ')
            nextCoordinates = nodes[1][1:len(nodes[1])-1].strip().split(', ')
            mapDict[nodes[0]] = nextCoordinates
            if nodes[0][len(nodes[0]) -1 ] == 'A':
                currentNodes.append(nodes[0])
    
    # print(mapDict)    
    stepsForNodes = []

    for currentNode in currentNodes:
        steps = 0
        while True:
            instruction = instructions[steps % len(instructions)]
            steps += 1

            nextSteps = mapDict[currentNode]
            if instruction == 'L': # we go left
                currentNode = nextSteps[0]
            else: # or we go right
                currentNode =nextSteps[1]
            
            # print(instruction, currentNode)
            if currentNode[len(currentNode) - 1] == 'Z':
                break
        
        stepsForNodes.append(steps)


    print('part 2 rs: ', math.lcm(*stepsForNodes))