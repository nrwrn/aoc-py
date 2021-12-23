import sys
from io import TextIOBase
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple
from dataclasses import dataclass


def parse(lines: TextIOBase) -> List[List[int]]:
    return [[int(char) for char in list(line.strip())] for line in lines]


def iter_neighbors(grid: List[List[Any]]) -> Iterable[Tuple[Any, List[Any]]]:
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            possible = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            yield cell, [
                grid[i][j]
                for i, j in possible
                if i in range(len(grid)) and j in range(len(grid[0]))
            ]


@dataclass
class Node:
    coord: Tuple[int, int, int]

    def __eq__(self, other):
        return self.coord == other.coord

    def __hash__(self):
        return hash(self.coord)


class Graph:
    start: Node
    end: Node
    nodes: Set[Node]
    edges: Dict[Node, Dict[Node, int]]

    def __init__(self, grid: List[List[int]]):
        self.nodes = set()
        pairs = []
        self.edges = {}
        for i, row in enumerate(grid):
            pair_row = []
            for j, weight in enumerate(row):
                in_node = Node((i, j, 0))
                out_node = Node((i, j, 1))
                self.set_edge(in_node, out_node, weight)
                pair_row.append((in_node, out_node))
                self.nodes.add(in_node)
                self.nodes.add(out_node)
            pairs.append(pair_row)
        for pair, neighbors in iter_neighbors(pairs):
            for n_in, _ in neighbors:
                self.set_edge(pair[1], n_in, 0)
        self.start = pairs[0][0][1]
        self.end = pairs[-1][-1][1]

    def set_edge(self, frm, to, weight):
        if frm not in self.edges:
            self.edges[frm] = {}
        self.edges[frm][to] = weight
    
    def get_path(self) -> Optional[int]:
        q: Set[Node] = self.nodes.copy()
        dist = {node: sys.maxsize for node in self.nodes}
        prev = {}
        dist[self.start] = 0

        while q:
            u = min(q, key=lambda node: dist[node])
            q.discard(u)
            print(u.coord)
            valid_edges = [(tgt, weight) for tgt, weight in self.edges[u].items() if tgt in q]
            for neighbor, weight in valid_edges:
                new_total = dist[u] + weight
                if new_total < dist[neighbor]:
                    dist[neighbor] = new_total
                    prev[neighbor] = u
            if u is self.end:
                return dist[u]
        return None


def part1(files: List[TextIOBase]) -> int:
    weight_grid = parse(files[0])
    graph = Graph(weight_grid)
    return graph.get_path() or 0


def increment(grid: List[List[int]], val: int) -> List[List[int]]:
    return [[1 + (cell + val - 1) % 9 for cell in row] for row in grid]


def part2(files: List[TextIOBase]) -> int:
    original_grid = parse(files[0])
    grid_row = [sum([increment([row], i)[0] for i in range(5)], []) for row in original_grid]
    weight_grid = sum([increment(grid_row, i) for i in range(5)], [])
    graph = Graph(weight_grid)
    return graph.get_path() or 0
