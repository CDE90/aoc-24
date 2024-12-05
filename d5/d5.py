def satisfies(rules: list[tuple[int, int]], update_nums: list[int]):
    for rule in rules:
        first, second = rule
        if first in update_nums and second in update_nums:
            if update_nums.index(second) < update_nums.index(first):
                return False
    return True


def p1(input: str):
    parts = input.split("\n\n")

    rules = [rule for rule in parts[0].split("\n") if rule]
    updates = [update for update in parts[1].split("\n") if update]

    full_rules = [
        (int(first), int(second))
        for first, second in (rule.split("|") for rule in rules if rule)
    ]

    acc = 0

    for update in updates:
        update_nums = [int(x) for x in update.split(",") if x]

        if satisfies(full_rules, update_nums):
            acc += update_nums[len(update_nums) // 2]

    return acc


def p2(input: str):
    parts = input.split("\n\n")

    rules = [rule for rule in parts[0].split("\n") if rule]
    updates = [update for update in parts[1].split("\n") if update]

    full_rules = [
        (int(first), int(second))
        for first, second in (rule.split("|") for rule in rules if rule)
    ]

    acc = 0

    for update in updates:
        update_nums = [int(x) for x in update.split(",") if x]

        if satisfies(full_rules, update_nums):
            continue

        for i in range(len(update_nums) - 1):
            for j in range(i + 1, len(update_nums)):
                a, b = update_nums[i], update_nums[j]

                for rule in full_rules:
                    if rule[0] == a and rule[1] == b:
                        update_nums[i], update_nums[j] = b, a
                        break

        if satisfies(full_rules, update_nums):
            acc += update_nums[len(update_nums) // 2]

    return acc


def main():
    with open("d5/input.txt") as f:
        input = f.read()

    test = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
