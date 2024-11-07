import part_1


def get_location(min_val, val_range, ranges):
    curr_min = 4294967296
    if not len(ranges):
        return min_val
    for range_var in ranges[0]:
        diff = min_val - range_var[1]
        if diff < 0:
            if val_range < -diff:
                return min(curr_min, get_location(min_val, val_range, ranges[1:]))
            curr_min = min(curr_min, get_location(min_val, -diff, ranges[1:]))
            min_val += -diff
            val_range -= -diff
        elif diff < range_var[2]:
            if val_range < range_var[2] - diff:
                return min(
                    curr_min, get_location(range_var[0] + diff, val_range, ranges[1:])
                )
            curr_min = min(
                curr_min,
                get_location(range_var[0] + diff, range_var[2] - diff, ranges[1:]),
            )
            min_val += range_var[2] - diff
            val_range -= range_var[2] - diff
    return min(curr_min, get_location(min_val, val_range, ranges[1:]))


def get_maps(data):
    seeds = sorted([(x, y) for x, y in zip(data[0][0::2], data[0][1::2])])
    for seed_range in seeds:
        yield get_location(seed_range[0], seed_range[1], data[1])


if __name__ == "__main__":
    out_maps = get_maps(part_1.parse_input(1))
    print(min(out_maps))
