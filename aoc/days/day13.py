from io import TextIOBase
from typing import Dict, Iterable, List, Set, Tuple


def fold(points: Set[Tuple[int, int]], pos: int, axis: int) -> Set[Tuple[int, int]]:
    folded = set()
    for point in points:
        if point[axis] == pos:
            continue  # it's on the fold line
        elif point[axis] < pos:
            folded.add(point)
        else:  # doing this extra slick so it could easily adapt to n dimensions
            new_point = list(point)
            new_point[axis] = pos * 2 - new_point[axis]
            folded.add(tuple(new_point))
    return folded


def part1(files: List[TextIOBase]) -> int:
    lines = files[0]
    points: Set[Tuple[int, int]] = set()
    line = lines.readline()
    while line.strip() != "":
        points.add(tuple([int(n) for n in line.strip().split(",")]))
        line = lines.readline()
    fold_line = lines.readline()
    fold_pos = int(fold_line.split("=")[1])
    fold_axis = 0 if "x" in fold_line else 1
    points = fold(points, fold_pos, fold_axis)
    return len(points)


def part2(files: List[TextIOBase]) -> int:
    lines = files[0]
    points: Set[Tuple[int, int]] = set()
    line = lines.readline()
    while line.strip() != "":
        points.add(tuple([int(n) for n in line.strip().split(",")]))
        line = lines.readline()
    for fold_line in lines:
        fold_pos = int(fold_line.split("=")[1])
        fold_axis = 0 if "x" in fold_line else 1
        points = fold(points, fold_pos, fold_axis)
    extent = (max([i for i, j in points]), max([j for i, j in points]))
    chars = [["." for i in range(extent[0] + 1)] for j in range(extent[1] + 1)]
    for point in points:
        chars[point[1]][point[0]] = "#"
    for c_line in chars:
        print("".join(c_line))
    return len(points)
