import random

def objective_function(x):
    return x**2

def tabu_search(start_x, max_iter, tabu_size, step_size):
    current_x = start_x
    best_x = current_x
    tabu_list = []

    for i in range(max_iter):
        neighbors = [current_x - step_size, current_x + step_size]
        neighbors = [x for x in neighbors if x >= 0]  # Limitamos a valores positivos

        best_neighbor = None
        best_neighbor_value = float('inf')

        for neighbor in neighbors:
            if neighbor not in tabu_list:
                neighbor_value = objective_function(neighbor)
                if neighbor_value < best_neighbor_value:
                    best_neighbor = neighbor
                    best_neighbor_value = neighbor_value

        current_x = best_neighbor

        if best_neighbor_value < objective_function(best_x):
            best_x = best_neighbor

        tabu_list.append(best_neighbor)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

    return best_x

# Parámetros de búsqueda tabú
start_x = random.uniform(0, 10)  # Valor inicial aleatorio
max_iterations = 100
tabu_size = 10
step_size = 0.1

result = tabu_search(start_x, max_iterations, tabu_size, step_size)
print(f"El mínimo local encontrado es en x = {result} con un valor de la función f(x) = {objective_function(result)}")
