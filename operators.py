import random
from data_models import Individual, KnapsackProblem





#  --- Calculate fitness ---

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





# --- Selections ---

# --- Roulette wheel selection ---

def roulette_wheel_selection(population: list[Individual]) -> Individual:
    """Roulette Wheel Selection"""
    sum_fitness = sum(i.fitness for i in population)
    if sum_fitness == 0:
        return random.choice(population)
    
    pick = random.uniform(0, sum_fitness)
    
    cumulative_sum = 0
    for individual in population:
        cumulative_sum += individual.fitness
        if cumulative_sum >= pick:
            return individual
    return population[-1]





# --- tournament selection ---

def tournament_selection(population: list['Individual'], tournament_size: int = 3) -> 'Individual':
    """
    Default tournament size k=3
    """
 
    if tournament_size > len(population):
        tournament_size = len(population) # Używamy całej populacji
        
    tournament = random.sample(population, tournament_size)
    
    # best fit
    winner = max(tournament, key=lambda i: i.fitness)
    
    return winner





# --- ranking selection ---

def ranking_selection(population: list[Individual]) -> Individual:
    n = len(population)
    sorted_population = sorted(population, key=lambda i: i.fitness, reverse=True)
    chances = [(n - i) for i in range(n)]
    total_chances = sum(chances)

    if total_chances == 0:
        return random.choice(population)
    
    pick = random.uniform(0, total_chances)
    cumulative_sum = 0

    for i, individual in enumerate(sorted_population):
        cumulative_sum += chances[i]
        if cumulative_sum >= pick:
            return individual
        
    return sorted_population[-1]






# --- Single point Crossovers ---

def single_point_crossover(parent1: Individual, parent2: Individual) -> tuple[Individual, Individual]:
    """Single-Point Crossover"""
    length = len(parent1)
    crossover_point = random.randint(1, length - 1)
    
    offspring_chromosome1 = parent1.chromosome[:crossover_point] + parent2.chromosome[crossover_point:]
    offspring_chromosome2 = parent2.chromosome[:crossover_point] + parent1.chromosome[crossover_point:]
    
    return Individual(offspring_chromosome1), Individual(offspring_chromosome2)






# --- Two point Crossovers ---

def two_point_crossover(parent1: 'Individual', parent2: 'Individual') -> tuple['Individual', 'Individual']:
    length = len(parent1)
    
    # picking two different random points
    crossover_points = sorted(random.sample(range(1, length), 2))
    point1, point2 = crossover_points[0], crossover_points[1]

    # descendant 1
    offspring_chromosome1 = (
        parent1.chromosome[:point1] + 
        parent2.chromosome[point1:point2] + 
        parent1.chromosome[point2:]
    )
    
    # descendant 2
    offspring_chromosome2 = (
        parent2.chromosome[:point1] + 
        parent1.chromosome[point1:point2] + 
        parent2.chromosome[point2:]
    )
    
    return Individual(offspring_chromosome1), Individual(offspring_chromosome2)






# --- Mutations ---

def mutation(individual: Individual, mutation_probability: float) -> None:
    """Mutation operator"""
    for i in range(len(individual)):
        if random.random() < mutation_probability:
            individual.chromosome[i] = 1 - individual.chromosome[i]  # Flipping bit