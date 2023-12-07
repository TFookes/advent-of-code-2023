import json
import math

hand_ranks = {
    "5k" : 6,
    "4k" : 5,
    "fh" : 4,
    "3k" : 3,
    "2p" : 2,
    "1p" : 1,
    "hk" : 0
}

card_ranks = {
    "A" : 13,
    "K" : 12,
    "Q" : 11,
    "J" : 0,
    "T" : 9,
    "9" : 8,
    "8" : 7,
    "7" : 6,
    "6" : 5,
    "5" : 4,
    "4" : 3,
    "3" : 2,
    "2" : 1
}

def determine_type(hand): 
    num_cards = {
        "A" : 0,
        "K" : 0,
        "Q" : 0,
        "J" : 0,
        "T" : 0,
        "9" : 0,
        "8" : 0,
        "7" : 0,
        "6" : 0,
        "5" : 0,
        "4" : 0,
        "3" : 0,
        "2" : 0,
    }   
    jokers = 0
    for card in hand:
        if card == "J": jokers += 1
        else: num_cards[card] += 1

    max_of_same = max(num_cards.values())

    if max_of_same == 5 or jokers == 5: return "5k"
    elif max_of_same == 4: 
        match jokers: 
            case 1: return "5k"
        return "4k"
    elif max_of_same == 1: 
        match jokers:
            case 4: return "5k"
            case 3: return "4k"
            case 2: return "3k"
            case 1: return "1p"
        return "hk"
    elif max_of_same == 3: 
        if 2 in num_cards.values(): 
            return "fh"
        else: 
            match jokers: 
                case 2: return "5k"
                case 1: return "4k"
            return "3k"
    elif max_of_same == 2:
        num_twos = len(list(filter(lambda x: x == 2, num_cards.values())))
        if num_twos == 2: 
            match jokers:
                case 1: return "fh"
            return "2p"
        else: 
            match jokers: 
                case 3: return "5k"
                case 2: return "4k"
                case 1: return "3k"
            return "1p"


def order_rank(hand):
    value = 0
    for i, card in enumerate(hand):
        value += (card_ranks[card]) * math.pow(10, 5 - i - i)

    return value


if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]

    hands = {}
    hand_types = {
        "5k" : [],
        "4k" : [],
        "fh" : [],
        "3k" : [],
        "2p" : [],
        "1p" : [],
        "hk" : []
    }

    for line in lines:
        x = line.split()
        hands[x[0]] =  x[1]

    for hand in hands:
        print(hand)
        hand_types[determine_type(hand)] += [hand]

    #print(json.dumps(hands, indent=4))
    #print(json.dumps(hand_types, indent=4))

    rank = len(hands)

    for type in hand_types:
        hand_types[type] = sorted(hand_types[type], key=order_rank, reverse=True)
        
    print(json.dumps(hand_types, indent=4))

    winnings = 0

    for type in hand_types:
        print("=" * 20)
        print(type)
        print("=" * 20)
        for hand in hand_types[type]: 
            winnings += int(hands[hand]) * rank
            print(hand, hands[hand], rank, int(hands[hand]) * rank, winnings)
            rank -= 1

    print(winnings)
