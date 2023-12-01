
# inputFile = "./01/input_example_2.txt" # ./01/input_example_1.txt

inputFile = "./01/input.txt"

def checkDigit(c):
    return c if c.isdigit() else ''

def checkDigitSpelled(index, text):
    if index + 3 > len(text):
        return ''
    
    match text[index:index + 3]:
        case 'one':
            return '1'
        case 'two':
            return '2'
        case 'six':
            return '6'

    if index + 4 > len(text):
        return ''

    match text[index:index + 4]:
        case 'four':
            return '4'
        case 'five':
            return '5'
        case 'nine':
            return '9'
    

    if index + 5 > len(text):
        return ''

    match text[index:index + 5]:
        case 'seven':
            return '7'
        case 'eight':
            return '8'
        case 'three':
            return '3'


    return ''

# https://adventofcode.com/2023/day/1
if __name__ == '__main__':

    with open(inputFile, "r") as f:
        lines = f.read().strip().split('\n')


    sumDigits = 0
    for line in lines:
        firstDigit = ''
        for c in line:
            firstDigit = checkDigit(c)
            if firstDigit != '':
                break

        # last digit
        lastDigit = ''
        for c in reversed(line):
            lastDigit = checkDigit(c)
            if lastDigit != '':
                break
        
        if firstDigit != '' and  lastDigit != '':
            sumDigits += int(firstDigit + lastDigit)
    
    print("part 1 rs: ", sumDigits)

    ## part2 copied first part here and added functionalities
    sumDigits = 0
    for line in lines:
        firstDigit = ''
        for i, c in enumerate(line):
            firstDigit = checkDigit(c)
            if firstDigit != '':
                break
            firstDigit = checkDigitSpelled(i, line)
            if firstDigit != '':
                break

        # last digit
        lastDigit = ''
        for i, c in enumerate(reversed(line)):
            lastDigit = checkDigit(c)
            if lastDigit != '':
                break
            # print(i, c)
            lastDigit = checkDigitSpelled(len(line) - 1 - i, line) ## need to revesrse index to look ahead of the line
            if lastDigit != '':
                break

        # print(line, firstDigit, lastDigit)
        if firstDigit != '' and  lastDigit != '':
            sumDigits += int(firstDigit + lastDigit)

    print("part 2 rs: ", sumDigits)


