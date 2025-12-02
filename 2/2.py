test_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""


def get_ranges(input: str) -> list[tuple[int, ...]]:
    return [tuple(map(int, r.split("-"))) for r in input.strip().split(",")]


def part1(input: str) -> None:
    ranges = get_ranges(input)
    summed = 0

    for start, end in ranges:
        for i in range(start, end + 1):
            stringed = str(i)
            if stringed[: len(stringed) // 2] == stringed[len(stringed) // 2 :]:
                summed += i

    print(summed)


def part2(input: str) -> None:
    ranges = get_ranges(input)
    summed = 0
    # Use \1 to refer to the first captured group, and {1,} to indicate it repeats at least twice
    regex_repeating_twice = r"^(\d+)\1{1,}$"

    import re

    for start, end in ranges:
        for i in range(start, end + 1):
            stringed = str(i)
            if re.search(regex_repeating_twice, stringed):
                summed += i

    print(summed)


if __name__ == "__main__":
    with open("2.txt") as f:
        data = f.read().strip()
        part1(data)
        part2(data)
