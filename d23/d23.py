import time
from itertools import combinations
from typing import TypeVar


def p1(input: str):
    lines = input.strip().split("\n")
    computer_connections = [line.split("-") for line in lines]

    connections: dict[str, set[str]] = {}

    for c1, c2 in computer_connections:
        connections[c1] = connections.get(c1, set())
        connections[c1].add(c2)
        connections[c2] = connections.get(c2, set())
        connections[c2].add(c1)

    triplet_connections: set[tuple[str, str, str]] = set()

    for c1, cs in connections.items():
        triplet_connections.update(
            tuple(sorted([c1, c2, c3]))  # type: ignore[misc]
            for (c2, c3) in combinations(cs, 2)
            if c2 in connections[c3]
            and c3 in connections[c2]
            and (c1[0] == "t" or c2[0] == "t" or c3[0] == "t")
        )

    return len(triplet_connections)


T = TypeVar("T")


def all_combinations(iterable: set[T], min_length: int = 1) -> set[tuple[T, ...]]:
    out: set[tuple[T, ...]] = set()
    for i in range(min_length, len(iterable) + 1):
        out.update(combinations(iterable, i))
    return out


def p2(input: str):
    lines = input.strip().split("\n")
    computer_connections = [line.split("-") for line in lines]

    connections: dict[str, set[str]] = {}

    for c1, c2 in computer_connections:
        connections[c1] = connections.get(c1, set())
        connections[c1].add(c2)
        connections[c2] = connections.get(c2, set())
        connections[c2].add(c1)

    # We need to find the biggest group of computers that are connected to each other
    biggest_group: set[str] = set()

    for c1, cs in connections.items():
        conns = {
            tuple(sorted((c1, *comb)))
            for comb in all_combinations(cs, min_length=len(biggest_group))
            if all(
                comb[i] in connections[comb[j]]
                for i in range(len(comb))
                for j in range(i + 1, len(comb))
            )
        }
        if conns:
            biggest_group = max(conns, key=len)  # type: ignore[arg-type]

    password = ",".join(sorted(biggest_group))

    return password


def main():
    with open("d23/input.txt") as f:
        input = f.read()

    test = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""

    st = time.perf_counter()

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")

    print(f"Time taken: {time.perf_counter() - st:.3f} seconds")


if __name__ == "__main__":
    main()
