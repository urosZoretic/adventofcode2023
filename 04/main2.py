
# inputFile = "./04/input_example_1.txt"

inputFile = "./04/input.txt"


# https://adventofcode.com/2023/day/4


if __name__ == '__main__':

    with open(inputFile, "r") as f:
        lines = f.read().split("\n")


    nbCopiesGames = [1 for x in range(len(lines))]

    for i, line in enumerate(lines):
        game = [ l.strip() for l in line.split(':')[1].strip().split('|') ]
        winningNumbers = {}
        for winningNumber in game[0].split(' '):
            if winningNumber.strip() != '' and winningNumber.isnumeric():
                winningNumbers[winningNumber.strip()] = {}

        nbMatch = 0
        for nb in game[1].split(' '):
            nbClean = nb.strip()
            if nbClean == '' or not nbClean.isnumeric():
                continue
            if nbClean in winningNumbers:
                nbMatch += 1

        
        currentGameCoypies = nbCopiesGames[i]
        for j in range(nbMatch):
            nextGameIndex = i + j + 1
            if nextGameIndex < len(nbCopiesGames):
                nbCopiesGames[nextGameIndex] += currentGameCoypies

        # print(game, winningNumbers, nbMatch, nbCopiesGames)


    print('part 2 rs: ', sum(nbCopiesGames))
