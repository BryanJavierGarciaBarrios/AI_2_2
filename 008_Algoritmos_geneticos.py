import random

# Parámetros del algoritmo genético
population_size = 100
chromosome_length = 20
mutation_rate = 0.1
generations = 100

# Cadena de destino a encontrar
target_string = "10101010101010101010"

# Función de inicialización de la población
def initialize_population(pop_size, chrom_length):
    population = []
    for _ in range(pop_size):
        chromosome = ''.join(random.choice("01") for _ in range(chrom_length))
        population.append(chromosome)
    return population

# Función de selección de padres (torneo binario)
def select_parents(population, fitness_scores, num_parents):
    parents = []
    for _ in range(num_parents):
        candidate_indices = random.sample(range(len(population)), 2)
        candidate1 = population[candidate_indices[0]]
        candidate2 = population[candidate_indices[1]]
        fitness1 = fitness_scores[candidate_indices[0]]
        fitness2 = fitness_scores[candidate_indices[1]]
        selected_parent = candidate1 if fitness1 > fitness2 else candidate2
        parents.append(selected_parent)
    return parents

# Función de cruce (un punto de cruce)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Función de mutación (cambiar un bit)
def mutate(chromosome, mutation_rate):
    mutated_chromosome = ""
    for bit in chromosome:
        if random.random() < mutation_rate:
            mutated_chromosome += "0" if bit == "1" else "1"
        else:
            mutated_chromosome += bit
    return mutated_chromosome

# Función de evaluación de aptitud (fitness)
def evaluate_fitness(chromosome, target):
    fitness = sum(1 for bit1, bit2 in zip(chromosome, target) if bit1 == bit2)
    return fitness

# Algoritmo genético
def genetic_algorithm(target, pop_size, chrom_length, mutation_rate, generations):
    population = initialize_population(pop_size, chrom_length)
    for generation in range(generations):
        fitness_scores = [evaluate_fitness(chrom, target) for chrom in population]
        max_fitness = max(fitness_scores)
        best_chromosome = population[fitness_scores.index(max_fitness)]

        print(f"Generación {generation}: {best_chromosome} (Fitness: {max_fitness}/{chrom_length})")

        if best_chromosome == target:
            break

        parents = select_parents(population, fitness_scores, pop_size // 2)
        new_population = []
        while len(new_population) < pop_size:
            parent1, parent2 = random.choice(parents), random.choice(parents)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population

    return best_chromosome

# Ejecución del algoritmo genético
result = genetic_algorithm(target_string, population_size, chromosome_length, mutation_rate, generations)
print(f"Solución encontrada: {result}")
