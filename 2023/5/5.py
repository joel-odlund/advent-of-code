
input = open("input.txt", "r").read().split("\n")
seeds = [int(seed) for seed in (input[0].split(":")[1].split())]
#seeds = seeds[:1]

def split(list, separator=""):
    sublist = []
    for item in list:
        if item == separator and sublist:
            yield sublist
            sublist = []
        else:
            sublist.append(item)
    if sublist:
        yield sublist

maps = [[tuple(map(int, sm.split())) for sm in m[1:]] for m in (list(split(input[2:])))]


def single_map(value, mapdefs):
    if not mapdefs:
        return value
    target_range, source_range, range_size = mapdefs[0]
    if value >= source_range and value < source_range + range_size:
        f = value + target_range - source_range
        return f
    else:
        return single_map(value, mapdefs[1:])

def multi_map(value, maps):
    for map in maps:

        value = single_map(value, map)
    return value

def part_1(seeds, maps):
    return min([multi_map(seed,maps) for seed in seeds])


print('part 1', part_1(seeds, maps))

def map_level(input_range, mapdefs):
    if not mapdefs:
        yield input_range
        return

    target_range_start, source_range_start, range_size = mapdefs[0]
    source_range_end = source_range_start + range_size

    mapping_delta = target_range_start - source_range_start

    input_range_start, input_range_end = input_range

    ## an input range can be mapped to up to three ranges
    ## |-----left_side---|----inside---|---right---|

    if input_range_start < source_range_start:
        left_range = (input_range_start, min(input_range_end, source_range_start))
        yield from map_level(left_range, mapdefs[1:])
    if input_range_end > source_range_start and input_range_start < source_range_end:
        inside_range  = (max(source_range_start, input_range_start), min(source_range_end, input_range_end))
        mapped_range = inside_range[0] + mapping_delta, inside_range[1] + mapping_delta
        yield mapped_range
    if input_range_end > source_range_end:
        right_range = (max(input_range_start, source_range_end), input_range_end)
        yield from map_level(right_range, mapdefs[1:])

def recursive_map_all():
    ranges = [(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds) -1, 2 )]
    out = []
    for r in ranges:
        mapped = [r]
        for i, level in enumerate(maps):
            mapped = sum([list(map_level(x, level)) for x in mapped], start=[])
        out += mapped

    return out

lowest = min(recursive_map_all())[0]
print("part 2", lowest)




#%%
