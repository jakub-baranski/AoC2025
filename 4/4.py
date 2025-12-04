test_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def count_neighbour_rolls(data: list[list[str]], row: int, col: int) -> int:
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(data) and 0 <= c < len(data[0]):
            if data[r][c] == "@":
                count += 1

    return count


def part1(input: str) -> None:

    lines = input.split("\n")
    data = [list(line) for line in lines]
    rolls = 0

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "@":
                neightbours = count_neighbour_rolls(data, i, j)
                if neightbours <= 3:
                    rolls += 1

    print(rolls)


def part2(input: str) -> None:
    lines = input.split("\n")
    data = [list(line) for line in lines]
    rolls = 0

    while True:
        removed = 0
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] == "@":
                    neightbours = count_neighbour_rolls(data, i, j)
                    if neightbours <= 3:
                        rolls += 1
                        data[i][j] = "."
                        removed += 1
        if removed == 0:
            break

    print(rolls)


if __name__ == "__main__":
    with open("4.txt") as f:
        data = f.read().strip()
        part1(data)
        part2(data)
