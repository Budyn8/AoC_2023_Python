def main():
    return


if __name__ == "__main__":
    output = 0
    file_desc = open("./input", "r")

    for line in file_desc:
        val = 1 / 2

        inputs = line.split(":")[1].split("|")
        winners = [int(x) for x in inputs[0].split(" ") if x]
        mines = [int(x) for x in inputs[1].split(" ") if x]

        for mine_num in mines:
            if mine_num in winners:
                val = val * 2
        output += val.__floor__()
    print(output)
