import math
from collections import defaultdict
from pprint import pprint

if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]

    numTickets = defaultdict(lambda: 1)

    for ticket, line in enumerate(lines):
        split = line.split(':')[1].strip().split(' | ')
        winningNumbers = set([int(x) for x in split[0].split()])
        matchNumbers = set([int(x) for x in split[1].split()])

        intersection = winningNumbers.intersection(matchNumbers)

        print(f'Found {len(intersection)} matching number(s), updating tickets {[ticket + i for i in range(1, len(intersection) + 1)]} with {numTickets[ticket]} additonal copies')
        for i in range(ticket + 1, ticket + len(intersection) + 1):
            numTickets[i] += 1 * numTickets[ticket]

    pprint(numTickets, sort_dicts=True)
    print(sum(numTickets.values()))

