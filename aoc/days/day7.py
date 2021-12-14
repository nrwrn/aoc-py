from io import TextIOBase
from typing import List

def crab_fn(crabs: List, n: int) -> int:
    return sum([abs(crab - n) for crab in crabs])

def part1(files: List[TextIOBase]) -> int:
    crabs = [int(s) for s in files[0].readline().split(',')]
    checks = set(crabs)
    return min([sum([abs(crab - check) for crab in crabs]) for check in checks])

def tri_fuel(dist: int) -> int:
    return dist * (dist + 1) // 2

def part2(files: List[TextIOBase]) -> int:
    crabs = [int(s) for s in files[0].readline().split(',')]
    checks = range(min(crabs), max(crabs) + 1)
    return min([sum([tri_fuel(abs(crab - check)) for crab in crabs]) for check in checks])