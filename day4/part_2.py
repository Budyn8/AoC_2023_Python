if __name__ == "__main__":
    file_desc = open("./input", "r")
    a_table = [1] * 212
    index = 0
    for line in file_desc:
        val = 1
        inputs = line.split(":")[1].split("|")
        winners = [int(x) for x in inputs[0].split(" ") if x]
        mines = [int(x) for x in inputs[1].split(" ") if x]

        for num in mines:
            if num in winners:
                a_table[index + val] += a_table[index]
                val += 1
        index += 1

    print(sum(a_table))
