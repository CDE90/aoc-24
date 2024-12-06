def get_visited_cells(conv_lines: list[list[bool]], start_pos: tuple[int, int]):
    # up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dimensions = len(conv_lines), len(conv_lines[0])
    guard_pos = start_pos
    curr_direction = (-1, 0)

    visited = {(guard_pos, curr_direction)}

    while True:
        # Move the guard forward, unless there is a blockage
        new_pos = (
            guard_pos[0] + curr_direction[0],
            guard_pos[1] + curr_direction[1],
        )

        if (
            new_pos[0] < 0
            or new_pos[0] >= dimensions[0]
            or new_pos[1] < 0
            or new_pos[1] >= dimensions[1]
        ):
            break

        if not conv_lines[new_pos[0]][new_pos[1]]:
            guard_pos = new_pos

            if (guard_pos, curr_direction) not in visited:
                visited.add((guard_pos, curr_direction))
            else:
                break

        else:
            # Move the guard 90 degrees right
            curr_direction = directions[(directions.index(curr_direction) + 1) % 4]

    return visited


def p1(input: str):
    lines = [line for line in input.split("\n") if line]

    start_pos = (0, 0)

    # Find the guard position
    for l_idx, line in enumerate(lines):
        for c_idx, char in enumerate(line):
            if char == "^":
                start_pos = (l_idx, c_idx)
                break

    # Convert the lines into a list of lists of booleans (True if blocked)
    conv_lines = [[c == "#" for c in line] for line in lines]

    visited = get_visited_cells(conv_lines, start_pos)

    cells_visited = set()
    for (l_idx, b_idx), _ in visited:
        cells_visited.add((l_idx, b_idx))

    return len(cells_visited)


def p2(input: str):
    lines = [line for line in input.split("\n") if line]

    start_pos = (0, 0)

    # Find the guard position
    for l_idx, line in enumerate(lines):
        for c_idx, char in enumerate(line):
            if char == "^":
                start_pos = (l_idx, c_idx)
                break

    # Convert the lines into a list of lists of booleans (True if blocked)
    conv_lines = [[c == "#" for c in line] for line in lines]

    acc = 0

    dimensions = len(conv_lines), len(conv_lines[0])

    # up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def is_stuck(inner_lines: list[list[bool]]):
        guard_pos = start_pos
        curr_direction = (-1, 0)

        visited = {(guard_pos, curr_direction)}

        while True:
            # Move the guard forward, unless there is a blockage
            new_pos = (
                guard_pos[0] + curr_direction[0],
                guard_pos[1] + curr_direction[1],
            )

            if (
                new_pos[0] < 0
                or new_pos[0] >= dimensions[0]
                or new_pos[1] < 0
                or new_pos[1] >= dimensions[1]
            ):
                return False

            if not inner_lines[new_pos[0]][new_pos[1]]:
                guard_pos = new_pos

                if (guard_pos, curr_direction) not in visited:
                    visited.add((guard_pos, curr_direction))
                else:
                    return True

            else:
                # Move the guard 90 degrees right
                curr_direction = directions[(directions.index(curr_direction) + 1) % 4]

    # Run the simulation once, and get a list of visited positions
    visited = get_visited_cells(conv_lines, start_pos)

    print(len(visited))

    cell_visited = set()
    for (l_idx, b_idx), _ in visited:
        cell_visited.add((l_idx, b_idx))

    for l_idx, b_idx in cell_visited:
        blocked = conv_lines[l_idx][b_idx]

        if not blocked:
            conv_lines[l_idx][b_idx] = True
        elif (l_idx, b_idx) == start_pos:
            continue
        else:
            continue

        # Check if the guard is stuck
        if is_stuck(conv_lines):
            acc += 1

        conv_lines[l_idx][b_idx] = False

    return acc


def main():
    with open("d6/input.txt") as f:
        input = f.read()

    test = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
