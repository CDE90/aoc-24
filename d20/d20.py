from collections import deque


def get_distances(
    start_pos: tuple[int, int], grid: list[list[str]]
) -> dict[tuple[int, int], float]:
    distances: dict[tuple[int, int], float] = {}
    queue = deque([(start_pos, 0)])
    seen = {start_pos}

    while queue:
        pos, dist = queue.popleft()
        distances[pos] = dist

        # Check all adjacent positions
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = pos[0] + dx, pos[1] + dy
            new_pos = (new_x, new_y)

            if (
                0 <= new_y < len(grid)
                and 0 <= new_x < len(grid[0])
                and grid[new_y][new_x] != "#"
                and new_pos not in seen
            ):
                seen.add(new_pos)
                queue.append((new_pos, dist + 1))

    return distances


def manhattan_distance(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


def find_shortcuts(
    max_length: int,
    start_pos: tuple[int, int],
    end_pos: tuple[int, int],
    grid: list[list[str]],
    test_mode: bool = False,
) -> int:
    min_shortcut = 1 if test_mode else 100

    # Get distances from start and end
    start_distances = get_distances(start_pos, grid)
    end_distances = get_distances(end_pos, grid)

    normal_dist = start_distances[end_pos]
    height, width = len(grid), len(grid[0])
    acc = 0

    # Pre-calculate reachable positions
    reachable_positions = set(start_distances.keys()) & set(end_distances.keys())

    # Process each starting point
    for pos1 in reachable_positions:
        y1, x1 = pos1[1], pos1[0]
        start_dist = start_distances[pos1]

        # Skip if this starting point can't lead to a valid shortcut
        if start_dist >= normal_dist - min_shortcut:
            continue

        # Calculate bounds for the second portal position
        y_min = max(0, y1 - max_length)
        y_max = min(height - 1, y1 + max_length)

        for y2 in range(y_min, y_max + 1):
            y_range = max_length - abs(y2 - y1)
            if y_range < 0:
                continue

            x_min = max(0, x1 - y_range)
            x_max = min(width - 1, x1 + y_range)

            for x2 in range(x_min, x_max + 1):
                pos2 = (x2, y2)

                # Skip if position is not reachable
                if pos2 not in reachable_positions:
                    continue

                portal_steps = manhattan_distance(pos1, pos2)
                total_dist = start_dist + portal_steps + end_distances[pos2]

                if normal_dist - total_dist >= min_shortcut:
                    acc += 1

    return acc


def p1(input: str, test_mode: bool = False):
    grid = [[char for char in line] for line in input.strip().split("\n")]

    start_pos = (-1, -1)
    end_pos = (-1, -1)

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "S":
                start_pos = (j, i)
            elif cell == "E":
                end_pos = (j, i)

    return find_shortcuts(2, start_pos, end_pos, grid, test_mode)


def p2(input: str, test_mode: bool = False):
    grid = [[char for char in line] for line in input.strip().split("\n")]

    start_pos = (-1, -1)
    end_pos = (-1, -1)

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "S":
                start_pos = (j, i)
            elif cell == "E":
                end_pos = (j, i)

    return find_shortcuts(20, start_pos, end_pos, grid, test_mode)


def main():
    with open("d20/input.txt") as f:
        input = f.read()

    test = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""

    print(f"Part 1 test: {p1(test, True)}")
    print(f"Part 2 test: {p2(test, True)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
