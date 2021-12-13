import importlib
import click
import sys
from typing import List

@click.command()
@click.option('-d', '--day')
@click.option('-p', '--part')
@click.argument('files', nargs=-1, type=click.File('r'))
def root_command(day: int, part: int, files: List[click.File]):
    module_name = f"aoc.days.day{day}"
    try:
        mod = importlib.import_module(module_name)
        func = getattr(mod, f"part{part}")
    except (ModuleNotFoundError, AttributeError):
        print(f"No such module/function {module_name}")
        sys.exit(-1)
    print(get_func(day, part)(files))

def get_func(day: int, part: int):
    module_name = f"aoc.days.day{day}"
    try:
        mod = importlib.import_module(module_name)
        func = getattr(mod, f"part{part}")
    except (ModuleNotFoundError, AttributeError):
        print(f"No such module/function {module_name}")
        sys.exit(-1)
    return func