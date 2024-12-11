from functools import cache


@cache
def process_stone(stone: int) -> tuple[int, ...]:
    if stone == 0:
        return (1,)

    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        mid = len(str_stone) // 2
        first_half = str_stone[:mid]
        second_half = str_stone[mid:]
        return int(first_half), int(second_half)

    return (stone * 2024,)


def blink(counts: dict[int, int]) -> dict[int, int]:
    new_counts: dict[int, int] = {}
    for k, v in counts.items():
        for s in process_stone(k):
            new_counts[s] = new_counts.get(s, 0) + v

    return new_counts


def p1(input: str):
    stones = [int(x) for x in input.split(" ") if x]

    counts: dict[int, int] = {}
    for s in stones:
        counts[s] = counts.get(s, 0) + 1

    for _ in range(25):
        counts = blink(counts)

    return sum(counts.values())


def p2(input: str):
    stones = [int(x) for x in input.split(" ") if x]

    counts: dict[int, int] = {}
    for s in stones:
        counts[s] = counts.get(s, 0) + 1

    for _ in range(75):
        counts = blink(counts)

    return sum(counts.values())


def main():
    with open("d11/input.txt") as f:
        input = f.read()

    # test = """0 1 10 99 999"""
    test = "125 17"

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
