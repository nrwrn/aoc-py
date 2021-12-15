from io import TextIOBase
from typing import Callable, Dict, List, Tuple


def parse_line(line: str) -> Tuple[List[str], List[str]]:
    divided = line.split(" | ", 2)
    tokenized = [sec.split() for sec in divided]
    sortified = [["".join(sorted(token)) for token in sec] for sec in tokenized]
    return sortified[0], sortified[1]


def part1(files: List[TextIOBase]) -> int:
    acc = 0
    for line in files[0]:
        signals, outputs = parse_line(line)
        for output in outputs:
            if len(output) in [2, 3, 4, 7]:
                acc += 1
    return acc


def segs(num: int) -> Callable[[str], bool]:
    def pred(segments: str) -> bool:
        return len(segments) == num

    return pred


def diff(str1: str, str2: str) -> str:
    return list(set(str1) - set(str2))[0]


def contains_all(substr: str) -> Callable[[str], bool]:
    def pred(superstr: str) -> bool:
        return all([char in superstr for char in substr])

    return pred


def part2(files: List[TextIOBase]) -> int:
    acc = 0
    for line in files[0]:
        signals, outputs = parse_line(line)
        one = next(filter(segs(2), signals))
        four = next(filter(segs(4), signals))
        seven = next(filter(segs(3), signals))
        eight = next(filter(segs(7), signals))
        for signal in filter(segs(6), signals):
            if contains_all(four)(signal):
                nine = signal
            elif contains_all(seven)(signal):
                zero = signal
            else:
                six = signal
        top_left = diff(eight, six)
        for signal in filter(segs(5), signals):
            if contains_all(one)(signal):
                three = signal
            elif top_left in signal:
                two = signal
            else:
                five = signal
        key = {
            zero: 0,
            one: 1,
            two: 2,
            three: 3,
            four: 4,
            five: 5,
            six: 6,
            seven: 7,
            eight: 8,
            nine: 9,
        }
        acc += int("".join([str(key[output]) for output in outputs]))
    return acc
