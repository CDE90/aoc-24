def p1(input: str):
    lines = input.split("\n")
    line_nums = [
        (int(line.split("   ")[0]), int(line.split("   ")[1])) for line in lines
    ]
    nums_1 = [line[0] for line in line_nums]
    nums_2 = [line[1] for line in line_nums]

    acc = 0

    while len(nums_1):
        n1 = min(nums_1)
        n2 = min(nums_2)
        diff = abs(n1 - n2)
        acc += diff
        nums_1.remove(n1)
        nums_2.remove(n2)

    return acc


def p2(input: str):
    lines = input.split("\n")
    line_nums = [
        (int(line.split("   ")[0]), int(line.split("   ")[1])) for line in lines
    ]
    nums_1 = [line[0] for line in line_nums]
    nums_2 = [line[1] for line in line_nums]

    acc = 0

    for n1 in nums_1:
        count_n2 = nums_2.count(n1)
        acc += n1 * count_n2

    return acc


def main():
    with open("d1/input.txt") as f:
        input = f.read()

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
