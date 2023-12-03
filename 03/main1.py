
# inputFile = "./03/input_example_1.txt"

inputFile = "./03/input.txt"


def isDigit(val):
    return str(val).isdigit()


def isSymbol(val):
    return not(isDigit(val) or val == '.')


def isNumberAdjecentToSymbol(number, symbols):
    n, numberCoord = number
    xNumber, yNumber = numberCoord

    for xs, ys in symbols:
        for xc, yc in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            xAdjecent = xs + xc
            yAdjecent = ys + yc
            for numbYIndex in range(len(str(n))):
                if (xAdjecent, yAdjecent) == (xNumber, yNumber + numbYIndex):
                    return True
    
    return False


# https://adventofcode.com/2023/day/3
if __name__ == '__main__':

    with open(inputFile, "r") as f:
        lines = f.read().split("\n")

    symbols = []
    numbers = []

    for x, line in enumerate(lines):
        # print(x, line)
        y = 0
        while y < len(line):
            val = line[y]
            if isSymbol(val):
                symbols.append((x, y))
                y += 1
            elif isDigit(val):
                number = ""
                numCoord = (x, y)
                while y < len(line) and isDigit(line[y]):
                    number += line[y]
                    y +=1
                numbers.append((int(number), numCoord))
            else:
                y += 1
    
    # print(numbers)
    # print(symbols)

    sumAdjecentNumbers = 0
    for number in numbers:
        if isNumberAdjecentToSymbol(number, symbols):
            sumAdjecentNumbers += number[0]


    print('part 1 rs: ', sumAdjecentNumbers)
