test_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def part1(data: str) -> None:
    lines = data.split("\n")

    initial = 50
    counter = 0

    for instruction in lines:
        turn = instruction[0]
        value = int(instruction[1:])

        if turn == "L":
            initial -= value
        else:
            initial += value

        value = initial % 100
        if value == 0:
            counter += 1

    print(counter)


def part2(data: str) -> None:
    """
    I feel dirty...
    """

    lines = data.split("\n")

    current = 50
    counter = 0

    for instruction in lines:
        turn = instruction[0]
        value = int(instruction[1:])

        for _ in range(value):
            if current == 0:
                counter += 1
            if turn == "L":
                current -= 1
            else:
                current += 1
            current = current % 100

    print(int(counter))


if __name__ == "__main__":
    with open("1.txt") as f:
        data = f.read().strip()
        part1(data)
        part2(data)
