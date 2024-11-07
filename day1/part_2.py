#!/home/budyn/projects/advent-of-code-2023/venv/bin/python3
numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def get_first(line):
    lowest_index = len(line)
    curr_number = 0
    for number in numbers:
        if number in line:
            curr_num_index = line.index(number)
            if curr_num_index < lowest_index:
                lowest_index = curr_num_index
                curr_number = numbers.index(number)

    for i in range(1, 10):
        if str(i) in line:
            curr_num_index = line.index(str(i))
            if curr_num_index < lowest_index:
                lowest_index = curr_num_index
                curr_number = i

    return curr_number


def get_last(line):
    lowest_index = -1
    curr_number = 0
    for number in numbers:
        if number in line:
            curr_num_index = line.rindex(number)
            if curr_num_index > lowest_index:
                lowest_index = curr_num_index
                curr_number = numbers.index(number)

    for i in range(1, 10):
        if str(i) in line:
            curr_num_index = line.rindex(str(i))
            if curr_num_index > lowest_index:
                lowest_index = curr_num_index
                curr_number = i

    return curr_number


if __name__ == "__main__":
    input_file = open("./input1", "r")
    output = 0
    for line in input_file.readlines():
        output += int(str(get_first(line)) + str(get_last(line)))
    print(output)
