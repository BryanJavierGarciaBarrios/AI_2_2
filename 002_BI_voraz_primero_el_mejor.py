# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

import heapq

def best_first_search(graph, start, goal, heuristic):
    open_set = [(heuristic[start], start)]
    came_from = {}
    while open_set:
        _, current_node = heapq.heappop(open_set)

        if current_node == goal:
            return reconstruct_path(came_from, current_node)

        for neighbor, cost in graph[current_node]:
            if neighbor not in came_from:
                came_from[neighbor] = current_node
                heapq.heappush(open_set, (heuristic[neighbor], neighbor))

    return None

def reconstruct_path(came_from, current_node):
    path = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        path.append(current_node)
    path.reverse()
    return path

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos un grafo de ejemplo donde cada arista tiene un costo
    graph = {
        'A': [('B', 1), ('C', 3)],
        'B': [('A', 1), ('D', 2), ('E', 4)],
        'C': [('A', 3), ('F', 2)],
        'D': [('B', 2)],
        'E': [('B', 4), ('F', 1)],
        'F': [('C', 2), ('E', 1), ('G', 3)],
        'G': [('F', 3)]
    }

    start_node = 'B'
    goal_node = 'F'

    # Definimos una heurística simple basada en la distancia en línea recta
    heuristic = {
        'A': 7,
        'B': 6,
        'C': 5,
        'D': 2,
        'E': 4,
        'F': 2,
        'G': 0
    }

    path = best_first_search(graph, start_node, goal_node, heuristic)

    if path:
        print(f"Camino de {start_node} a {goal_node}: {path}")
    else:
        print(f"No se encontró un camino de {start_node} a {goal_node}.")
