import math

if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]

    sum = 0

    for line in lines:
        split = line.split(':')[1].strip().split(' | ')
        winningNumbers = set([int(x) for x in split[0].split()])
        matchNumbers = set([int(x) for x in split[1].split()])

        intersection = winningNumbers.intersection(matchNumbers)
        if len(intersection) > 0: sum += math.pow(2, len(intersection) - 1)

    print(sum)

