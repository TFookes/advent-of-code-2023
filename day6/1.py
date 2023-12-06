import math

def compute_diatnce(wind_up, total_time):
    return wind_up * (total_time - wind_up)


if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]

    races = {}
    times = []
    distances = []

    for line in lines:
        s = line.split(':')
        if s[0] == 'Time':
            for x, time in enumerate(s[1].split()):
                times += [int(time)]

        elif s[0] == 'Distance': 
            for x, dist in enumerate(s[1].split()):
                distances += [int(dist)]

    for i, t in enumerate(times):
        races[t] = distances[i]

    print(races)

    perms_that_win = []
    for race in races:    
        wins = 0
        for i in range(0, race):
            if compute_diatnce(i, race,) > races[race]: wins += 1
    
        perms_that_win += [wins]
        print(perms_that_win)

    print(math.prod(perms_that_win))