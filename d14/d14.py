import re


def get_robots(input: str) -> list[tuple[int, int, int, int]]:
    lines = input.split("\n")

    robots: list[tuple[int, int, int, int]] = []
    for line in lines:
        pos = re.search(r"p=(-?\d+),(-?\d+)", line)
        vel = re.search(r"v=(-?\d+),(-?\d+)", line)
        assert pos is not None and vel is not None
        robots.append(
            (int(pos.group(1)), int(pos.group(2)), int(vel.group(1)), int(vel.group(2)))
        )

    return robots


def simulate_robots(
    robots: list[tuple[int, int, int, int]], dimensions: tuple[int, int]
):
    for i, robot in enumerate(robots):
        new_x = robot[0] + robot[2]
        new_y = robot[1] + robot[3]

        # Wrap around
        if new_x >= dimensions[0]:
            new_x -= dimensions[0]
        elif new_x < 0:
            new_x += dimensions[0]

        if new_y >= dimensions[1]:
            new_y -= dimensions[1]
        elif new_y < 0:
            new_y += dimensions[1]

        robots[i] = (new_x, new_y, robot[2], robot[3])


def p1(input: str, test_mode: bool = False):
    dimensions = (101, 103)
    if test_mode:
        dimensions = (11, 7)

    robots = get_robots(input)

    for _ in range(100):
        simulate_robots(robots, dimensions)

    quadrant_1 = (0, 0, dimensions[0] // 2, dimensions[1] // 2)
    quadrant_2 = (dimensions[0] // 2 + 1, 0, dimensions[0], dimensions[1] // 2)
    quadrant_3 = (0, dimensions[1] // 2 + 1, dimensions[0] // 2, dimensions[1])
    quadrant_4 = (
        dimensions[0] // 2 + 1,
        dimensions[1] // 2 + 1,
        dimensions[0],
        dimensions[1],
    )

    quadrants = [quadrant_1, quadrant_2, quadrant_3, quadrant_4]

    acc = 1

    for quadrant in quadrants:
        q = 0
        for robot in robots:
            if (
                quadrant[0] <= robot[0] < quadrant[2]
                and quadrant[1] <= robot[1] < quadrant[3]
            ):
                q += 1

        acc *= q

    return acc


def count_robots_with_neighbors(robots: list[tuple[int, int, int, int]]) -> int:
    count = 0

    positions: set[tuple[int, int]] = set()

    for robot in robots:
        positions.add((robot[0], robot[1]))

    for robot in robots:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_x = robot[0] + dx
                new_y = robot[1] + dy
                if (new_x, new_y) in positions:
                    count += 1

    return count


def p2(text: str, test_mode: bool = False):
    dimensions = (101, 103)
    if test_mode:
        dimensions = (11, 7)

    robots = get_robots(text)

    iterations = 0

    while True:
        simulate_robots(robots, dimensions)

        num_neighbors = count_robots_with_neighbors(robots)

        if num_neighbors > 1500:
            print(f"Found potential tree at {iterations+1} seconds")
            space = [["." for _ in range(dimensions[0])] for _ in range(dimensions[1])]

            for x, y, _, _ in robots:
                if space[y][x] == ".":
                    space[y][x] = "1"
                else:
                    space[y][x] = str(int(space[y][x]) + 1)

            print("\n".join(["".join(row) for row in space]))
            print(num_neighbors)
            cont = input("\nKeep searching? (Y/n)")
            if cont == "n":
                break

        iterations += 1

    return iterations + 1


def main():
    with open("d14/input.txt") as f:
        input = f.read()

    test = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

    print(f"Part 1 test: {p1(test, True)}")
    print(f"Part 2 test: {p2(test, True)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
