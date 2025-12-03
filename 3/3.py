test_input = """987654321111111
811111111111119
234234234234278
818181911112111"""


def largest_number_in_line_index(line: str, batteries_remaining: int) -> int:
    largest = -1
    index = -1
    for i, char in enumerate(line):
        num = int(char)
        if num > largest and (
            len(line) - i > batteries_remaining
        ):  # Ensure there is a next character
            largest = num
            index = i
    return index


def part1(data: str) -> None:
    lines = data.split("\n")
    results: list[int] = []
    for line in lines:
        index = largest_number_in_line_index(line, 1)
        first = line[index]
        remaining = line[index + 1 :]
        second_index = largest_number_in_line_index(remaining, 0)
        second = remaining[second_index]
        results.append(int(f"{first}{second}"))

    print(sum(results))


def part2(data: str) -> None:

    batteries = 12

    lines = data.split("\n")
    results: list[int] = []
    for line in lines:
        switched: list[str] = []
        last_index = -1
        for batteries_remaining in range(batteries, 0, -1):
            remaining = line[last_index + 1 :]
            index = largest_number_in_line_index(remaining, batteries_remaining - 1)
            last_index = index + last_index + 1
            picked = line[last_index]
            switched.append(picked)

        results.append(int("".join(switched)))

    print(sum(results))


if __name__ == "__main__":
    part2(test_input)
    with open("3.txt") as f:
        data = f.read().strip()
        part1(data)
        part2(data)
