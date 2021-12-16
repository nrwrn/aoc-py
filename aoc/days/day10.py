from io import TextIOBase
from typing import Any, List, Tuple, Iterator


open_close = {"(": ")", "[": "]", "{": "}", "<": ">"}
invalid_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
complete_points = {")": 1, "]": 2, "}": 3, ">": 4}


def part1(files: List[TextIOBase]) -> int:
    cmap = [[c for c in line.strip()] for line in files[0]]
    acc = 0
    for line in cmap:
        stack = []
        for char in line:
            if char in open_close.keys():
                stack.append(open_close[char])
            elif char != stack.pop():
                acc += invalid_points[char]
                break
    return acc


def part2(files: List[TextIOBase]) -> int:
    cmap = [[c for c in line.strip()] for line in files[0]]
    scores = []
    for line in cmap:
        stack = []
        valid = True
        for char in line:
            if char in open_close.keys():
                stack.append(open_close[char])
            elif char != stack.pop():
                valid = False
                break
        if valid:
            acc = 0
            for char in reversed(stack):
                acc *= 5
                acc += complete_points[char]
            scores.append(acc)
    return sorted(scores)[len(scores)//2]
