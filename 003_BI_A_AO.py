import heapq

def astar(graph, start, goal, heuristic):
    open_list = [(0, start, [])]
    closed_set = set()

    while open_list:
        f, current, path = heapq.heappop(open_list)

        if current == goal:
            return path + [current]

        if current in closed_set:
            continue

        closed_set.add(current)

        for neighbor, cost in graph.get(current, {}).items():
            if neighbor not in closed_set:
                g = len(path) + cost
                h = heuristic[neighbor]
                f = g + h
                heapq.heappush(open_list, (f, neighbor, path + [current]))

    return None

def ao_star(graph, start, goal, heuristic):
    open_list = [(0, start, [])]
    closed_set = set()

    while open_list:
        f, current, path = heapq.heappop(open_list)

        if current == goal:
            return path + [current]

        if current in closed_set:
            continue

        closed_set.add(current)

        for neighbor, cost in graph.get(current, {}).items():
            if neighbor not in closed_set:
                h = heuristic[neighbor]
                g = len(path) + cost
                f = max(g, f) + h
                heapq.heappush(open_list, (f, neighbor, path + [current]))

    return None

# Ejemplo de búsqueda A*
start_node = 'A'
goal_node = 'F'

# Definición del grafo
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'D': 2, 'E': 4},
    'C': {'F': 3},
    'D': {'E': 1},
    'E': {'F': 1},
    'F': {}
}

# Heurística de distancia Manhattan
heuristic = {
    'A': 3,
    'B': 2,
    'C': 3,
    'D': 1,
    'E': 1,
    'F': 0
}

path_astar = astar(graph, start_node, goal_node, heuristic)

if path_astar:
    print("Camino encontrado por A*:", path_astar)
else:
    print("No se encontró un camino por A*.")

# Ejemplo de búsqueda AO*
path_ao_star = ao_star(graph, start_node, goal_node, heuristic)

if path_ao_star:
    print("Camino encontrado por AO*:", path_ao_star)
else:
    print("No se encontró un camino por AO*.")
