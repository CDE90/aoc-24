def find_path(grid: list[list[bool]], size: int) -> list[tuple[int, int]] | None:
    visited: set[tuple[int, int]] = set()
    queue: list[tuple[int, int, list[tuple[int, int]]]] = [(0, 0, [])]

    while queue:
        x, y, path = queue.pop(0)

        if (x, y) in visited or grid[x][y]:
            continue

        visited.add((x, y))
        path.append((x, y))

        if x == size and y == size:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= size and 0 <= ny <= size and not grid[nx][ny]:
                queue.append((nx, ny, path.copy()))

    return None


def p1(input: str, test_mode: bool = False):
    if test_mode:
        size = 6
        num = 12
    else:
        size = 70
        num = 1024

    input = input.strip()
    positions = [
        (int(pos.split(",")[0]), int(pos.split(",")[1])) for pos in input.split("\n")
    ]

    # False for not corrupted, True for corrupted
    grid = [[False for _ in range(size + 1)] for _ in range(size + 1)]

    for i in range(num):
        x, y = positions[i]
        grid[x][y] = True

    path = find_path(grid, size)

    if path is None:
        return "IMPOSSIBLE"

    return len(path) - 1


def p2(input: str, test_mode: bool = False):
    if test_mode:
        size = 6
    else:
        size = 70

    input = input.strip()
    positions = [
        (int(pos.split(",")[0]), int(pos.split(",")[1])) for pos in input.split("\n")
    ]

    # False for not corrupted, True for corrupted
    grid = [[False for _ in range(size + 1)] for _ in range(size + 1)]

    prev_path = None

    for i in range(len(positions)):
        x, y = positions[i]
        grid[x][y] = True

        if prev_path and (x, y) not in prev_path:
            continue

        path = find_path(grid, size)

        if path is None:
            return f"{x},{y}"

        prev_path = set(path)


def main():
    with open("d18/input.txt") as f:
        input = f.read()

    test = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""

    print(f"Part 1 test: {p1(test, True)}")
    print(f"Part 2 test: {p2(test, True)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
