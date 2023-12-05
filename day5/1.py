from pprint import pprint

def find_next(current, almamap):
    #print(current, almamap.keys())
    for ranges in almamap.keys():
        if current in range(ranges[0], ranges[1]): 
            return almamap[ranges][0] + (current - ranges[0])
        
    return current

if __name__ == "__main__":
    with open("./test_inputs.txt", "r") as inputs:
        lines = inputs.readlines()
        lines = [line.strip() for line in lines]

    seeds = []
    seeds_soil = {}
    soil_fert = {}
    fert_water = {}
    water_light = {}
    light_temp = {}
    temp_humid = {}
    humid_loc = {}

    current_type = None
    for i, line in enumerate(lines):
        if i == 0:
            seeds = [int(x) for x in line.split(':')[1].split()]
            print(f'SEEDS: {seeds}')
            continue

        if line.strip() == '': continue

        if "map:" in line:
            type = line.split('-')[2].split()[0]
            match type:
                case 'soil': current_type = seeds_soil
                case 'fertilizer': current_type = soil_fert
                case 'water': current_type = fert_water
                case 'light': current_type = water_light
                case 'temperature': current_type = light_temp
                case 'humidity': current_type = temp_humid
                case 'location': current_type = humid_loc
        else:
            ranges = line.split()
            dest_range_start = int(ranges[0])
            source_range_start = int(ranges[1])
            range_len = int(ranges[2])
            current_type[(source_range_start, source_range_start + range_len)] = (dest_range_start, dest_range_start + range_len)

    print(f'SEEDS -> SOIL:              {seeds_soil}')
    print(f'SOIL -> FERTILIZER:         {soil_fert}')
    print(f'FERTILIZER -> WATER:        {fert_water}')
    print(f'WATER -> LIGHT:             {water_light}')
    print(f'LIGHT -> TEMPERATURE:       {light_temp}')
    print(f'TEMPERATURE -> HUMIDITY:    {temp_humid}')
    print(f'HUMIDITY -> LOCATION:       {humid_loc}')

    seed_locs = []

    for seed in seeds:
        next_map = ('ss', seeds_soil)
        current = seed
        trail = []
        for i in range(0, 7):
            trail += [current]
            current = find_next(current, next_map[1])
            match next_map[0]:
                case 'ss': next_map = ('sf', soil_fert)
                case 'sf': next_map = ('fw', fert_water)
                case 'fw': next_map = ('wl', water_light)
                case 'wl': next_map = ('lt', light_temp)
                case 'lt': next_map = ('th', temp_humid)
                case 'th': next_map = ('hl', humid_loc)
                case 'hl': trail += [current] 

        print(f'FINAL: {current}, TRAIL: {trail}')
        seed_locs += [current]

    print(min(seed_locs))

