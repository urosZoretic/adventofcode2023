
# inputFile = "./06/input_example_1.txt"
inputFile = "./06/input.txt"


if __name__ == '__main__':

    with open(inputFile, "r") as f:
        lines = f.read().strip().split("\n")

    times = []
    [times.append(int(t.strip())) if t.strip() != '' else '' for t in lines[0].split(':')[1].strip().split(' ')]
    distances = []
    [distances.append(int(d.strip())) if d.strip() != '' else '' for d in lines[1].split(':')[1].strip().split(' ')]

    # print(lines)
    # print(times)
    # print(distances)

    nbWaysToWin = 0
    for i, t in enumerate(times):
        nbWins = 0
        for speed in range (1, t):
            distanceTravel = speed * (t - speed)  ## we can travel speed * time => speed - timLeft
            # print("distance: ", distanceTravel, " speed: ", speed, " time travel: ", t-speed, " record distance: ", distances[i])
            if distanceTravel > distances[i]:
                nbWins += 1
            if nbWins != 0 and distanceTravel <= distances[i]:
                break
        
        if nbWaysToWin == 0:
            nbWaysToWin = nbWins
        else:
            nbWaysToWin *= nbWins
        # print("wins: ", nbWins)

    print('par1 rs: ', nbWaysToWin)