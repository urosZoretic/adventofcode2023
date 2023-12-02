
# inputFile = "./02/input_example_1.txt"

inputFile = "./02/input.txt"

# https://adventofcode.com/2023/day/2
if __name__ == '__main__':

    with open(inputFile, "r") as f:
        lines = [ v.split(':') for v in f.read().strip().split('\n')]

    # which is possbile game has: only 12 red cubes, 13 green cubes, and 14 blue
    sumPossbile = 0
    for line in lines:
        game = line[0]
        drawsSubsets = [ [ v1.strip().split(' ') for v1 in v.strip().split(',')] for v in line[1].strip().split(';') ]
        isPossbile = True
        for draw in drawsSubsets:
            # print(draw)
            red = 0
            blue = 0
            green = 0
            for turn in draw:
                match turn[1]: # color
                    case 'red':
                        red += int(turn[0])
                    case 'green':
                        green += int(turn[0])
                    case 'blue':
                        blue += int(turn[0])
                    case _:
                        isPossbile = False
                        break
            
            if not isPossbile:
                break
            if red > 12 or green > 13 or blue > 14:
                isPossbile = False
                break
            
            # print('red; ', red, 'green: ', green, 'blue: ', blue)

        if isPossbile:
            sumPossbile += int(game.split(' ')[1])
            # print(game, isPossbile, sumPossbile)

    print('part 1 rs: ', sumPossbile)


    # part 2. What is the sum of the power of these sets?

    sumOfPowerMinSets = 0
    for line in lines:
        game = line[0]
        drawsSubsets = [ [ v1.strip().split(' ') for v1 in v.strip().split(',')] for v in line[1].strip().split(';') ]
        
        # start with 1 because of multiplication
        min_max_Red = 1
        min_max__Blue = 1
        min_max_Green = 1
        for draw in drawsSubsets:
            # print(draw)
            red = 0
            blue = 0
            green = 0
            for turn in draw:
                match turn[1]: # color
                    case 'red':
                        red += int(turn[0])
                    case 'green':
                        green += int(turn[0])
                    case 'blue':
                        blue += int(turn[0])
                    case _:
                        print('something went wrong.. no mathing color')
                        exit(1)
                        break
            
            if red > min_max_Red:
                min_max_Red = red
            if blue > min_max__Blue:
                min_max__Blue = blue
            if green > min_max_Green:
                min_max_Green = green
        
        # print("game ", game, " min red: ", min_max_Red, "min green: ", min_max_Green, "min blue: ", min_max__Blue)
        sumOfPowerMinSets += (min_max_Red * min_max_Green * min_max__Blue)

    print('part 2 rs: ', sumOfPowerMinSets)