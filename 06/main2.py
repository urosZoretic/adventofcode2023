
# inputFile = "./06/input_example_1.txt"
inputFile = "./06/input.txt"


if __name__ == '__main__':

    with open(inputFile, "r") as f:
        lines = f.read().strip().split("\n")

    time = int(''.join([ t for t in lines[0].split(':')[1].strip().split(' ')]))
    distance =  int(''.join([ d.strip() for d in lines[1].split(':')[1].strip().split(' ')]))

    print(time, distance)
    nbWins = 0
    for speed in range (1, time):
        distanceTravel = speed * (time - speed)  ## we can travel speed * time => speed - timLeft
        if distanceTravel > distance:
            nbWins += 1
            # print("distance: ", distanceTravel, " speed: ", speed, " time travel: ", time - speed, " record distance: ", distance)
        if nbWins != 0 and distanceTravel <= distance:
            break

    # print(lines)
    # print(times)
    # print(distances)


    print('par1 rs: ', nbWins)