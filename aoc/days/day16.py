from io import TextIOBase
from bitstring import BitArray
from typing import Any, Dict, Iterator, List, Optional, Set, Tuple
from operator import mul
from functools import reduce


def bit_iter(file: TextIOBase) -> Iterator[str]:
    for line in file:
        for char in list(line.strip()):
            for bit in list(BitArray(hex=char).bin):
                yield bit


def iter_pop(iter: Iterator[Any], num: int) -> List[Any]:
    return [elem for _, elem in zip(range(num), iter)]


def read_packet(bits: Iterator[str]) -> Dict[str, int]:
    version = int("".join(iter_pop(bits, 3)), 2)
    ptype = int("".join(iter_pop(bits, 3)), 2)
    length = 6
    if ptype == 4:
        continuation = True
        literal = []
        while continuation:
            continuation = (next(bits) == "1")
            literal += iter_pop(bits, 4)
            length += 5
        int_lit = int("".join(literal), 2)
        return {"version_sum": version, "value": int_lit, "length": length}
    lid = next(bits)
    length += 1
    version_sum = version
    values = []
    if lid == "1":
        sub_length = int("".join(iter_pop(bits, 11)), 2)
        length += 11
        for _ in range(sub_length):
            result = read_packet(bits)
            length += result["length"]
            version_sum += result["version_sum"]
            values.append(result["value"])
    else:
        sub_length = int("".join(iter_pop(bits, 15)), 2)
        length += 15
        while sub_length > 0:
            result = read_packet(bits)
            sub_length -= result["length"]
            length += result["length"]
            version_sum += result["version_sum"]
            values.append(result["value"])
    if ptype == 0:
        value = sum(values)
    elif ptype == 1:
        value = reduce(mul, values, 1)
    elif ptype == 2:
        value = min(values)
    elif ptype == 3:
        value = max(values)
    elif ptype == 5:
        value = 1 if values[0] > values[1] else 0
    elif ptype == 6:
        value = 1 if values[0] < values[1] else 0
    elif ptype == 7:
        value = 1 if values[0] == values[1] else 0
    else:
        raise NotImplementedError
    return {"version_sum": version_sum, "value": value, "length": length}


def part1(files: List[TextIOBase]) -> int:
    bits = bit_iter(files[0])
    return read_packet(bits)["version_sum"]


def part2(files: List[TextIOBase]) -> int:
    bits = bit_iter(files[0])
    return read_packet(bits)["value"]