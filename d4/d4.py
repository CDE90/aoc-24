def p1(input: str):
    lines = input.split("\n")

    acc = 0
    directions = [
        (0, 1),  # right
        (0, -1),  # left
        (-1, 0),  # up
        (1, 0),  # down
        (-1, -1),  # up-left
        (-1, 1),  # up-right
        (1, -1),  # down-left
        (1, 1),  # down-right
    ]

    for line_idx, line in enumerate(lines):
        for char_idx, char in enumerate(line):
            if char == "X":
                for dx, dy in directions:
                    try:
                        positions = [
                            (line_idx + i * dx, char_idx + i * dy) for i in range(1, 4)
                        ]

                        if any(
                            pos[0] < 0
                            or pos[0] >= len(lines)
                            or pos[1] < 0
                            or pos[1] >= len(lines[pos[0]])
                            for pos in positions
                        ):
                            continue

                        # Check for "MAS" pattern
                        if all(
                            lines[pos[0]][pos[1]] == letter
                            for pos, letter in zip(positions, ["M", "A", "S"])
                        ):
                            acc += 1

                    except IndexError:
                        continue

    return acc


def p2(input: str):
    lines = input.split("\n")

    acc = 0

    for line_idx, line in enumerate(lines):
        for char_idx, char in enumerate(line):
            if char == "A":
                if any(
                    pos < 0 or pos >= len(line)
                    for pos in [line_idx - 1, char_idx - 1, line_idx + 1, char_idx + 1]
                ):
                    continue

                top_left = lines[line_idx - 1][char_idx - 1]
                top_right = lines[line_idx - 1][char_idx + 1]
                bottom_left = lines[line_idx + 1][char_idx - 1]
                bottom_right = lines[line_idx + 1][char_idx + 1]

                if (
                    top_left == "M"
                    and bottom_right == "S"
                    or top_left == "S"
                    and bottom_right == "M"
                ) and (
                    top_right == "M"
                    and bottom_left == "S"
                    or top_right == "S"
                    and bottom_left == "M"
                ):
                    acc += 1

    return acc


def main():
    with open("d4/input.txt") as f:
        input = f.read()

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")

    test = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")


if __name__ == "__main__":
    main()
