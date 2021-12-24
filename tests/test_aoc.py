from aoc.aoc import get_func
from io import TextIOWrapper
from importlib import resources

from . import input


def test_d1_p1():
    file = resources.open_text(input, "day01.txt")
    result = get_func(1, 1)([file])
    assert result == 7


def test_d1_p2():
    file = resources.open_text(input, "day01.txt")
    result = get_func(1, 2)([file])
    assert result == 5


def test_d5_p1():
    file = resources.open_text(input, "day05.txt")
    result = get_func(5, 1)([file])
    assert result == 5


def test_d5_p2():
    file = resources.open_text(input, "day05.txt")
    result = get_func(5, 2)([file])
    assert result == 12


def test_d6_p1():
    file = resources.open_text(input, "day06.txt")
    result = get_func(6, 1)([file])
    assert result == 5934


def test_d6_p2():
    file = resources.open_text(input, "day06.txt")
    result = get_func(6, 2)([file])
    assert result == 26984457539


def test_d7_p1():
    file = resources.open_text(input, "day07.txt")
    result = get_func(7, 1)([file])
    assert result == 37


def test_d7_p2():
    file = resources.open_text(input, "day07.txt")
    result = get_func(7, 2)([file])
    assert result == 168


def test_d8_p1():
    file = resources.open_text(input, "day08.txt")
    result = get_func(8, 1)([file])
    assert result == 26


def test_d8_p2():
    file = resources.open_text(input, "day08.txt")
    result = get_func(8, 2)([file])
    assert result == 61229


def test_d9_p1():
    file = resources.open_text(input, "day09.txt")
    result = get_func(9, 1)([file])
    assert result == 15


def test_d9_p2():
    file = resources.open_text(input, "day09.txt")
    result = get_func(9, 2)([file])
    assert result == 1134


def test_d10_p1():
    file = resources.open_text(input, "day10.txt")
    result = get_func(10, 1)([file])
    assert result == 26397


def test_d10_p2():
    file = resources.open_text(input, "day10.txt")
    result = get_func(10, 2)([file])
    assert result == 288957


def test_d11_p1():
    file = resources.open_text(input, "day11.txt")
    result = get_func(11, 1)([file])
    assert result == 1656


def test_d11_p2():
    file = resources.open_text(input, "day11.txt")
    result = get_func(11, 2)([file])
    assert result == 195


def test_d12_p1():
    file = resources.open_text(input, "day12.txt")
    result = get_func(12, 1)([file])
    assert result == 226


def test_d12_p2():
    file = resources.open_text(input, "day12.txt")
    result = get_func(12, 2)([file])
    assert result == 3509


def test_d13_p1():
    file = resources.open_text(input, "day13.txt")
    result = get_func(13, 1)([file])
    assert result == 17


def test_d13_p2():
    file = resources.open_text(input, "day13.txt")
    result = get_func(13, 2)([file])
    assert result == 16

def test_d14_p1():
    file = resources.open_text(input, "day14.txt")
    result = get_func(14, 1)([file])
    assert result == 1588


def test_d14_p2():
    file = resources.open_text(input, "day14.txt")
    result = get_func(14, 2)([file])
    assert result == 2188189693529

def test_d15_p1():
    file = resources.open_text(input, "day15.txt")
    result = get_func(15, 1)([file])
    assert result == 40


def test_d15_p2():
    file = resources.open_text(input, "day15.txt")
    result = get_func(15, 2)([file])
    assert result == 315

def test_d16_p1():
    file = resources.open_text(input, "day16.txt")
    result = get_func(16, 1)([file])
    assert result == 31


def test_d16_p2():
    file = resources.open_text(input, "day16.txt")
    result = get_func(16, 2)([file])
    assert result == 54

def test_d16_p2_real():
    file = resources.open_text(input, "day16_real.txt")
    result = get_func(16, 2)([file])
    assert result == 12883091136209

def test_d17_p1():
    file = resources.open_text(input, "day17.txt")
    result = get_func(17, 1)([file])
    assert result == 45


def test_d17_p2():
    file = resources.open_text(input, "day17.txt")
    result = get_func(17, 2)([file])
    assert result == 112
