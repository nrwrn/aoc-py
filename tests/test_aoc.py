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
    assert result == None
