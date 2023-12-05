
# inputFile = "./05/input_example_1.txt"
inputFile = "./05/input.txt"

def getMappingForMap(seed, seedToX):
    for mapping in seedToX:
        if seed >= mapping[1] and seed <= mapping[1] + mapping [2]:
            diffMapping = abs(mapping[1] - mapping[0])
            if mapping[1] < mapping[0]:
                seed += diffMapping
            if mapping[1] > mapping[0]:
                seed -= diffMapping
            
            return seed
    

    return seed


if __name__ == '__main__':

    with open(inputFile, "r") as f:
        lines = f.read().split("\n")

    seeds = []
    seedToSoil = []
    soilToFertilizer = []
    fertilizerToWater = []
    waterToLight = []
    lightToTemperature = []
    temperatureToHumidity = []
    humidityToLocation = []

    mapType = ''


    for i, line in enumerate(lines):
        if i == 0:
            seeds = [ int(x.strip()) for x in  line.split(':')[1].strip().split(' ') ]
            continue
        if line == 'seed-to-soil map:':
            mapType = 'seed-to-soil'
            continue
        if line == 'soil-to-fertilizer map:':
            mapType = 'soil-to-fertilizer'
            continue
        if line == 'fertilizer-to-water map:':
            mapType = 'fertilizer-to-water'
            continue
        if line == 'water-to-light map:':
            mapType = 'water-to-light'
            continue
        if line == 'light-to-temperature map:':
            mapType = 'light-to-temperature'
            continue
        if line == 'temperature-to-humidity map:':
            mapType = 'temperature-to-humidity'
            continue
        if line == 'humidity-to-location map:':
            mapType = 'humidity-to-location'
            continue
        if line == '':
            mapType = ''
            continue
        
        match mapType:
            case 'seed-to-soil':
                seedToSoil.append([int(x.strip()) for x in line.split(' ') ])
                continue
            case 'soil-to-fertilizer':
                soilToFertilizer.append([int(x.strip()) for x in line.split(' ') ])
                continue
            case 'fertilizer-to-water':
                fertilizerToWater.append([int(x.strip()) for x in line.split(' ') ])
                continue
            case 'water-to-light':
                waterToLight.append([int(x.strip()) for x in line.split(' ') ])
                continue
            case 'light-to-temperature':
                lightToTemperature.append([int(x.strip()) for x in line.split(' ') ])
                continue
            case 'temperature-to-humidity':
                temperatureToHumidity.append([int(x.strip()) for x in line.split(' ') ])
                continue
            case 'humidity-to-location':
                humidityToLocation.append([int(x.strip()) for x in line.split(' ') ])
                continue
    
    '''print('seeds: ', seeds)
    print(seedToSoil)
    print(soilToFertilizer)
    print(fertilizerToWater)
    print(waterToLight)
    print(lightToTemperature)
    print(temperatureToHumidity)
    print(humidityToLocation)'''

    # location for one 79
    minLocation = 0

    for i, seed in enumerate(seeds):
        soil = getMappingForMap(seed, seedToSoil)
        # print(soil)
        fertilizer = getMappingForMap(soil, soilToFertilizer)
        # print(fertilizer)
        water = getMappingForMap(fertilizer, fertilizerToWater)
        # print(water)
        light = getMappingForMap(water, waterToLight)
        # print(light)
        temperature = getMappingForMap(light, lightToTemperature)
        # print(temperature)
        humidity = getMappingForMap(temperature, temperatureToHumidity)
        # print(humidity)
        location = getMappingForMap(humidity, humidityToLocation)
        # print(location)
        # print("---------------------------")
        if i == 0:
            minLocation = location
        else:
            if location < minLocation:
                minLocation = location

    print("part 1 rs min location: ", minLocation)