from io import TextIOBase
from typing import List


def part1(files: List[TextIOBase]):
    file = files[0]
    prev_int = None
    acc = 0
    for line in file:
        cur_int = int(line)
        if prev_int != None:
            if prev_int < cur_int:
                acc += 1
        prev_int = cur_int
    return acc


def part2(files: List[TextIOBase]):
    file = files[0]
    acc = 0
    prev_window = [int(file.readline()) for _ in range(3)]
    for line in file:
        window = prev_window.copy()
        window.pop(0)
        window.append(int(line))
        if sum(window) > sum(prev_window):
            acc += 1
        prev_window = window
    return acc
