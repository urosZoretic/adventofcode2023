# inputFile = "./07/input_example_1.txt"
inputFile = "./07/input.txt"

def checkType(hand):
    labelsDict = {}
    for label in hand:
        if label in labelsDict:
         labelsDict[label] += 1
        else:
           labelsDict[label] = 1

    jokerNb = 0
    if 'J' in labelsDict:
        jokerNb = labelsDict['J']
        del labelsDict['J']
    # print(labelsDict)
    labelsDictSorted = sorted(labelsDict.items(), key=lambda x: x[1], reverse=True)

    # print(labelsDictSorted, hand, jokerNb)
    if len(labelsDictSorted) == 0:
        labelsDictSorted.append(('J', jokerNb))
    else:
        c, v = labelsDictSorted[0]
        v += jokerNb
        labelsDictSorted[0] = (c, v)

    # print(labelsDictSorted, len(labelsDictSorted), jokerNb, c, v)
 
    ## check type
    if len(labelsDictSorted) == 1: ## only on different labels
       return 'five-of-a-kind'
    
    if len(labelsDictSorted) == 2:
        _, nb = labelsDictSorted[0]
        if nb == 4: ## four of a kind
            return 'four-of-a-kind'
        if nb == 3: ## full house
            return 'full-house'
        else:
           print('somethign wrong len 2')
           exit(1)
    
    if len(labelsDictSorted) == 3:
        _, nb = labelsDictSorted[0]
        if nb == 3: ## Three of a kind
            return 'three-of-a-kind'       
        if nb == 2: ## Two pair
            return 'two-pair'
        else:
           print('somethign wrong len 3')
           exit(1)
    if len(labelsDictSorted) == 4: ## one pair
        return 'one-pair'
    
    return 'high-card'

## all hands have 5 card
def checkOrdering(firstHand, secondHand):
    cardOrdering = {
        'A': 1,
        'K': 2,
        'Q': 3,
        'T': 4,
        '9': 5,
        '8': 6,
        '7': 7,
        '6': 8,
        '5': 9,
        '4': 10,
        '3': 11,
        '2': 12,
        'J': 13,
    }

    for i, card in enumerate(firstHand):
        if card == secondHand[i]:
            continue
        
        pOne = cardOrdering[card]
        pTwo = cardOrdering[secondHand[i]]
        if pOne < pTwo:
            return firstHand
        else:
            return secondHand


def insertToArray(typeArray, nextHand):
    # print(nextHand, nextHand[0], nextHand[1])
    indexToInsert = -1
    for i, hand in enumerate(typeArray):
        if checkOrdering(hand[0], nextHand[0]) == hand[0]: ## current in array is bigger then current to insert
            indexToInsert = i
            break
    
    if indexToInsert >= 0:
        typeArray.insert(indexToInsert, nextHand)
    else:
        typeArray.append(nextHand)


    return typeArray

if __name__ == '__main__':
    with open(inputFile, "r") as f:
        lines = f.read().strip().split("\n")

    fiveOfAKind = []
    fourOfAKind = []
    fullHouse = []
    threeOfAKind = []
    twoPair = []
    onePair = []
    highCard = []
    
    for l in lines:
        game = l.strip().split(' ')
        hand = game[0]
        bid = int(game[1])

        # print(hand, 'bid: ', bid)
        match checkType(hand):
            case 'five-of-a-kind':
                fiveOfAKind = insertToArray(fiveOfAKind, (hand, bid))
                pass
            case 'four-of-a-kind':
                fourOfAKind = insertToArray(fourOfAKind, (hand, bid))
                pass
            case 'full-house':
                fullHouse = insertToArray(fullHouse, (hand, bid))
                pass
            case 'three-of-a-kind':
                threeOfAKind = insertToArray(threeOfAKind, (hand, bid))
                pass
            case 'two-pair':
                twoPair = insertToArray(twoPair, (hand, bid))
                pass
            case 'one-pair':
                onePair = insertToArray(onePair, (hand, bid))
                pass
            case 'high-card':
                highCard = insertToArray(highCard, (hand, bid))
                pass
        

    '''print(fiveOfAKind)
    print(fourOfAKind)
    print(fullHouse)
    print(threeOfAKind)
    print(twoPair)
    print(onePair)
    print(highCard)'''

    totalWinning = 0
    rank = 1

    for hand in highCard:
       totalWinning += (rank * hand[1])
       rank += 1

    for hand in onePair:
       totalWinning += (rank * hand[1])
       rank += 1

    for hand in twoPair:
       totalWinning += (rank * hand[1])
       rank += 1

    for hand in threeOfAKind:
       totalWinning += (rank * hand[1])
       rank += 1

    for hand in fullHouse:
       totalWinning += (rank * hand[1])
       rank += 1

    for hand in fourOfAKind:
       totalWinning += (rank * hand[1])
       rank += 1

    for hand in fiveOfAKind:
       totalWinning += (rank * hand[1])
       rank += 1

    print('part 2 rs: ', totalWinning)