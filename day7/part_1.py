kards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
kards.reverse()


def get_hand_type(hand):
    h_type = dict()
    for kard in hand[0]:
        if kard in h_type:
            h_type[kard] += 1
        else:
            h_type[kard] = 1
    temp = max(h_type.values())
    return (
        [
            (temp + 1) * (temp > 3)
            or (3 + (2 in h_type.values())) * (temp == 3)
            or (list(h_type.values()).count(2))
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
