
# inputFile = "./08/input_example_2.txt" # "./08/input_example_1.txt"
inputFile = "./08/input.txt"

if __name__ == '__main__':
    
    with open(inputFile, "r") as f:
        lines = f.read().strip().split("\n")


    instructions = lines[0]
    mapDict = {}

    for i, l in enumerate(lines):
        if i >= 2:
            nodes = l.strip().split(' = ')
            node = nodes[0]
            nextCoordinates = nodes[1][1:len(nodes[1])-1].strip().split(', ')
            mapDict[nodes[0]] = nextCoordinates
        pass

    # print(mapDict)
    steps = 0
    currentNode = 'AAA'
    while True:
        instruction = instructions[steps % len(instructions)]
        steps += 1

        nextSteps = mapDict[currentNode]
        if instruction == 'L': # we go left
            currentNode = nextSteps[0]
        else: # or we go right
            currentNode =nextSteps[1]
        
        # print(instruction, currentNode)
        if currentNode == 'ZZZ':
            break

    print('part 1 rs: ', steps)