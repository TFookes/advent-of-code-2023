from pprint import pprint
import sys

def find_next(current, almamap):
    #print(current, almamap.keys())
    for ranges in almamap.keys():
        if current in range(ranges[0], ranges[1]): 
            return almamap[ranges][0] + (current - ranges[0])
        
    return current


def check_seed_exists(seed, seeds, loc):
    for seed_ranges in seeds:
        if seed in range(int(seed_ranges[0]), int(seed_ranges[0]) + int(seed_ranges[1])):
            print(f'YAY! {current} - {loc}')
            return True
    

if __name__ == "__main__":
    with open("./inputs.txt", "r") as inputs:
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
            print('Computing Seeds')
            nums = line.split(':')[1].split()
            for j, num in enumerate(nums):
                if j >= len(nums) - 1: continue
                if j == 0 or j % 2 == 0:
                    seeds += [(nums[j], nums[j+1])]

            print(seeds)      
            print('Seeds computed')
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
            #current_type[(source_range_start, source_range_start + range_len)] = (dest_range_start, dest_range_start + range_len)
            current_type[(dest_range_start, dest_range_start + range_len)] = (source_range_start, source_range_start + range_len)

    '''
    print(f'SEEDS -> SOIL:              {seeds_soil}')
    print(f'SOIL -> FERTILIZER:         {soil_fert}')
    print(f'FERTILIZER -> WATER:        {fert_water}')
    print(f'WATER -> LIGHT:             {water_light}')
    print(f'LIGHT -> TEMPERATURE:       {light_temp}')
    print(f'TEMPERATURE -> HUMIDITY:    {temp_humid}')
    print(f'HUMIDITY -> LOCATION:       {humid_loc}')
    '''
    
    seed_locs = []
    i = 0      
    previous_i = 0 
    while True:
        print(i)
        next_map = ('hl', humid_loc)
        current = i
        found = False
        for j in range(0, 7):
            current = find_next(current, next_map[1])
            match next_map[0]:
                case 'hl': next_map = ('th', temp_humid)
                case 'th': next_map = ('lt', light_temp)
                case 'lt': next_map = ('wl', water_light)
                case 'wl': next_map = ('fw', fert_water)
                case 'fw': next_map = ('sf', soil_fert)
                case 'sf': next_map = ('ss', seeds_soil)
                case 'ss': found = check_seed_exists(current, seeds, i) 

        if found:
            for x in range(previous_i, i + 1):
                next_map = ('hl', humid_loc)
                found_lower = False
                potential = x
                print(x)
                for y in range(0, 7):
                    potential = find_next(potential, next_map[1])
                    match next_map[0]:
                        case 'hl': next_map = ('th', temp_humid)
                        case 'th': next_map = ('lt', light_temp)
                        case 'lt': next_map = ('wl', water_light)
                        case 'wl': next_map = ('fw', fert_water)
                        case 'fw': next_map = ('sf', soil_fert)
                        case 'sf': next_map = ('ss', seeds_soil)
                        case 'ss': 
                            found_lower = check_seed_exists(potential, seeds, x) 

                    if found_lower: 
                        print(f'YAY! {potential} - {x}')
                        sys.exit(1)

        previous_i = i
        i = i + 100000
                