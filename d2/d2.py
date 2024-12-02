def satisfies(numbers: list[int]):
    # Check if the numbers are all increasing or decreasing
    if all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)) and all(
        1 <= abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1)
    ):
        return True
    elif all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1)) and all(
        1 <= abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1)
    ):
        return True

    return False


def p1(input: str):
    lines = input.split("\n")

    acc = 0

    for line in lines:
        if line == "":
            continue

        ns = line.split(" ")
        numbers = [int(n) for n in ns]

        acc += int(satisfies(numbers))

    return acc


def p2(input: str):
    lines = input.split("\n")

    acc = 0

    for line in lines:
        if line == "":
            continue

        ns = line.split(" ")
        numbers = [int(n) for n in ns]

        acc += int(satisfies(numbers))

        if satisfies(numbers):
            continue

        # Also check if by removing one of the numbers, we can satisfy the above conditions
        for i in range(len(numbers)):
            numbers_copy = numbers.copy()
            numbers_copy.pop(i)
            acc += int(satisfies(numbers_copy))
            if satisfies(numbers_copy):
                break

    return acc


def main():
    with open("d2/input.txt") as f:
        input = f.read()

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
