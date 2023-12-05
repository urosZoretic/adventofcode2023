
# inputFile = "./05/input_example_1.txt"
inputFile = "./05/input.txt"

def getMappingForMapReversed(seed, seedToX):
    for mapping in reversed(seedToX):
        if seed >= mapping[0] and seed < mapping[0] + mapping [2]:
            diffMapping = abs(mapping[1] - mapping[0])
            if mapping[1] > mapping[0]:
                seed += diffMapping
            if mapping[1] < mapping[0]:
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
    
    
    seedMaps = []
    for i in range(0, len(seeds), 2):
        seedMaps.append((seeds[i], seeds[i+1]))


    print(seedMaps)

    location = 0
    while True:
        humidity = getMappingForMapReversed(location, humidityToLocation)
        # print(humidity)
        temperature = getMappingForMapReversed(humidity, temperatureToHumidity)
        # print(temperature)
        light = getMappingForMapReversed(temperature, lightToTemperature)
        # print(light)
        water = getMappingForMapReversed(light, waterToLight)
        # print(water)
        fertilizer = getMappingForMapReversed(water, fertilizerToWater)
        # print(fertilizer)
        soil = getMappingForMapReversed(fertilizer, soilToFertilizer)
        # print(soil)
        seed = getMappingForMapReversed(soil, seedToSoil)
        # print(seed)
        
        if location % 100000 == 0:
            print("seed: ",  seed, "location: ", location)
        isFound = False
        for start, end in seedMaps:
            # print("start: ", start, "end: ", end)
            if seed >= start and seed < start + end:
                isFound = True
                break

        if isFound:
            break
        location += 1

    print("rs part 2: ", location)
