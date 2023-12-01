numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def check_digit(line, pos, checklist):
    correct = None
    for number in checklist:
        for i in range(0, len(number)):
            try:
                if line[pos + i] != number[i]: break
            except IndexError as e:
                break

            if i == len(number) - 1: correct = f'{numbers[number]}'

    return correct 

def decode(line):
    first = ''
    last = ''
    for i, char in enumerate(line):
        num = None
        if char.isdigit():
            num = char
        elif char == 'o':
            num = check_digit(line, i, ['one'])
        elif char == 't':
            num = check_digit(line, i, ['two', 'three'])
        elif char == 'f':
            num = check_digit(line, i, ['four', 'five'])
        elif char == 's':
            num = check_digit(line, i, ['six', 'seven'])
        elif char == 'e':
            num = check_digit(line, i, ['eight'])
        elif char == 'n':
            num = check_digit(line, i, ['nine'])

        if num is not None:
            if first == '':
                first = num

            last = num

    print(first, last)
    return int(''.join([first, last]))

if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]

        total = 0 
        for line in lines:
            print(line)
            total += decode(line)

        print(total)