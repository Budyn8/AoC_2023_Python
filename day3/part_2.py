before_line: str = ""
current_line: str = ""
next_line: str = ""


def get_multiply(curr_index: int):
    i = -1
    count = 0
    multiply = 1

    while i < 2:
        if before_line[curr_index + i].isnumeric():
            number = before_line[curr_index + i]
            j = 1
            while before_line[curr_index + i - j].isnumeric():
                number = before_line[curr_index + i - j] + number
                j += 1
            i += 1
            while before_line[curr_index + i].isnumeric():
                number += before_line[curr_index + i]
                i += 1
            number = int(number)
            count += 1
            multiply *= number
        i += 1

    i = -1
    while i < 2:
        if current_line[curr_index + i].isnumeric():
            number = current_line[curr_index + i]
            j = 1
            while current_line[curr_index + i - j].isnumeric():
                number = current_line[curr_index + i - j] + number
                j += 1
            i += 1
            while current_line[curr_index + i].isnumeric():
                number += current_line[curr_index + i]
                i += 1
            number = int(number)
            count += 1
            multiply *= number
        if count > 2:
            return 0
        i += 1
    i = -1
    while i < 2:
        if next_line[curr_index + i].isnumeric():
            number = next_line[curr_index + i]
            j = 1
            while next_line[curr_index + i - j].isnumeric():
                number = next_line[curr_index + i - j] + number
                j += 1
            i += 1
            while next_line[curr_index + i].isnumeric():
                number += next_line[curr_index + i]
                i += 1
            number = int(number)
            count += 1
            multiply *= number
        if count > 2:
            return 0
        i += 1
    if count == 2:
        return multiply
    return 0


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
            if current_line[curr_index] == "*":
                multiply = get_multiply(curr_index)
                if multiply > 0:
                    output += multiply
            curr_index += 1
        before_line = current_line
        current_line = next_line
        next_line = "." + file_desc.readline().replace("\n", ".")
        if next_line == ".":
            next_line = "." * len(current_line)
            count += 1
    print(output)
