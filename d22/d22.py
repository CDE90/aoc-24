import time
from functools import cache

from tqdm import tqdm


@cache
def evolve_number(num: int) -> int:
    num = ((num * 64) ^ num) % 16777216
    num = ((num // 32) ^ num) % 16777216
    num = ((num * 2048) ^ num) % 16777216
    return num


def p1(input: str):
    numbers = [int(x) for x in input.strip().split("\n")]

    acc = 0

    for num in numbers:
        new_num = num
        for i in range(2000):
            new_num = evolve_number(new_num)
        acc += new_num

    return acc


def p2(input: str, test_mode: bool = False):
    numbers = [int(x) for x in input.strip().split("\n")]

    acc = 0

    prices: list[list[int]] = []

    for i, num in enumerate(numbers):
        prices.append([num % 10])
        for j in range(2000):
            num = evolve_number(num)
            prices[i].append(num % 10)

    price_diffs: list[list[int]] = []
    for i in range(len(prices)):
        price_diffs.append([])
        for j in range(1, len(prices[i])):
            price_diffs[i].append(prices[i][j] - prices[i][j - 1])

    price_diff_sequences: dict[tuple[int, int, int, int], int] = {}
    seq_prices: list[dict[tuple[int, int, int, int], int]] = []

    for buyer_idx, buyer_diffs in enumerate(tqdm(price_diffs)):
        seq_prices.append({})
        for i in range(len(buyer_diffs) - 3):
            tup = (
                buyer_diffs[i],
                buyer_diffs[i + 1],
                buyer_diffs[i + 2],
                buyer_diffs[i + 3],
            )
            price_diff_sequences[tup] = price_diff_sequences.get(tup, 0) + 1
            if tup not in seq_prices[buyer_idx]:
                seq_prices[buyer_idx][tup] = prices[buyer_idx][i + 4]

    if not test_mode:
        # Only keep sequences that have a count of at least 300
        # (ignore sequences that will obviously not give a high enough score)
        price_diff_sequences = {
            tup: count for tup, count in price_diff_sequences.items() if count >= 300
        }

    valid_price_diff_sequences = list(price_diff_sequences.keys())

    optimal_sequence: tuple[int, int, int, int] = (0, 0, 0, 0)
    optimal_sum = 0

    for price_diff_sequence in tqdm(valid_price_diff_sequences):
        acc = 0
        acc = sum(
            seq_prices[buyer_idx].get(price_diff_sequence, 0)
            for buyer_idx in range(len(price_diffs))
        )

        if acc > optimal_sum:
            optimal_sum = acc
            optimal_sequence = price_diff_sequence

    return optimal_sum


def main():
    with open("d22/input.txt") as f:
        input = f.read()

    test = """1
10
100
2024
"""
    test2 = """1
2
3
2024
"""

    st = time.perf_counter()

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test2, True)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")

    print(f"Time taken: {time.perf_counter() - st:.3f} seconds")


if __name__ == "__main__":
    main()
