import time


def p1(input: str):
    id = 0
    blocks = []

    for idx, char in enumerate(input):
        if idx % 2 == 0:
            blocks.extend([id] * int(char))
            id += 1
        else:
            blocks.extend([(-1)] * int(char))

    # For each block, swap any (-1) values with the last non-negative value in the list
    for idx, block in enumerate(blocks):
        # Check if all blocks after this one are negative
        if all(b == -1 for b in blocks[idx + 1 :]):
            break

        if block == -1:
            last_idx = 0
            for i in range(len(blocks) - 1, idx, -1):
                if blocks[i] > 0:
                    last_idx = i
                    break
            blocks[idx] = blocks[last_idx]
            blocks[last_idx] = -1

    blocks = [b for b in blocks if b != -1]

    acc = 0

    for idx, block in enumerate(blocks):
        acc += block * idx

    return acc


def p2(input: str):
    id = 0
    blocks: list[list[int]] = []

    for idx, char in enumerate(input):
        if idx % 2 == 0:
            blocks.append([id] * int(char))
            id += 1
        else:
            blocks.append([(-1)] * int(char))

    idx = 0
    while idx < len(blocks):
        block = blocks[idx]

        # Check if all blocks after this one are negative
        if all(-1 in b for b in blocks[idx + 1 :]):
            break

        if -1 in block:
            available_space = len(block)
            last_idx = 0

            for i in range(len(blocks) - 1, idx, -1):
                if not blocks[i]:
                    continue
                if blocks[i][0] > 0 and len(blocks[i]) <= available_space:
                    last_idx = i
                    break

            if last_idx <= idx:
                idx += 1
                continue

            swap_block = blocks[last_idx]
            blocks[idx] = swap_block
            if len(swap_block) < available_space:
                blocks.insert(idx + 1, [-1] * (available_space - len(swap_block)))
                blocks[last_idx + 1] = block[available_space - len(swap_block) :]
            else:
                blocks[last_idx] = block

        idx += 1

    flattened_blocks = [b for block in blocks for b in block]

    acc = 0

    for idx, b in enumerate(flattened_blocks):
        if b == -1:
            continue
        acc += b * idx

    return acc


def main():
    with open("d9/input.txt") as f:
        input = f.read()

    test = """2333133121414131402"""

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    st = time.perf_counter()
    print(f"Part 1: {p1(input)}")
    print(f"Part 1 time: {time.perf_counter() - st}")
    st = time.perf_counter()
    print(f"Part 2: {p2(input)}")
    print(f"Part 2 time: {time.perf_counter() - st}")


if __name__ == "__main__":
    main()
