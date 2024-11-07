kards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
kards.reverse()

joker_maps = (
    (0, 1, 3, 5, 6),
    (1, 3, 5, 6),
    (2, 4),
    (3, 5, 6),
    tuple([4]),
    (5, 6),
    tuple([6]),
)


def get_hand_type(hand):
    h_type = dict()
    for kard in hand[0]:
        if kard in h_type:
            h_type[kard] += 1
        else:
            h_type[kard] = 1
    jokers = ("J" in h_type.keys()) and h_type.pop("J") or 0

    temp = 1
    if len(h_type) != 0:
        temp = max(h_type.values())
    else:
        return ([6] + [kards.index("J") * 6], int(hand[1]))

    return (
        [
            joker_maps[
                (temp + 1) * (temp > 3)
                or (3 + (2 in h_type.values())) * (temp == 3)
                or (list(h_type.values()).count(2))
            ][jokers]
        ]
        + [kards.index(kard) for kard in hand[0]],
        int(hand[1]),
    )


def parse_input_data():
    input = open("./input", "r").read().split("\n")
    return [hand.split(" ") for hand in input if hand]


if __name__ == "__main__":
    sorted_hands = sorted([get_hand_type(hand) for hand in parse_input_data()])
    winnings = 0
    for rank, bid in enumerate(sorted_hands, 1):
        winnings += rank * bid[1]
    print(winnings)
