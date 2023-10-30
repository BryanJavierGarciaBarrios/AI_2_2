import random

def beam_search(problem, beam_width, max_iterations):
    current_states = [problem.initial_state() for _ in range(beam_width)]
    
    for _ in range(max_iterations):
        next_states = []

        for state in current_states:
            neighbors = problem.get_neighbors(state)
            next_states.extend(neighbors)
        
        next_states.sort(key=lambda x: problem.get_value(x), reverse=True)
        current_states = next_states[:beam_width]
    
    best_solution = max(current_states, key=lambda x: problem.get_value(x))
    
    return best_solution

class OptimizationProblem:
    def initial_state(self):
        return [1, 2, 3]  # Ejemplo de solución inicial

    def get_neighbors(self, state):
        neighbors = []
        for _ in range(5):
            neighbor = state[:]
            index = random.randint(0, len(neighbor) - 1)
            neighbor[index] += random.uniform(-0.1, 0.1)
            neighbors.append(neighbor)
        return neighbors

    def get_value(self, state):
        # Esta es una función de ejemplo que se podría optimizar.
        # Debes reemplazarla por tu propia función de evaluación.
        return -sum((x - 3) ** 2 for x in state)

# Ejemplo de uso
if __name__ == "__main__":
    problem = OptimizationProblem()

    beam_width = 5
    max_iterations = 100

    final_solution = beam_search(problem, beam_width, max_iterations)

    print("Mejor solución encontrada:", final_solution)
