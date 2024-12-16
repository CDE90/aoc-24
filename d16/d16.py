from typing import Any


def p1(input: str):
    grid = [[char for char in row] for row in input.split("\n") if row]

    start_pos = (-1, -1)
    end_pos = (-1, -1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                start_pos = (i, j)
            elif grid[i][j] == "E":
                end_pos = (i, j)

    print(start_pos, end_pos)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # visited = set()
    visited = {}

    # Queue of (pos, direction, current cost)
    # Initial direction is east (0, 1)
    queue: list[tuple[tuple[int, int], tuple[int, int], int, Any]] = [
        (start_pos, (0, 1), 0, None)
    ]

    best_cost = 10**10
    best_sol = None

    while queue:
        pos, direction, cost, parent = queue.pop(0)
        if (pos, direction) in visited:
            if cost >= visited[(pos, direction)]:
                continue
            # continue
        # visited.add((pos, direction))
        visited[(pos, direction)] = cost

        if pos == end_pos:
            if cost < best_cost:
                best_cost = cost
                best_sol = parent
            continue

        # We can go forwards, turn left (without moving) or turn right (without moving)
        forward = (pos[0] + direction[0], pos[1] + direction[1])
        if grid[forward[0]][forward[1]] != "#":
            queue.append((forward, direction, cost + 1, (pos, direction, cost, parent)))

        left_dir = directions[(directions.index(direction) - 1) % 4]
        queue.append((pos, left_dir, cost + 1000, (pos, direction, cost, parent)))
        right_dir = directions[(directions.index(direction) + 1) % 4]
        queue.append((pos, right_dir, cost + 1000, (pos, direction, cost, parent)))

    print(best_sol)

    child = best_sol
    while child:
        grid[child[0][0]][child[0][1]] = "X"
        child = child[3]

    print("\n".join(["".join(row) for row in grid]))

    return best_cost


def p2(input: str):
    grid = [[char for char in row] for row in input.split("\n") if row]

    start_pos = (-1, -1)
    end_pos = (-1, -1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                start_pos = (i, j)
            elif grid[i][j] == "E":
                end_pos = (i, j)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    visited: dict[tuple[int, int, int], int] = {}

    # Queue of (pos, direction, current cost)
    # Initial direction is east (0, 1)
    queue: list[tuple[int, int, int, int, Any]] = [
        (start_pos[0], start_pos[1], 0, 0, None)
    ]

    best_cost = 10**10
    best_sols = []

    while queue:
        x, y, dir, cost, parent = queue.pop(0)

        if cost > best_cost:
            continue

        if (x, y, dir) in visited:
            if cost > visited[(x, y, dir)]:
                continue
        visited[(x, y, dir)] = cost

        if (x, y) == end_pos:
            if cost < best_cost:
                best_cost = cost
                best_sols = [(x, y, parent)]
            elif cost == best_cost:
                best_sols.append((x, y, parent))
            continue

        d = directions[dir]

        # We can go forwards, turn left (without moving) or turn right (without moving)
        if grid[x + d[0]][y + d[1]] != "#":
            queue.append((x + d[0], y + d[1], dir, cost + 1, (x, y, parent)))

        l_dir = (dir - 1) % 4
        r_dir = (dir + 1) % 4

        queue.append((x, y, l_dir, cost + 1000, (x, y, parent)))
        queue.append((x, y, r_dir, cost + 1000, (x, y, parent)))

    print(len(best_sols))

    good_tiles = set()

    for sol in best_sols:
        child = sol
        while child:
            good_tiles.add((child[0], child[1]))
            child = child[2]

    for pos in good_tiles:
        grid[pos[0]][pos[1]] = "O"

    print("\n".join(["".join(row) for row in grid]))

    return len(good_tiles)


def main():
    with open("d16/input.txt") as f:
        input = f.read()

    test = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

    #     test = """#################
    # #...#...#...#..E#
    # #.#.#.#.#.#.#.#.#
    # #.#.#.#...#...#.#
    # #.#.#.#.###.#.#.#
    # #...#.#.#.....#.#
    # #.#.#.#.#.#####.#
    # #.#...#.#.#.....#
    # #.#.#####.#.###.#
    # #.#.#.......#...#
    # #.#.###.#####.###
    # #.#.#...#.....#.#
    # #.#.#.#####.###.#
    # #.#.#.........#.#
    # #.#.#.#########.#
    # #S#.............#
    # #################
    # """

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
