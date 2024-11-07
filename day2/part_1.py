import re

# part one

EXPECTED_ANWS = {"r": 12, "g": 13, "b": 14}


def parse_line(line: str):
    game = line.split(":")
    game_id = int(re.findall("1?[0-9][0-9]?", game[0])[0])
    losses = game[1]

    exp = "[0-9][0-9]? [r|g|b]"
    bruh = re.findall(exp, losses)

    max_values = {"r": 0, "g": 0, "b": 0}

    for find in bruh:
        value = find[0]
        if find[1] != " ":
            value += find[1]
        if max_values[find[-1]] < int(value):
            max_values[find[-1]] = int(value)

    for key in EXPECTED_ANWS.keys():
        if EXPECTED_ANWS[key] < max_values[key]:
            return 0
    return game_id


if __name__ == "__main__":
    output = 0
    input_file = open("input", "r")
    for line in input_file:
        output += parse_line(line)
    print(output)
