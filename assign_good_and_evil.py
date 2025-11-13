from collections import deque


def assign_good_and_evil(graph):
    if graph is None:
        return None

    labeling = {}

    for start_node in graph.nodes():
        if start_node in labeling:
            continue

        labeling[start_node] = "good"
        queue = deque([start_node])

        while queue:
            current = queue.popleft()
            current_label = labeling[current]
            opposite_label = "evil" if current_label == "good" else "good"

            for neighbor in graph.neighbors(current):
                if neighbor not in labeling:
                    labeling[neighbor] = opposite_label
                    queue.append(neighbor)
                elif labeling[neighbor] != opposite_label:
                    return None

    return labeling