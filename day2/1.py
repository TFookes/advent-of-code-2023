dice = {
    "red" : 12,
    "green" : 13,
    "blue" : 14,
}


def possible(lineId, sets):
    for set in sets:
        red = 0
        green = 0
        blue = 0
        for pull in set.split(','):
            x = pull.strip().split(' ')
            match x[1]:
                case 'red': red += int(x[0])
                case 'green': green += int(x[0])
                case 'blue': blue += int(x[0])

        print(f'red: {red}, green: {green}, blue: {blue}')
        if red > dice['red'] or green > dice['green'] or blue > dice['blue']: 
            print('no valid')
            return 0

    return int(lineId)


if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]

        total = 0 
        for line in lines:
            lineId = line.split(':')[0].split(' ')[1]
            print(lineId)
            sets = line.split(':')[1].strip().split(';')
            print(sets)
            total += possible(lineId, sets)

        print(total)