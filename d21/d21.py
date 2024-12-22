from collections import deque
from functools import cache
from itertools import pairwise

# NUMERIC KEYPAD
# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

# DIRECTIONAL KEYPAD
#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

# Encodes the keypads as dictionaries of buttons, and neighboring buttons
NUMERIC_PAD = {
    "0": [("2", "^"), ("A", ">")],
    "1": [("2", ">"), ("4", "^")],
    "2": [("0", "v"), ("1", "<"), ("3", ">"), ("5", "^")],
    "3": [("2", "<"), ("6", "^"), ("A", "v")],
    "4": [("1", "v"), ("5", ">"), ("7", "^")],
    "5": [("2", "v"), ("4", "<"), ("6", ">"), ("8", "^")],
    "6": [("3", "v"), ("5", "<"), ("9", "^")],
    "7": [("4", "v"), ("8", ">")],
    "8": [("5", "v"), ("7", "<"), ("9", ">")],
    "9": [("6", "v"), ("8", "<")],
    "A": [("0", "<"), ("3", "^")],
}

DIRECTIONAL_PAD = {
    "^": [("A", ">"), ("v", "v")],
    "<": [("v", ">")],
    "v": [("<", "<"), ("^", "^"), (">", ">")],
    ">": [("v", "<"), ("A", "^")],
    "A": [("^", "<"), (">", "v")],
}

PADS = [NUMERIC_PAD, DIRECTIONAL_PAD]


def find_shortest_paths(start: str, end: str, pad: dict) -> list[str]:
    """Find all shortest paths between two buttons on a keypad"""

    queue: deque[tuple[str, list[str]]] = deque([(start, [])])
    seen = {start}
    shortest = None
    paths = []

    while queue:
        current, path = queue.popleft()

        if current == end:
            if shortest is None:
                shortest = len(path)
            if len(path) == shortest:
                paths.append("".join(path + ["A"]))
            continue

        if shortest and len(path) >= shortest:
            continue

        for next_button, direction in pad[current]:
            seen.add(next_button)
            queue.append((next_button, path + [direction]))

    return paths


@cache
def calculate_sequence_length(sequence: str, depth: int, pad_index: int = 0) -> int:
    """
    Calculate minimum sequence length needed at given depth
    pad_index: 0 for numeric pad, 1 for directional pad
    """

    pad = PADS[pad_index]
    total_length = 0

    # Add 'A' at start because robots start at 'A' position
    sequence = "A" + sequence

    # Process each pair of consecutive characters
    for current, next_char in pairwise(sequence):
        # Find all shortest paths between these buttons
        paths = find_shortest_paths(current, next_char, pad)

        if depth == 0:
            # Base case: just take shortest path length
            total_length += min(map(len, paths))
        else:
            # Recursive case: find minimum length needed for each possible path
            total_length += min(
                calculate_sequence_length(path, depth - 1, 1) for path in paths
            )

    return total_length


def p1(input: str):
    codes = input.strip().split("\n")
    return sum(calculate_sequence_length(code, 2) * int(code[:3]) for code in codes)


def p2(input: str):
    codes = input.strip().split("\n")
    return sum(calculate_sequence_length(code, 25) * int(code[:3]) for code in codes)


def main():
    with open("d21/input.txt") as f:
        input = f.read()

    test = """029A
980A
179A
456A
379A
"""

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
