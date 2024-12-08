import itertools
import math

import tqdm


def get_eval_res(nums: list[int], ops: tuple[str, ...], acc: int = 0) -> int:
    if len(nums) == 0:
        return acc

    if acc == 0:
        # take the first two numbers, and first op
        first_num = nums[0]
        second_num = nums[1]
        op = ops[0]

        if op == "||":
            new_acc = (
                first_num * 10 ** math.floor(math.log10(second_num) + 1) + second_num
            )
        elif op == "+":
            new_acc = first_num + second_num
        elif op == "*":
            new_acc = first_num * second_num

        return get_eval_res(nums[2:], ops[1:], new_acc)
    else:
        # take the first number, and first op
        first_num = nums[0]
        op = ops[0]

        if op == "||":
            new_acc = acc * 10 ** math.floor(math.log10(first_num) + 1) + first_num
        elif op == "+":
            new_acc = acc + first_num
        elif op == "*":
            new_acc = acc * first_num

        return get_eval_res(nums[1:], ops[1:], new_acc)


def p1(input: str):
    lines = [line for line in input.split("\n") if line]

    parts = [
        (int(line.split(": ")[0]), [int(x) for x in line.split(": ")[1].split(" ")])
        for line in lines
    ]

    acc = 0

    for line in tqdm.tqdm(parts):
        req_total = line[0]
        available_nums = line[1]

        # We want to arrange the numbers as such:
        # ((((1 * 2) + 3) + 4) * 5) + 6
        # Where + and * can be in any place, and the numbers have to be in the order given

        pos_op_combos = list(
            itertools.product(["+", "*"], repeat=len(available_nums) - 1)
        )

        valid = False

        for ops in pos_op_combos:
            value = get_eval_res(available_nums, ops)

            if value == req_total:
                valid = True
                break

        if valid:
            acc += req_total

    return acc


def p2(input: str):
    lines = [line for line in input.split("\n") if line]

    parts = [
        (int(line.split(": ")[0]), [int(x) for x in line.split(": ")[1].split(" ")])
        for line in lines
    ]

    acc = 0

    for line in tqdm.tqdm(parts):
        req_total = line[0]
        available_nums = line[1]

        # We want to arrange the numbers as such:
        # ((((1 * 2) + 3) + 4) * 5) + 6
        # Where + and * can be in any place, and the numbers have to be in the order given

        pos_op_combos = list(
            itertools.product(["+", "*", "||"], repeat=len(available_nums) - 1)
        )

        valid = False

        for ops in pos_op_combos:
            value = get_eval_res(available_nums, ops)

            if value == req_total:
                valid = True
                break

        if valid:
            acc += req_total

    return acc


def main():
    with open("d7/input.txt") as f:
        input = f.read()

    test = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
