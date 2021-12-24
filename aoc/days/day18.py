from io import TextIOBase
from typing import Any, Dict, Iterator, List, Optional, Set, Tuple, Union
from dataclasses import dataclass
from math import floor, ceil


@dataclass
class Snum:
    val: Optional[int]
    l: Optional["Snum"] = None
    r: Optional["Snum"] = None

    def is_leaf(self) -> bool:
        return self.val is not None

    def __add__(self: "Snum", other: "Snum") -> "Snum":
        new = Snum(None, self.copy(), other.copy())
        new.reduce()
        return new
    
    def __repr__(self):
        if self.val is not None:
            return str(self.val)
        else:
            assert self.l and self.r
            return "[" + str(self.l) + "," + str(self.r) + "]"
    
    def copy(self) -> "Snum":
        return Snum(self.val, self.l.copy() if self.l else None, self.r.copy() if self.r else None)

    def reduce(self):
        while self.try_explode() or self.try_split():
            pass

    def try_explode(self) -> bool:
        last_leaf: Optional[Snum] = None
        iterator = traverse(self)
        for sn, depth in iterator:
            if sn.is_leaf():
                last_leaf = sn
            elif depth > 3:
                assert sn.l and sn.r and sn.l.val is not None and sn.r.val is not None
                if last_leaf and last_leaf.val is not None:
                    last_leaf.val += sn.l.val
                next(iterator)
                next(iterator)
                for next_leaf, _ in iterator:
                    if next_leaf.is_leaf() and next_leaf.val is not None:
                        next_leaf.val += sn.r.val
                        break
                sn.val = 0
                sn.l = None
                sn.r = None
                return True
        return False

    def try_split(self) -> bool:
        for sn, _ in traverse(self):
            if sn.is_leaf() and sn.val and sn.val > 9:
                sn.l = Snum(floor(sn.val / 2.0))
                sn.r = Snum(ceil(sn.val / 2.0))
                sn.val = None
                return True
        return False

    @classmethod
    def read(cls, s: str) -> "Snum":
        if s[0] == "[":
            left = Snum.read(s[1:])
            right = Snum.read(after_comma(s[1:]))
            return Snum(None, left, right) 
        else:
            return Snum(int(s.split(",")[0].strip("]")))

    def mag(self) -> int:
        if self.val is not None:
            return self.val
        assert self.l and self.r
        return self.l.mag() * 3 + self.r.mag() * 2


def after_comma(s: str) -> str:
    depth = 0
    chars = iter(s)
    for char in chars:
        if char == "," and depth == 0:
            return "".join(chars)
        elif char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
    raise RuntimeError


def traverse(sn: Snum) -> Iterator[Tuple[Snum, int]]:
    stack: List[Tuple[Snum, int]] = [(sn, 0)]
    while len(stack) > 0:
        active, depth = stack.pop()
        yield active, depth
        if not active.is_leaf():
            if active.r is not None:  # to appease mypy
                stack.append((active.r, depth + 1))
            if active.l is not None:  # to appease mypy
                stack.append((active.l, depth + 1))


def part1(files: List[TextIOBase]) -> int:
    file = files[0]
    snsum = Snum.read(file.readline().strip())
    for line in file:
        snsum += Snum.read(line.strip())
    return snsum.mag()


def part2(files: List[TextIOBase]) -> int:
    mags: List[int] = []
    snums = [Snum.read(line.strip()) for line in files[0]]
    for snum in snums:
        for other in snums:
            if snum is other:
                continue
            mags.append((snum + other).mag())
    return max(mags)
