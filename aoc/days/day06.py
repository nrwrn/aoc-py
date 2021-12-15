from io import TextIOBase
from typing import List


class School:
    def __init__(self, end_day: int):
        self.memo = {}
        self.end_day = end_day

    def spawn_fish(self, start_day: int, counter: int) -> int:
        zero_day = start_day + counter
        fish = 1
        if self.memo.get(zero_day) is not None:
            return self.memo.get(zero_day)
        for i in range(zero_day, self.end_day, 7):
            fish += self.spawn_fish(i + 1, 8)
        self.memo[zero_day] = fish
        return fish


def part1(files: List[TextIOBase]) -> int:
    fish_list = [int(s) for s in files[0].readline().split(",")]
    sch = School(80)
    num_fish = 0
    for fish in fish_list:
        num_fish += sch.spawn_fish(0, fish)
    return num_fish


def part2(files: List[TextIOBase]) -> int:
    fish_list = [int(s) for s in files[0].readline().split(",")]
    sch = School(256)
    num_fish = 0
    for fish in fish_list:
        num_fish += sch.spawn_fish(0, fish)
    return num_fish
