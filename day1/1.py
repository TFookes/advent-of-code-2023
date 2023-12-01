def decode(line):
    first = ''
    last = ''
    for char in line:
        if char.isdigit() and first == '':
            first = char
        
        if char.isdigit():
            last = char

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