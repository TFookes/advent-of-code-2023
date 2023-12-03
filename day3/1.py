def get_number(row, pos):
    number = row[pos]
    for i in range(1, pos + 1):
        if row[pos - i].isdigit(): number = row[pos - i] + number
        else: break

    for i in range(pos + 1, len(row)):
        if row[i].isdigit(): number = number + row[i]
        else: break

    print(number)
    return number

def is_symbol(char):
    return not (char.isdigit() or char == '.')


def check_adjacent(row, above, below, pos):
    if pos == len(row) - 1:
        sameRow = (is_symbol(row[pos - 1])) 
        rowAbove = (is_symbol(above[pos - 1]) or is_symbol(above[pos])) 
        rowBelow = (is_symbol(below[pos - 1]) or is_symbol(below[pos]))
    elif pos == 0:
        sameRow = (is_symbol(row[pos + 1])) 
        rowAbove = (is_symbol(above[pos]) or is_symbol(above[pos + 1])) 
        rowBelow = (is_symbol(below[pos]) or is_symbol(below[pos + 1]))
    else:
        sameRow = (is_symbol(row[pos - 1]) or is_symbol(row[pos + 1])) 
        rowAbove = (is_symbol(above[pos - 1]) or is_symbol(above[pos]) or is_symbol(above[pos + 1])) 
        rowBelow = (is_symbol(below[pos - 1]) or is_symbol(below[pos]) or is_symbol(below[pos + 1]))

    return sameRow or rowAbove or rowBelow


if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]

    rows = []
    for line in lines:
        rows += [[x for x in line]]

    # for row in rows: print(row) 

    sum = 0
    previous_number = None

    for i, row in enumerate(rows): 
        for j, char in enumerate(row):
            number = None
            if char.isdigit(): 
                if previous_number is not None and char in previous_number: continue
                if i == 0:
                    if check_adjacent(row, row, rows[i + 1], j):
                        number = get_number(row, j)
                elif i == len(rows) - 1:
                    if check_adjacent(row, rows[i - 1], row, j):
                        number = get_number(row, j)
                else:
                    if check_adjacent(row, rows[i - 1], rows[i + 1], j):
                        number = get_number(row, j)
            else:
                previous_number = None

            if number is not None: 
                sum += int(number)
                previous_number = number

    print(sum)