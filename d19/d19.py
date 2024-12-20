from functools import cache

from tqdm import tqdm


def num_possible(pattern: str, available: tuple[str, ...]) -> int:
    @cache
    def inner_func(pos: int) -> int:
        # Base case: if we've matched the entire pattern
        if pos == len(pattern):
            return 1

        # Try each available string at the current position
        return sum(
            int(pattern.startswith(a, pos) and inner_func(pos + len(a)))
            for a in available
        )

    return inner_func(0)


def p1(input: str):
    available = tuple(input.strip().split("\n\n")[0].split(", "))

    required = input.strip().split("\n\n")[1].split("\n")

    acc = 0

    for r in tqdm(required):
        if num_possible(r, available):
            acc += 1

    return acc


def p2(input: str):
    available = tuple(input.strip().split("\n\n")[0].split(", "))

    required = input.strip().split("\n\n")[1].split("\n")

    acc = 0

    for r in tqdm(required):
        n = num_possible(r, available)
        if n:
            acc += n

    return acc


def main():
    with open("d19/input.txt") as f:
        input = f.read()

    test = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
