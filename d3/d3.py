import re


def p1(input: str):
    regex = r"mul\((\d+),(\d+)\)"

    # Find the number of matches
    matches = re.findall(regex, input)

    acc = 0
    # Sum the multiplication of each match
    for match in matches:
        acc += int(match[0]) * int(match[1])

    return acc


def p2(input: str):
    mul_regex = r"mul\((\d+),(\d+)\)"
    do_regex = r"do\(\)"
    dont_regex = r"don\'t\(\)"

    enabled = True
    acc = 0

    while len(input):
        match = re.search(re.compile(f"({mul_regex}|{do_regex}|{dont_regex})"), input)

        if not match:
            return acc

        if "mul" in match.group(1) and enabled:
            acc += int(match.group(2)) * int(match.group(3))
        elif "don't" in match.group(1):
            enabled = False
        elif "do" in match.group(1):
            enabled = True

        # remove the matched string from the input
        input = input[match.end() :]

    return acc


def main():
    with open("d3/input.txt") as f:
        input = f.read()

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
