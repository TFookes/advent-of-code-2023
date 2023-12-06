if __name__ == '__main__':
    f = open("inputs.txt", "r")
    input = []
    for line in f:
        input.append(line.split()[1:])
    f.close()
    total_time = int("".join(input[0]))
    record_distance = int("".join(input[1]))
    race_result = 0
    for press_time in range(1, total_time):
        race_time = total_time - press_time
        speed = press_time  # 1 mm/s per second pressed
        distance = speed * race_time
        if distance > record_distance:
            race_result += 1
    print(race_result)