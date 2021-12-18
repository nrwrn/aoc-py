from io import TextIOBase
from typing import Dict, Iterable, List, Set, Tuple


def make_graph(lines: TextIOBase) -> Dict[str, List[str]]:
    connections = [tuple(line.strip().split("-")) for line in lines]
    graph = {}
    for a, b in connections:
        if a not in graph.keys():
            graph[a] = []
        if b not in graph.keys():
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


def visit(node: str, graph: Dict[str, List[str]], blocked: Set[str], goojf: bool) -> int:
    new_blocked = blocked
    if not node.isupper():
        new_blocked = blocked.copy()
        new_blocked.add(node)
    neighbors = [n for n in graph[node] if n not in blocked]
    blocked_neighbors = [n for n in graph[node] if n in blocked and n not in ["start", "end"]]
    acc = 0
    if "end" in neighbors:
        neighbors.remove("end")
        acc += 1
    for neighbor in neighbors:
        acc += visit(neighbor, graph, new_blocked, goojf)
    if goojf: # "get out of jail free"
        for neighbor in blocked_neighbors:
            acc += visit(neighbor, graph, new_blocked, False)
    return acc



def part1(files: List[TextIOBase]) -> int:
    graph = make_graph(files[0])
    return visit("start", graph, set(), False)


def part2(files: List[TextIOBase]) -> int:
    graph = make_graph(files[0])
    return visit("start", graph, set(), True)
