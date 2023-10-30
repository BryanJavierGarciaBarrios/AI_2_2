import random
import math

def generate_random_cities(num_cities):
    cities = []
    for i in range(num_cities):
        x, y = random.uniform(0, 100), random.uniform(0, 100)
        cities.append((x, y))
    return cities

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calculate_total_distance(cities, order):
    total_distance = 0
    for i in range(len(order) - 1):
        city1 = cities[order[i]]
        city2 = cities[order[i + 1]]
        total_distance += calculate_distance(city1, city2)
    return total_distance

def generate_initial_solution(cities):
    return random.sample(range(len(cities)), len(cities))

def neighbor_solution(solution):
    i, j = random.sample(range(len(solution)), 2)
    new_solution = solution[:]
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution
def simulated_annealing(cities, initial_temperature, cooling_rate, max_iterations):
    current_solution = generate_initial_solution(cities)
    current_distance = calculate_total_distance(cities, current_solution)
    best_solution = current_solution
    best_distance = current_distance

    temperature = initial_temperature

    for i in range(max_iterations):
        new_solution = neighbor_solution(current_solution)
        new_distance = calculate_total_distance(cities, new_solution)

        if new_distance < current_distance:
            current_solution = new_solution
            current_distance = new_distance
            if new_distance < best_distance:
                best_solution = new_solution
                best_distance = new_distance
        elif random.random() < math.exp((current_distance - new_distance) / temperature):
            current_solution = new_solution
            current_distance = new_distance

        temperature *= 1 - cooling_rate

    return best_solution, best_distance

# Parámetros del recocido simulado
num_cities = 20
initial_temperature = 1000
cooling_rate = 0.995
max_iterations = 10000

cities = generate_random_cities(num_cities)

best_solution, best_distance = simulated_annealing(cities, initial_temperature, cooling_rate, max_iterations)

print("Mejor recorrido encontrado:", best_solution)
print("Distancia total del mejor recorrido:", best_distance)
