from dataclasses import dataclass
from typing import Union


@dataclass
class Path:
    cost: int
    vertexes: list

@dataclass
class Node:
    id: int
    path_cost: int


GRAPH = {
    1: [Node(2, 6), Node(4, 2)],
    2: [Node(5, 3), Node(4, 7), Node(1, 1)],
    3: [],
    4: [Node(6, 3), Node(3, 9), Node(2,10)],
    5: [],
    6: [Node(1, 4), Node(3, 5)],
}


def shortest_path(start: int, end: int, graph: dict) -> Union[Path, None]:
    if start == end:
        return Path(0, [start])
    if graph[start] == []:
        return None
    
    # for nodes in graph[start] :
    #     if nodes[0]
    # return Path(9, [1, 2, 5])


def verify(start: int, end: int, graph: dict, path_exists: bool, cost: int = None):
    print(f"Testing the path from {start} to {end}: ", end="")
    try:
        result = shortest_path(start, end, graph)
        if path_exists:
            assert result is not None
            assert result.vertexes[0] == start
            assert result.vertexes[-1] == end
            somme = 0
            for a, b in zip(result.vertexes, result.vertexes[1:]):
                assert [node for node in graph[a] if node.id == b]
                somme += [node.path_cost for node in graph[a] if node.id == b][0]                
            assert somme == result.cost == cost
        else:
            assert result is None
    except:
        print("ERROR...")
        return False
    print("OK!")


# a = shortest_path(1,1,GRAPH)
# print(a.cost)


verify(start=1, end=5, graph=GRAPH, path_exists=True, cost=9)
verify(start=2, end=5, graph=GRAPH, path_exists=True, cost=3)
verify(start=3, end=5, graph=GRAPH, path_exists=False)
verify(start=4, end=5, graph=GRAPH, path_exists=True, cost=10)
verify(start=4, end=2, graph=GRAPH, path_exists=True, cost=7)
verify(start=1, end=1, graph=GRAPH, path_exists=True, cost=0)
