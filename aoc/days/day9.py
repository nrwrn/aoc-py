from io import TextIOBase
from typing import Any, List, Tuple, Iterator
from functools import reduce
from operator import mul


def neighbors(c: Tuple[int, int]) -> List[Tuple[int, int]]:
    i, j = c
    return [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]


def real_neighbors(c: Tuple[int, int], grid: List[List[Any]]) -> Iterator[Tuple[int, int]]:
    for neighbor in neighbors(c):
        ni, nj = neighbor
        if ni in range(0, len(grid)) and nj in range(0, len(grid[0])):
            yield neighbor


def grid_iter(grid: List[List[Any]]) -> Iterator[Tuple[Tuple[int, int], Any]]:
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            yield ((i, j), cell)


def get_lows(hmap: List[List[int]]) -> Iterator[Tuple[int, int]]:
    for c, cell in grid_iter(hmap):
        is_higher = []
        for ni, nj in real_neighbors(c, hmap):
            is_higher.append(True if hmap[ni][nj] > cell else False)
        if all(is_higher):
            yield c


def part1(files: List[TextIOBase]) -> int:
    hmap = [[int(c) for c in line.strip()] for line in files[0]]
    acc = 0
    for i, j in get_lows(hmap):
        acc += hmap[i][j] + 1
    return acc


def part2(files: List[TextIOBase]) -> int:
    hmap = [[int(c) for c in line.strip()] for line in files[0]]
    basin_sizes = []
    for i_low, j_low in get_lows(hmap):
        visited = set()
        queue = [(i_low, j_low)]
        basin_size = 0
        while len(queue) > 0:
            expl = queue.pop(0)
            if hmap[expl[0]][expl[1]] == 9 or expl in visited:
                continue
            visited.add(expl)
            basin_size += 1
            queue += real_neighbors(expl, hmap)
        basin_sizes.append(basin_size)
    return reduce(mul, sorted(basin_sizes)[-3:], 1)
