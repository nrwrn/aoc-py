from io import TextIOBase
from typing import List

class Line:
    def __init__(self, c1, c2) -> None:
        if c1[0] < c2[0]:
            self.c1: tuple[int, int] = c1
            self.c2: tuple[int, int] = c2
        elif c1[0] > c2[0]:
            self.c1: tuple[int, int] = c2
            self.c2: tuple[int, int] = c1
        elif c1[1] < c2[1]:
            self.c1: tuple[int, int] = c1
            self.c2: tuple[int, int] = c2
        else:
            self.c1: tuple[int, int] = c2
            self.c2: tuple[int, int] = c1

    @classmethod
    def from_string(cls, s: str):
        coords = [[int(s) for s in c_str.split(",")] for c_str in s.split(" -> ")]
        return cls((coords[0][0], coords[0][1]), (coords[1][0], coords[1][1]))
    
    def extent(self) -> tuple[int, int]:
        return (max(self.c1[0], self.c2[0]), max(self.c1[1], self.c2[1]))
    
    def is_straight(self) -> bool:
        return self.c1[0] == self.c2[0] or self.c1[1] == self.c2[1]
    
    def points(self) -> List[tuple[int, int]]:
        if self.c1[0] == self.c2[0]:
            start = min(self.c1[1], self.c2[1])
            end = max(self.c1[1], self.c2[1]) + 1
            return [(self.c1[0], j) for j in range(start, end)]
        if self.c1[1] == self.c2[1]:
            start = min(self.c1[0], self.c2[0])
            end = max(self.c1[0], self.c2[0]) + 1
            return [(i, self.c1[1]) for i in range(start, end)]
        else: # assume 45deg
            start, end = (self.c1, self.c2) if self.c1[0] < self.c2[0] else (self.c2, self.c1)
            y_range = range(start[1], end[1] + 1) if start[1] < end[1] else range(start[1], end[1] - 1, -1)
            return [coord for coord in zip(range(start[0], end[0]+1), y_range)]

def max_extent(file: TextIOBase):
    max_extent = (0, 0)
    for line in file:
        extent = Line.from_string(line).extent()
        max_extent = (max(max_extent[0], extent[0]), max(max_extent[1], extent[1]))
    return max_extent

def apply(line: Line, grid: List[List[int]]) -> int:
    acc = 0
    for pt in line.points():
        if grid[pt[0]][pt[1]] == 1:
            acc += 1
        grid[pt[0]][pt[1]] += 1
    return acc

def part1(files: List[TextIOBase]) -> int:
    file = files[0]
    grid_size = max_extent(file)
    file.seek(0)
    grid = [[0 for _ in range(grid_size[1] + 1)] for _ in range(grid_size[0] + 1)]
    acc = 0
    for line_str in file:
        line = Line.from_string(line_str)
        if line.is_straight():
            acc += apply(line, grid)
    return acc

def part2(files: List[TextIOBase]) -> int:
    file = files[0]
    grid_size = max_extent(file)
    file.seek(0)
    grid = [[0 for _ in range(grid_size[1] + 1)] for _ in range(grid_size[0] + 1)]
    acc = 0
    for line_str in file:
        line = Line.from_string(line_str)
        acc += apply(line, grid)
    #for row in [list(x) for x in zip(*grid)]:
    #    print(row)
    return acc