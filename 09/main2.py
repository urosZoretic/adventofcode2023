# inputFile = "./09/input_example_1.txt"
inputFile = "./09/input.txt"

def getNextSequence(entry):
    sequence = []
    for i, item in enumerate(entry):
        if i == 0:
            continue
        previous = entry[i - 1]
        sequence.append(item - previous)

    return sequence

if __name__ == '__main__':
    
    with open(inputFile, "r") as f:
        lines = f.read().strip().split("\n")

    histories = []
    for l in lines:
        history = [int(x.strip()) for x in l.strip().split(' ')]
        histories.append(history)

    oasisReport = 0
    for history in histories:
        seq = history
        pyramid = [seq]
        while not all(item == 0 for item in seq):
            seq = getNextSequence(seq)
            pyramid.insert(0, seq)
        num = 0
        for i in range(1, len(pyramid) ):
            num = pyramid[i][0] - num
        # print(num)
        oasisReport += num

    print('part 2 rs: ', oasisReport)

