def get_combo(a: int, b: int, c: int, operand: int) -> int:
    if operand < 4:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    else:
        # Won't happen
        raise ValueError("Invalid operand")


def run_program(program: list[int], registers: tuple[int, int, int]) -> list[int]:
    a, b, c = registers

    pc = 0
    out: list[int] = []

    while pc < len(program) - 1:
        instr = program[pc]
        operand = program[pc + 1]

        if instr == 0:
            # ADV
            a = a >> get_combo(a, b, c, operand)
        elif instr == 1:
            # BXL
            b = b ^ operand
        elif instr == 2:
            # BST
            b = get_combo(a, b, c, operand) & 0b111
        elif instr == 3:
            # JNZ
            if a != 0:
                pc = operand
                continue
        elif instr == 4:
            # BXC
            b = b ^ c
        elif instr == 5:
            # OUT
            out.append(get_combo(a, b, c, operand) & 0b111)
        elif instr == 6:
            # BDV
            b = a >> get_combo(a, b, c, operand)
        elif instr == 7:
            # CDV
            c = a >> get_combo(a, b, c, operand)

        pc += 2

    return out


def p1(input: str):
    input = input.strip()

    registers = input.split("\n\n")[0].split("\n")
    a = int(registers[0].split(": ")[1])
    b = int(registers[1].split(": ")[1])
    c = int(registers[2].split(": ")[1])

    program = [int(i) for i in input.split("\n\n")[1].strip().split(": ")[1].split(",")]

    out = run_program(program, (a, b, c))

    return ",".join(map(str, out))


def p2(input: str):
    input = input.strip()

    registers = input.split("\n\n")[0].split("\n")
    a = int(registers[0].split(": ")[1])

    program = [int(i) for i in input.split("\n\n")[1].strip().split(": ")[1].split(",")]

    valid: list[int] = [0]

    for wanted in reversed(program):
        curr_valid = []

        for next_valid in valid:
            for i in range(8):
                a = (next_valid << 3) | i
                res = run_program(program, (a, 0, 0))

                if res[0] == wanted:
                    curr_valid.append(a)

        valid = curr_valid

    return min(valid)


def main():
    with open("d17/input.txt") as f:
        input = f.read()

    #     test = """Register A: 729
    # Register B: 0
    # Register C: 0

    # Program: 0,1,5,4,3,0"""
    test = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
