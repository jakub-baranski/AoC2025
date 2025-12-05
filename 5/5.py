test_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def part1(inp: str) -> None:
    ranges_inp, ingredients_inp = inp.split("\n\n")

    ingredients = [int(i) for i in ingredients_inp.split("\n")]
    ranges: list[tuple[int, int]] = []

    counter = 0

    for line in ranges_inp.split("\n"):
        start, stop = line.split("-")
        ranges.append((int(start), int(stop)))

    for i in ingredients:
        for r in ranges:
            if r[0] <= i <= r[1]:
                counter += 1
                break

    print(counter)


def part2(inp: str) -> None:
    ranges_inp, _ingredients_inp = inp.split("\n\n")

    ranges: list[tuple[int, int]] = []

    for line in ranges_inp.split("\n"):
        start, stop = line.split("-")
        ranges.append((int(start), int(stop)))

    # sort by start
    sorted_ranges = sorted(ranges, key=lambda r: r[0])

    joined_ranges = [sorted_ranges[0]]

    # join ranges
    for r in sorted_ranges[1:]:
        last_joined = joined_ranges[-1]
        if r[0] <= last_joined[1] and r[1] > last_joined[1]:
            joined_ranges[-1] = (last_joined[0], r[1])
        elif last_joined[1] < r[0]:
            joined_ranges.append(r)

    counter = 0
    for r in joined_ranges:
        counter += r[1] - r[0] + 1

    print(counter)


if __name__ == "__main__":

    with open("5.txt") as f:
        inp = f.read().strip()
        part1(inp)
        part2(inp)
