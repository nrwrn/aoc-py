from io import TextIOBase
from typing import Dict, Iterable, List, Optional, Set, Tuple


def get_rules(lines: TextIOBase) -> Dict[str, str]:
    rules = {}
    for line in lines:
        splitsies = line.strip().split(" -> ")
        rules[splitsies[0]] = splitsies[1]
    return rules


def apply(rules: Dict[str, str], polymer: str):
    insertions: List[Optional[str]] = [None for _ in range(len(polymer) - 1)]
    for i in range(len(polymer) - 1):
        pair = polymer[i : i + 2]
        if pair in rules:
            insertions[i] = rules[pair]
    offset = 1
    li = list(polymer)
    for i, insert in enumerate(insertions):
        if insert is None:
            continue
        li.insert(i + offset, insert)
        offset += 1
    return "".join(li)


def histogram(s: str) -> Dict[str, int]:
    h = {}
    for char in s:
        if char not in h:
            h[char] = 0
        h[char] += 1
    return h


def hist_add(a: Dict[str, int], b: Dict[str, int]) -> Dict[str, int]:
    c = {}
    for k, v in a.items():
        if k not in c:
            c[k] = 0
        c[k] += v
    for k, v in b.items():
        if k not in c:
            c[k] = 0
        c[k] += v
    return c


class Polymer:
    def __init__(self, seed: str, rules: Dict[str, str]) -> None:
        self.memo: Dict[Tuple[str, int], Dict[str, int]] = {}
        self.seed = seed
        self.rules = rules
    
    def run(self, steps: int) -> Dict[str, int]:
        letter_counts = histogram(self.seed)
        for i in range(len(self.seed) - 1):
            pair = self.seed[i : i + 2]
            letter_counts = hist_add(letter_counts, self._recurse(pair, steps))
        return letter_counts

    def _recurse(self, pair: str, steps: int) -> Dict[str, int]:
        if steps == 0:
            return {}
        if pair not in self.rules:
            return {}
        if (pair, steps) in self.memo:
            return self.memo[(pair, steps)]
        insert = self.rules[pair]
        hist = {insert: 1}
        hist = hist_add(hist, self._recurse(pair[0] + insert, steps - 1))
        hist = hist_add(hist, self._recurse(insert + pair[1], steps - 1))
        self.memo[(pair, steps)] = hist
        return hist


def part1(files: List[TextIOBase]) -> int:
    lines = files[0]
    polymer = lines.readline().strip()
    lines.readline()  # empty line
    rules = get_rules(lines)
    for _ in range(10):
        polymer = apply(rules, polymer)
    freqs = histogram(polymer).values()
    return max(freqs) - min(freqs)


def part2(files: List[TextIOBase]) -> int:
    lines = files[0]
    seed = lines.readline().strip()
    lines.readline()  # empty line
    rules = get_rules(lines)
    polymer = Polymer(seed, rules)
    freqs = polymer.run(40).values()
    return max(freqs) - min(freqs)
