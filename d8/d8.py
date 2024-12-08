def p1(input: str):
    lines = input.split("\n")

    antinodes: set[tuple[int, int]] = set()

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == ".":
                continue

            # Now look for matching chars
            for y, inner_line in enumerate(lines):
                for x, inner_char in enumerate(inner_line):
                    if inner_char != char:
                        continue

                    x_diff = x - j
                    y_diff = y - i

                    if (x_diff, y_diff) == (0, 0):
                        continue

                    if x < j:
                        new_x_1 = x - abs(x_diff)
                        new_x_2 = j + abs(x_diff)
                    else:
                        new_x_1 = x + abs(x_diff)
                        new_x_2 = j - abs(x_diff)

                    if y < i:
                        new_y_1 = y - abs(y_diff)
                        new_y_2 = i + abs(y_diff)
                    else:
                        new_y_1 = y + abs(y_diff)
                        new_y_2 = i - abs(y_diff)

                    # Check if the new position is valid
                    if 0 <= new_x_1 < len(lines) and 0 <= new_y_1 < len(lines):
                        antinodes.add((new_x_1, new_y_1))

                    if 0 <= new_x_2 < len(lines) and 0 <= new_y_2 < len(lines):
                        antinodes.add((new_x_2, new_y_2))

    return len(antinodes)


def safe_div(x: int, y: int) -> int:
    if y == 0:
        return 1
    return x // y


def p2(input: str):
    lines = input.split("\n")

    antinodes: set[tuple[int, int]] = set()

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == ".":
                continue

            # Now look for matching chars
            for y, inner_line in enumerate(lines):
                for x, inner_char in enumerate(inner_line):
                    if inner_char != char:
                        continue

                    x_diff = x - j
                    y_diff = y - i

                    if (x_diff, y_diff) == (0, 0):
                        continue

                    new_xs: list[int] = []
                    new_ys: list[int] = []

                    if x < j:
                        for n in range(0, safe_div(50, abs(x_diff)) + 1):
                            new_xs.append(x - (abs(x_diff) * n))
                            new_xs.append(j + (abs(x_diff) * n))
                    else:
                        for n in range(0, safe_div(50, abs(x_diff)) + 1):
                            new_xs.append(x + (abs(x_diff) * n))
                            new_xs.append(j - (abs(x_diff) * n))

                    if y < i:
                        for n in range(0, safe_div(50, abs(y_diff)) + 1):
                            new_ys.append(y - (abs(y_diff) * n))
                            new_ys.append(i + (abs(y_diff) * n))

                    else:
                        for n in range(0, safe_div(50, abs(y_diff)) + 1):
                            new_ys.append(y + (abs(y_diff) * n))
                            new_ys.append(i - (abs(y_diff) * n))

                    for new_x, new_y in zip(new_xs, new_ys):
                        if 0 <= new_x < len(lines) and 0 <= new_y < len(lines):
                            antinodes.add((new_x, new_y))

    return len(antinodes)


def main():
    with open("d8/input.txt") as f:
        input = f.read()

    test = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
