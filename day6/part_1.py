from math import ceil, sqrt


def calc_distance(time, time_max):
    return time * (time_max - time)


def calc_time(distance, time_max):
    delta = sqrt(time_max**2 - 4 * distance)
    times = [(time_max - delta) / 2, (time_max + delta) / 2]
    if times[0] == int(times[0]):
        times[0] += 1
    return ceil(max(times)) - ceil(min(times))


def calc_possibilities(data):
    for time in data:
        yield calc_time(time[1], time[0])


def parse_input():
    input = open("input", "r").read().split("\n")
    return [
        (int(time), int(distance))
        for time, distance in zip(
            input[0].split(":")[1].split(), input[1].split(":")[1].split()
        )
    ]


def product(array):
    if not array:
        return 1
    return array[0] * product(array[1:])


if __name__ == "__main__":
    times = list(calc_possibilities(parse_input()))
    print(times)
    print(product(times))
