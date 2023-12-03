def get_number(row, pos):
    number = row[pos]
    start = pos
    end = pos
    for i in range(1, pos + 1):
        if row[pos - i].isdigit(): 
            number = row[pos - i] + number
            start = pos - i
        else: break

    for i in range(pos + 1, len(row)):
        if row[i].isdigit(): 
            number = number + row[i]
            end = i
        else: break

    return (number, start, end)


def is_digit(char):
    return char.isdigit()


def check_adjacent(row, above, below, pos):
    nums = []
    if not(pos == 0) and is_digit(row[pos - 1]): nums += [get_number(row, pos - 1)]
    if not(pos == len(row) - 1) and is_digit(row[pos + 1]): nums += [get_number(row, pos + 1)]

    if not(pos == 0) and is_digit(above[pos - 1]): nums += [get_number(above, pos - 1)]
    if is_digit(above[pos]): nums += [get_number(above, pos)]
    if not(pos == len(row) - 1) and is_digit(above[pos + 1]): nums += [get_number(above, pos + 1)]

    if not(pos == 0) and is_digit(below[pos - 1]): nums += [get_number(below, pos - 1)]
    if is_digit(below[pos]): nums += [get_number(below, pos)]
    if not(pos == len(row) - 1) and is_digit(below[pos + 1]): nums += [get_number(below, pos + 1)]
    
    nums = set(nums)
    if len(nums) != 2: return set()
    print(nums)
    return nums


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
            if char == '*': 
                if i == 0:
                    nums= check_adjacent(row, ['.' for i in len(row)], rows[i + 1], j)
                elif i == len(rows) - 1:
                    nums = check_adjacent(row, rows[i - 1], ['.' for i in len(row)], j)
                else:
                    nums = check_adjacent(row, rows[i - 1], rows[i + 1], j)

                gear = 1
                for num in nums:
                    gear = gear * int(num[0])

                if gear != 1: sum += gear

    print(sum)