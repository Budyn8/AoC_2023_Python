g_double_array = []

before_line = ""
current_line = ""
next_line = ""

symbols = [
    "*",
    "%",
    "$",
    "/",
    "#",
    "@",
    "&",
    "=",
    "+",
    "-",
]


def is_symbol(charcter):
    if charcter in symbols:
        return True
    return False


def check_for_symbol(curr_index, curr_number):
    for char in before_line[curr_index - len(curr_number) - 1 : curr_index + 1]:
        if char in symbols:
            return True

    for char in current_line[curr_index - len(curr_number) - 1 : curr_index + 1]:
        if char in symbols:
            return True

    for char in next_line[curr_index - len(curr_number) - 1 : curr_index + 1]:
        if char in symbols:
            return True

    return False


if __name__ == "__main__":
    output = 0

    file_desc = open("./input", "r")

    current_line = "." + file_desc.readline().replace("\n", ".")
    line_len = len(current_line)
    before_line = "." * (line_len)
    next_line = "." + file_desc.readline().replace("\n", ".")

    count = 0

    while count != 2:
        curr_index = 1
        while curr_index < line_len - 1:
            curr_number = "0"
            while current_line[curr_index].isnumeric():
                curr_number += current_line[curr_index]
                curr_index += 1
            curr_number = int(curr_number)
            if curr_number > 0:
                if check_for_symbol(curr_index, str(curr_number)):
                    output += curr_number
                continue
            curr_index += 1
        before_line = current_line
        current_line = next_line
        next_line = "." + file_desc.readline().replace("\n", ".")
        if next_line == ".":
            next_line = "." * len(current_line)
            count += 1
    print(output)
