from data_models import Individual, KnapsackProblem

#  --- Funkcja Przystosowania (Wymaganie 3.5) ---

def calculate_fitness(individual: Individual, problem: KnapsackProblem) -> float:
    """
    Calculates the fitness value (total value) if weight <= capacity, else 0.
    """
    total_weight = 0
    total_value = 0
    
    for i, gene in enumerate(individual.chromosome):
        if gene == 1:
            item = problem.items[i]
            total_weight += item.weight
            total_value += item.value
            
    if total_weight > problem.capacity:
        individual.fitness = 0.0
    else:
        individual.fitness = float(total_value)
        
    individual.total_weight = total_weight
    return individual.fitness