
# inputFile = "./03/input_example_1.txt"

inputFile = "./03/input.txt"


def isDigit(val):
    return str(val).isdigit()


def isNumberAdjecentToSymbolAndWhichAsterisks(number, asterisks):
    n, numberCoord = number
    xNumber, yNumber = numberCoord

    for xs, ys in asterisks:
        for xc, yc in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            xAdjecent = xs + xc
            yAdjecent = ys + yc
            for numbYIndex in range(len(str(n))):
                if (xAdjecent, yAdjecent) == (xNumber, yNumber + numbYIndex):
                    return True, (xs, ys)
    
    return False, ()


# https://adventofcode.com/2023/day/3
if __name__ == '__main__':

    with open(inputFile, "r") as f:
        lines = f.read().split("\n")

    asterisks = []
    asterisksAdjecents = {}
    numbers = []

    for x, line in enumerate(lines):
        # print(x, line)
        y = 0
        while y < len(line):
            val = line[y]
            if  val == '*':
                asterisks.append((x, y))
                asterisksAdjecents[(x, y)] = []
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
    # print(asterisks)
    # print(asterisksAdjecents)

    for number in numbers:
        isAdjecent, asteriskCoord = isNumberAdjecentToSymbolAndWhichAsterisks(number, asterisks)
        if isAdjecent:
            asterisksAdjecents[asteriskCoord].append(number[0])
            # print(number[0], asteriskCoord, asterisksAdjecents[asteriskCoord])

    sumGearRationsSemantic = 0
    for _, adjecentArray in asterisksAdjecents.items():
        if len(adjecentArray) == 2:
            sumGearRationsSemantic += (adjecentArray[0] * adjecentArray[1])

    print('part 2 rs: ', sumGearRationsSemantic)