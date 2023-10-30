import random

def hill_climbing(problem, max_iterations):
    current_state = problem.initial_state()
    
    for _ in range(max_iterations):
        neighbors = problem.get_neighbors(current_state)
        if not neighbors:
            break
        
        neighbor = max(neighbors, key=lambda x: problem.get_value(x))
        
        if problem.get_value(neighbor) <= problem.get_value(current_state):
            break
        
        current_state = neighbor
    
    return current_state

class OptimizationProblem:
    def __init__(self, initial_state):
        self.current_state = initial_state

    def initial_state(self):
        return self.current_state

    def get_neighbors(self, state):
        # Genera vecinos de manera aleatoria para ilustrar el concepto.
        neighbors = [state + random.uniform(-0.1, 0.1) for _ in range(3)]
        return neighbors

    def get_value(self, state):
        # Esta es una función de ejemplo que se podría optimizar.
        # Debes reemplazarla por tu propia función de evaluación.
        return -sum((state_i - 3) ** 2 for state_i in state)

# Ejemplo de uso
if __name__ == "__main__":
    initial_state = [1.0, 2.0, 3.0]
    problem = OptimizationProblem(initial_state)

    max_iterations = 1000
    final_state = hill_climbing(problem, max_iterations)

    print("Estado inicial:", initial_state)
    print("Estado final:", final_state)
