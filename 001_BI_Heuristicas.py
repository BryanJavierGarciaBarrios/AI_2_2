import heapq

class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic

    def __lt__(self, other):
        return self.total_cost < other.total_cost

def astar_search(initial_state, goal_state, get_neighbors, heuristic):
    open_list = []
    closed_set = set()

    start_node = Node(initial_state, None, None, 0, heuristic(initial_state, goal_state))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            return build_path(current_node)

        closed_set.add(current_node.state)

        for neighbor_state, action, step_cost in get_neighbors(current_node.state):
            if neighbor_state not in closed_set:
                neighbor_node = Node(neighbor_state, current_node, action, current_node.cost + step_cost, heuristic(neighbor_state, goal_state))
                heapq.heappush(open_list, neighbor_node)

    return None

def build_path(node):
    path = []
    while node:
        if node.action:
            path.append((node.action, node.state))
        node = node.parent
    return list(reversed(path))

# Heurística: distancia de Manhattan para el problema del 8-puzzle
def manhattan_distance(state, goal_state):
    size = int(len(state) ** 0.5)
    distance = 0
    for i in range(len(state)):
        if state[i] == 0:
            continue
        goal_index = goal_state.index(state[i])
        current_row, current_col = divmod(i, size)
        goal_row, goal_col = divmod(goal_index, size)
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

# Ejemplo del problema del 8-puzzle
initial_state = [1, 2, 3, 4, 5, 6, 7, 0, 8]
goal_state = [1, 2, 3, 4, 5, 8, 7, 6, 0]

def get_8puzzle_neighbors(state):
    size = int(len(state) ** 0.5)
    empty_index = state.index(0)
    neighbors = []
    if empty_index % size > 0:
        neighbors.append((state[:empty_index - 1] + [0] + [state[empty_index - 1]] + state[empty_index + 1:], 'Left', 1))
    if empty_index % size < size - 1:
        neighbors.append((state[:empty_index] + [state[empty_index + 1]] + [0] + state[empty_index + 2:], 'Right', 1))
    if empty_index >= size:
        neighbors.append((state[:empty_index - size] + [0] + state[empty_index - size + 1:empty_index] + [state[empty_index - size]] + state[empty_index + 1:], 'Up', 1))
    if empty_index < len(state) - size:
        neighbors.append((state[:empty_index] + state[empty_index + size] + state[empty_index + 1:empty_index + size] + [0] + state[empty_index + size + 1:], 'Down', 1))
    return neighbors

path = astar_search(initial_state, goal_state, get_8puzzle_neighbors, manhattan_distance)

if path:
    print("Solución encontrada:")
    for action, state in path:
        print(f"{action}: {state}")
else:
    print("No se encontró una solución.")
