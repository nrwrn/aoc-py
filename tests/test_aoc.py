from aoc.aoc import get_func
from io import TextIOWrapper
from importlib import resources

from . import input

def test_d1_p1():
    file = resources.open_text(input, 'day1.txt')
    result = get_func(1, 1)([file])
    assert result == 7

def test_d1_p2():
    file = resources.open_text(input, 'day1.txt')
    result = get_func(1, 2)([file])
    assert result == 5

def test_d5_p1():
    file = resources.open_text(input, 'day5.txt')
    result = get_func(5, 1)([file])
    assert result == 5

def test_d5_p2():
    file = resources.open_text(input, 'day5.txt')
    result = get_func(5, 2)([file])
    assert result == 12 
