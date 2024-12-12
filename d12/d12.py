from dataclasses import dataclass


def p1(input: str):
    data = [[char for char in row] for row in input.split("\n") if row]

    explored_cells: set[tuple[int, int]] = set()
    acc = 0

    for r_idx, row in enumerate(data):
        for c_idx, cell in enumerate(row):
            if (r_idx, c_idx) in explored_cells:
                continue

            perimeter, area = explore_neighbors(data, r_idx, c_idx, explored_cells)

            # print(f"Perimeter: {perimeter}, Area: {area}, {cell}, {r_idx}, {c_idx}")

            acc += perimeter * area

    return acc


def explore_neighbors(
    data: list[list[str]], r_idx: int, c_idx: int, explored_cells: set[tuple[int, int]]
) -> tuple[int, int]:
    # If this cell has already been explored, return 0 for both perimeter and area
    if (r_idx, c_idx) in explored_cells:
        return 0, 0

    # Mark this cell as explored
    explored_cells.add((r_idx, c_idx))

    # Initialize perimeter and area
    perimeter = 0
    area = 1  # Start with 1 to count the current cell

    # Check all 4 neighboring cells
    for r_offset, c_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        r = r_idx + r_offset
        c = c_idx + c_offset

        # Skip if out of bounds
        if r < 0 or r >= len(data) or c < 0 or c >= len(data[0]):
            perimeter += 1
            continue

        # If neighboring cell is the same character and not explored
        if data[r_idx][c_idx] == data[r][c] and (r, c) not in explored_cells:
            # Recursively explore this neighbor
            p, a = explore_neighbors(data, r, c, explored_cells)
            perimeter += p
            area += a
        # If neighboring cell is different, it's a perimeter
        elif data[r_idx][c_idx] != data[r][c]:
            perimeter += 1

    return perimeter, area


@dataclass
class Region:
    id: int
    char: str
    sides: int = 0
    area: int = 0


def p2(input: str):
    # Parse input and pad with '.' region
    lines = input.split("\n")
    height = len(lines)
    width = len(lines[0])

    # Create padded grid
    grid = [["."] * (width + 2) for _ in range(height + 2)]
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            grid[i + 1][j + 1] = char

    # Identify unique regions
    regions: dict[tuple[int, int], Region] = {}  # (r, c) -> Region
    next_id = 0

    for r in range(1, height + 1):
        for c in range(1, width + 1):
            if (r, c) not in regions:
                # New region found, flood fill
                char = grid[r][c]
                region = Region(next_id, char)
                next_id += 1

                # Flood fill
                to_explore = [(r, c)]
                while to_explore:
                    curr_r, curr_c = to_explore.pop()
                    if (curr_r, curr_c) in regions:
                        continue

                    regions[(curr_r, curr_c)] = region
                    region.area += 1

                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        new_r, new_c = curr_r + dr, curr_c + dc
                        if grid[new_r][new_c] == char and (new_r, new_c) not in regions:
                            to_explore.append((new_r, new_c))

    # Count sides for each region
    unique_regions: dict[int, Region] = {
        region.id: region for region in regions.values()
    }

    for r in range(1, height + 1):
        for c in range(1, width + 1):
            current_region = regions[(r, c)]

            # Top surface
            if (grid[r - 1][c] != current_region.char) and (
                grid[r][c - 1] != current_region.char
                or grid[r - 1][c - 1] == current_region.char
            ):
                current_region.sides += 1

            # Left surface
            if (grid[r][c - 1] != current_region.char) and (
                grid[r - 1][c] != current_region.char
                or grid[r - 1][c - 1] == current_region.char
            ):
                current_region.sides += 1

            # Bottom surface
            if (grid[r + 1][c] != current_region.char) and (
                grid[r][c - 1] != current_region.char
                or grid[r + 1][c - 1] == current_region.char
            ):
                current_region.sides += 1

            # Right surface
            if (grid[r][c + 1] != current_region.char) and (
                grid[r - 1][c] != current_region.char
                or grid[r - 1][c + 1] == current_region.char
            ):
                current_region.sides += 1

    # Calculate total
    total = 0
    for region in unique_regions.values():
        # print(f"Sides: {region.sides}, Area: {region.area}, {region.char}")
        total += region.sides * region.area

    return total


def main():
    with open("d12/input.txt") as f:
        input = f.read()

    test = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
