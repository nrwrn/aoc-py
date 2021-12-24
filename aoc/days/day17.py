from io import TextIOBase
from bitstring import BitArray
from typing import Any, Dict, Iterator, List, Optional, Set, Tuple
from operator import mul
from functools import reduce
from dataclasses import dataclass


@dataclass
class Box:
    x: Tuple[int, int]
    y: Tuple[int, int]
    
    @classmethod
    def from_string(cls, s: str) -> 'Box':
        stuff = s.split(": ")[1]
        x = stuff.split(", ")[0].split("=")[1].split("..")
        y = stuff.split(", ")[1].split("=")[1].split("..")
        return Box((int(x[0]), int(x[1])), (int(y[0]), int(y[1])))

    def floor(self) -> int:
        return min(self.y)
    
    def xouter(self) -> int:
        x = self.x
        return x[0] if abs(x[0]) > abs(x[1]) else x[1]
    
    def contains(self, point: Tuple[int, int]) -> bool:
        x, y = point
        return x >= min(self.x) and x <= max(self.x) and y >= min(self.y) and y <= max(self.y)


def is_miss(pos: Tuple[int, int], vel: Tuple[int, int], tgt: Box) -> bool:
    if tgt.xouter() < pos[0]:
        return True
    if pos[1] < tgt.floor() and vel[1] <= 0:
        return True
    return False


def path_iter(vel: Tuple[int, int], box: Box) -> Iterator[Tuple[int, int]]:
    pos = (0,0)
    while not is_miss(pos, vel, box):
        yield pos
        pos = (pos[0] + vel[0], pos[1] + vel[1])
        drag = 1 if vel[0] > 0 else 0
        vel = (vel[0] - drag, vel[1] - 1)


def part1(files: List[TextIOBase]) -> int:
    box = Box.from_string(files[0].readline().strip())
    hits = []
    # y upper bound assumes box is completely below the origin
    for y in range(box.floor(), abs(box.floor()) + 1):
        for x in range(box.xouter() + 1):
            peak = 0
            for point in path_iter((x, y), box):
                peak = max(peak, point[1])
                if box.contains(point):
                    hits.append(peak)
                    break
    return max(hits)


def part2(files: List[TextIOBase]) -> int:
    box = Box.from_string(files[0].readline().strip())
    hits = 0
    # y upper bound assumes box is completely below the origin
    for y in range(box.floor(), abs(box.floor()) + 1):
        for x in range(box.xouter() + 1):
            peak = 0
            for point in path_iter((x, y), box):
                if box.contains(point):
                    hits += 1
                    break
    return hits