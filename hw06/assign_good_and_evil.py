from collections import deque
from typing import Any, Dict, Iterable, List


def assign_good_and_evil(graph: Any) -> Dict[Any, str] | None:
    if graph is None:
        return None

    try:
        nodes = list(_get_nodes(graph))
    except AttributeError:
        raise AttributeError(
            "Unable to determine the set of nodes from the provided graph."
        )

    labels: Dict[Any, str] = {}

    for node in nodes:
        if node in labels:
            continue

        labels[node] = "good"
        queue: deque[Any] = deque([node])

        while queue:
            current = queue.popleft()
            current_label = labels[current]
            opposite_label = "evil" if current_label == "good" else "good"

            for neighbor in _get_neighbors(graph, current):
                if neighbor not in labels:
                    labels[neighbor] = opposite_label
                    queue.append(neighbor)
                elif labels[neighbor] != opposite_label:
                    return None

    return labels


def _get_nodes(graph: Any) -> Iterable[Any]:
    node_attrs = (
        "nodes",
        "get_nodes",
        "vertices",
    )

    for attr in node_attrs:
        if hasattr(graph, attr):
            candidate = getattr(graph, attr)
            nodes = candidate() if callable(candidate) else candidate
            if nodes is not None:
                return nodes

    if hasattr(graph, "adjacency_list"):
        return graph.adjacency_list.keys()
    if hasattr(graph, "adjacency"):
        return graph.adjacency.keys()

    raise AttributeError("Graph object does not expose its nodes.")


def _get_neighbors(graph: Any, node: Any) -> List[Any]:
    neighbor_attrs = (
        "neighbors",
        "get_neighbors",
        "adjacent_nodes",
        "adjacent",
    )

    for attr in neighbor_attrs:
        if hasattr(graph, attr):
            candidate = getattr(graph, attr)
            try:
                neighbors = candidate(node)
            except TypeError:
                continue
            if neighbors is not None:
                return list(neighbors)

    if hasattr(graph, "adjacency_list"):
        return list(graph.adjacency_list.get(node, []))
    if hasattr(graph, "adjacency"):
        return list(graph.adjacency.get(node, []))

    raise AttributeError("Graph object does not expose neighbour information.")


