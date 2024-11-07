import part_1


def parse_input():
    input = open("input", "r").read().split("\n")
    return [[int(x.replace(" ", "").split(":")[1]) for x in input if x]]


if __name__ == "__main__":
    print(part_1.product(list(part_1.calc_possibilities(parse_input()))))
