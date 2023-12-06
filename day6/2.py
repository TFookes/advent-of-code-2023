import math

total_time = 0 
dist = 0

global_min = None
global_max = None

def compute_distance(wind_up):
    return wind_up * (total_time - wind_up)


def find_min(min_time, max_time):
    global global_min
    global global_max

    if min_time == max_time or abs(min_time - max_time) == 1: 
        if compute_distance(min_time) > dist: global_min = min_time
        else: global_min = max_time
        print("MIN!: ", global_min)
    else:
        if compute_distance(min_time + math.floor((max_time - min_time) / 2)) > dist:
            find_min(min_time, max_time - math.floor((max_time - min_time) / 2))
        else: 
            find_min(min_time + math.floor((max_time - min_time) / 2), max_time)


def find_max(min_time, max_time):
    global global_min
    global global_max
    
    if min_time == max_time or abs(min_time - max_time) == 1: 
        if compute_distance(max_time) > dist: global_max = max_time
        else: global_max = min_time
        print("MAX!: ", global_max)
    else:
        if compute_distance(min_time + math.floor((max_time - min_time) / 2)) > dist:
            find_max(min_time + math.floor((max_time - min_time) / 2), max_time)
        else: 
            find_max(min_time, max_time - math.floor((max_time - min_time) / 2))


def find_start(min_time, max_time):
    if compute_distance(math.floor(max_time - min_time / 2)) > dist:
        find_max(min_time + math.floor(max_time - min_time / 2), total_time)
        find_min(0, min_time + math.floor(max_time - min_time / 2))
    elif global_min is None and global_max is None:
        find_start(min_time + math.floor((max_time - min_time) / 2), max_time) # Look above for ranges
        find_start(min_time, max_time - math.floor((max_time - min_time) / 2)) # Look below for ranges
        

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
                times += [time]

        elif s[0] == 'Distance': 
            for x, dist in enumerate(s[1].split()):
                distances += [dist]

    total_time = int(''.join(times))
    dist = int(''.join(distances))

    print(total_time, dist)

    wins_lower = 0
    wins_upper = 0

    find_start(0, total_time) 
    print("Min", global_min, "Max", global_max)
    print(global_max - global_min + 1)
    #print(math.floor((total_time - 0) / 2))
    #print(compute_distance(math.floor((total_time - 0) / 2)))
    #print(compute_distance(math.floor((total_time - 0) / 2)) > 0)