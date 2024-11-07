def get_location(curr_index, maps):
    if not len(maps):
        return curr_index
    for c_map in maps[0]:
        diff = curr_index - c_map[1]
        if diff in range(0, c_map[2] + 1):
            return get_location(c_map[0] + diff, maps[1:])
    return get_location(curr_index, maps[1:])


def map_seeds(data):
    for seed in data[0]:
        yield [get_location(seed, data[1]), seed]


def parse_input(sort_by_index):
    inputs = open("./input", "r").read().split("\n\n")
    seeds = [*map(int, inputs.pop(0).split(" ")[1:])]
    data = [
        sorted(
            [[*map(int, i.split(" "))] for i in row.split("\n")[1:] if i],
            key=lambda i_range: i_range[sort_by_index],
        )
        for row in inputs
    ]
    return seeds, data


if __name__ == "__main__":
    out_map = map_seeds(parse_input(0))
    print(min(out_map)[0])
