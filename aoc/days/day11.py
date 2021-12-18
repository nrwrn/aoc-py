from io import TextIOBase
from typing import Iterable, List, Set, Tuple


def get_neighbors(grid: List[List[int]], i: int, j: int) -> List[Tuple[int, int]]:
    possible = [
        (i + 1, j + 1),
        (i, j + 1),
        (i - 1, j + 1),
        (i - 1, j),
        (i - 1, j - 1),
        (i, j - 1),
        (i + 1, j - 1),
        (i + 1, j),
    ]
    return [
        (i, j)
        for i, j in possible
        if i in range(len(grid)) and j in range(len(grid[0]))
    ]


def grid_iter(grid) -> Iterable[Tuple[int, int]]:
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):  # throw out iter value as it's a copy
            yield i, j


def step(grid: List[List[int]]) -> int:
    flashed = set()
    for i, j in grid_iter(grid):
        grid[i][j] += 1
    for i, j in grid_iter(grid):
        maybe_flash(grid, i, j, flashed)
    for i, j in flashed:
        grid[i][j] = 0
    return len(flashed)


def maybe_flash(
    grid: List[List[int]], i: int, j: int, flashed: Set[Tuple[int, int]]
) -> bool:
    if grid[i][j] > 9 and (i, j) not in flashed:
        flashed.add((i, j))
        for ni, nj in get_neighbors(grid, i, j):
            grid[ni][nj] += 1
            maybe_flash(grid, ni, nj, flashed)


def part1(files: List[TextIOBase]) -> int:
    grid = [[int(c) for c in line.strip()] for line in files[0]]
    acc = 0
    for _ in range(100):
        acc += step(grid)
    return acc


def part2(files: List[TextIOBase]) -> int:
    grid = [[int(c) for c in line.strip()] for line in files[0]]
    grid_size = len(grid) * len(grid[0])
    i = 0
    num = 0
    while num != grid_size:
        num = step(grid)
        i += 1
    return i
