import re


def parse_line2(line: str):
    game = line.split(":")
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

    power = 1
    for value in max_values.values():
        power *= value

    return power


if __name__ == "__main__":
    output = 0
    input_file = open("input", "r")
    for line in input_file:
        output += parse_line2(line)
    print(output)
