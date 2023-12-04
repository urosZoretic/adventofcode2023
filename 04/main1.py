
# inputFile = "./04/input_example_1.txt"

inputFile = "./04/input.txt"


# https://adventofcode.com/2023/day/4


if __name__ == '__main__':

    with open(inputFile, "r") as f:
        lines = f.read().split("\n")


    gamesWorthSum = 0
    for line in lines:
        game = [ l.strip() for l in line.split(':')[1].strip().split('|') ]
        winningNumbers = {}
        for winningNumber in game[0].split(' '):
            if winningNumber.strip() != '' and winningNumber.isnumeric():
                winningNumbers[winningNumber.strip()] = {}



        gameWorth = 0
        for nb in game[1].split(' '):
            nbClean = nb.strip()
            if nbClean == '' or not nbClean.isnumeric():
                continue
            if nbClean in winningNumbers:
                if gameWorth == 0:
                    gameWorth = 1
                else:
                    gameWorth *= 2
        
        gamesWorthSum  += gameWorth
        # print(game, winningNumbers, gameWorth)


    print('part 1 rs: ', gamesWorthSum)
