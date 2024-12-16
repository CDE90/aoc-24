import copy
from typing import Literal


def handle_instruction(
    map: list[list[str]], bot_pos: tuple[int, int], instr: Literal["<", "^", ">", "v"]
):
    if instr == "<":
        direction = (0, -1)
    elif instr == "^":
        direction = (-1, 0)
    elif instr == ">":
        direction = (0, 1)
    elif instr == "v":
        direction = (1, 0)

    i, j = bot_pos

    pot_pos = (i + direction[0], j + direction[1])

    if map[pot_pos[0]][pot_pos[1]] == ".":
        map[pot_pos[0]][pot_pos[1]] = "@"
        map[i][j] = "."
        return pot_pos
    elif map[pot_pos[0]][pot_pos[1]] == "#":
        return bot_pos
    else:
        box_pos = pot_pos
        while map[box_pos[0]][box_pos[1]] == "O":
            box_pos = (box_pos[0] + direction[0], box_pos[1] + direction[1])
            if map[box_pos[0]][box_pos[1]] == "#":
                return bot_pos

            if map[box_pos[0]][box_pos[1]] == ".":
                map[box_pos[0]][box_pos[1]] = "O"
                map[i][j] = "."
                map[pot_pos[0]][pot_pos[1]] = "@"
                return pot_pos


def p1(input: str):
    parts = input.split("\n\n")

    map_str = parts[0]
    map = [[char for char in row] for row in map_str.split("\n")]

    instructions_f = parts[1]
    instructions: list[Literal["<", "^", ">", "v"]] = list(
        instructions_f.replace("\n", "")  # type: ignore[arg-type]
    )

    bot_pos = (-1, -1)

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "@":
                bot_pos = (i, j)
                break

    for instr in instructions:
        bot_pos = handle_instruction(map, bot_pos, instr)

    acc = 0

    for i in range(len(map)):
        for j, char in enumerate(map[i]):
            if char != "O":
                continue

            acc += 100 * i + j

    return acc


def handle_instruction_2(
    map: list[list[str]], bot_pos: tuple[int, int], instr: Literal["<", "^", ">", "v"]
):
    if instr == "<":
        direction = (0, -1)
    elif instr == "^":
        direction = (-1, 0)
    elif instr == ">":
        direction = (0, 1)
    elif instr == "v":
        direction = (1, 0)

    i, j = bot_pos

    pot_pos = (i + direction[0], j + direction[1])

    if map[pot_pos[0]][pot_pos[1]] == ".":
        map[pot_pos[0]][pot_pos[1]] = "@"
        map[i][j] = "."
        return pot_pos
    elif map[pot_pos[0]][pot_pos[1]] == "#":
        return bot_pos
    else:
        box_positions = set()
        box_positions.add(pot_pos)

        e = len(box_positions)

        cur = pot_pos
        while map[cur[0]][cur[1]] in ["[", "]"]:
            box_positions.add(cur)
            cur = (cur[0] + direction[0], cur[1] + direction[1])

        run_once = False
        while e != len(box_positions) or not run_once:
            e = len(box_positions)
            run_once = True

            for pos in list(box_positions):
                t1, t2 = pos
                if map[t1][t2] == "[":
                    box_positions.add((t1, t2 + 1))
                if map[t1][t2] == "]":
                    box_positions.add((t1, t2 - 1))

                if map[t1 + direction[0]][t2 + direction[1]] in ["[", "]"]:
                    box_positions.add((t1 + direction[0], t2 + direction[1]))

        can_move = True
        for pos in box_positions:
            temp = (pos[0] + direction[0], pos[1] + direction[1])
            if map[temp[0]][temp[1]] == "#":
                can_move = False
                break

        if not can_move:
            return bot_pos

        if direction in [(-1, 0), (0, -1)]:
            sorted_positions = sorted(box_positions, key=lambda x: (x[0], x[1]))
        else:
            sorted_positions = sorted(
                box_positions, key=lambda x: (x[0], x[1]), reverse=True
            )

        old_map = copy.deepcopy(map)

        for pos in sorted_positions:
            new_box_pos = (pos[0] + direction[0], pos[1] + direction[1])
            map[new_box_pos[0]][new_box_pos[1]] = old_map[pos[0]][pos[1]]
            map[pos[0]][pos[1]] = "."

        map[i][j] = "."
        map[pot_pos[0]][pot_pos[1]] = "@"
        return pot_pos


def p2(input: str):
    parts = input.split("\n\n")

    map_str = parts[0]
    map_str = (
        map_str.replace("#", "##")
        .replace("O", "[]")
        .replace(".", "..")
        .replace("@", "@.")
    )
    map = [[char for char in row] for row in map_str.split("\n")]

    instructions_f = parts[1]
    instructions: list[Literal["<", "^", ">", "v"]] = list(
        instructions_f.replace("\n", "")  # type: ignore[arg-type]
    )

    bot_pos = (-1, -1)

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "@":
                bot_pos = (i, j)
                break

    for instr in instructions:
        bot_pos = handle_instruction_2(map, bot_pos, instr)

    acc = 0

    for i in range(len(map)):
        for j, char in enumerate(map[i]):
            if char == "[":
                acc += 100 * i + j

    return acc


def main():
    with open("d15/input.txt") as f:
        input = f.read()

    test1 = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

    test2 = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

    print(f"Part 1 test: {p1(test1)}")
    print(f"Part 2 test: {p2(test1)}")

    print(f"Part 1 test2: {p1(test2)}")
    print(f"Part 2 test2: {p2(test2)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
