def p1(input: str):
    lines = [line for line in input.split("\n") if line]
    grid: list[list[int]] = [[int(char) for char in line] for line in lines]

    acc = 0

    for lidx, line in enumerate(grid):
        for cidx, num in enumerate(line):
            if num == 0:
                explored: set[tuple[int, int]] = set()
                frontier: list[tuple[int, int]] = [(cidx, lidx)]
                found = 0
                while frontier:
                    curr = frontier.pop()
                    if curr in explored:
                        continue
                    explored.add(curr)
                    if grid[curr[1]][curr[0]] == 9:
                        found += 1
                        continue
                    frontier.extend(
                        [
                            (nx, ny)
                            for (nx, ny) in [
                                (curr[0] + dx, curr[1] + dy)
                                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]
                            ]
                            if nx >= 0
                            and ny >= 0
                            and nx < len(grid)
                            and ny < len(grid[0])
                            and grid[ny][nx] == grid[curr[1]][curr[0]] + 1
                        ]
                    )

                acc += found

    return acc


def explore_neighbors(
    x: int,
    y: int,
    grid: list[list[int]],
    path: list[tuple[int, int]],
    explored_paths: set[tuple[tuple[int, int], ...]],
) -> int:
    valid = 0

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
            continue

        curr_num = grid[y][x]
        new_num = grid[ny][nx]

        if new_num == curr_num + 1 and new_num == 9:
            valid += 1

        elif new_num == curr_num + 1:
            new_path = path.copy()
            new_path.append((nx, ny))
            if tuple(new_path) not in explored_paths:
                explored_paths.add(tuple(new_path))
                valid += explore_neighbors(nx, ny, grid, new_path, explored_paths)

    return valid


def p2(input: str):
    lines = [line for line in input.split("\n") if line]
    grid: list[list[int]] = [[int(char) for char in line] for line in lines]

    paths: set[tuple[tuple[int, int], ...]] = set()
    acc = 0

    for lidx, line in enumerate(grid):
        for cidx, num in enumerate(line):
            if num == 0:
                n_valid = explore_neighbors(cidx, lidx, grid, [(cidx, lidx)], paths)
                acc += n_valid

    return acc


def main():
    with open("d10/input.txt") as f:
        input = f.read()

    test = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
