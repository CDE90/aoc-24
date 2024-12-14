import re


def p1(input: str):
    machines = input.split("\n\n")

    acc = 0

    # NOTE: costs 3 tokens to press A, 1 to press B
    # goal to minimize number of tokens

    for machine in machines:
        buttons = machine.split("\n")

        a = re.search(r"Button A: X\+(\d+), Y\+(\d+)", buttons[0])
        b = re.search(r"Button B: X\+(\d+), Y\+(\d+)", buttons[1])
        prize = re.search(r"Prize: X=(\d+), Y=(\d+)", buttons[2])

        assert a is not None and b is not None and prize is not None

        x_a = int(a.group(1))
        y_a = int(a.group(2))
        x_b = int(b.group(1))
        y_b = int(b.group(2))
        x_p = int(prize.group(1))
        y_p = int(prize.group(2))

        min_price = 10**10

        for i in range(100):
            for j in range(100):
                x_new_pos = i * x_a + j * x_b
                y_new_pos = i * y_a + j * y_b
                price = 3 * i + j

                if x_new_pos == x_p and y_new_pos == y_p:
                    min_price = min(min_price, price)

        if min_price == 10**10:
            continue

        acc += min_price

    return acc


def solve_machine(x_a, y_a, x_b, y_b, x_p, y_p):
    det = x_a * y_b - x_b * y_a

    if det == 0:
        return

    a_count = (x_p * y_b - y_p * x_b) / det
    b_count = (x_p * y_a - y_p * x_a) / -det

    if a_count < 0 or b_count < 0 or int(a_count) != a_count or int(b_count) != b_count:
        return

    return 3 * a_count + b_count


def p2(input: str):
    machines = input.split("\n\n")

    acc = 0

    # NOTE: costs 3 tokens to press A, 1 to press B
    # goal to minimize number of tokens

    for machine in machines:
        buttons = machine.split("\n")

        a = re.search(r"Button A: X\+(\d+), Y\+(\d+)", buttons[0])
        b = re.search(r"Button B: X\+(\d+), Y\+(\d+)", buttons[1])
        prize = re.search(r"Prize: X=(\d+), Y=(\d+)", buttons[2])

        assert a is not None and b is not None and prize is not None

        x_a = int(a.group(1))
        y_a = int(a.group(2))
        x_b = int(b.group(1))
        y_b = int(b.group(2))
        x_p = int(prize.group(1))
        y_p = int(prize.group(2))

        x_p += 10000000000000
        y_p += 10000000000000

        price = solve_machine(x_a, y_a, x_b, y_b, x_p, y_p)

        if price is None:
            continue

        acc += int(price)

    return acc


def main():
    with open("d13/input.txt") as f:
        input = f.read()

    test = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
