from typing import Callable
import random
from data_models import Item, KnapsackProblem, generate_random_individual, Individual
from operators import calculate_fitness, mutation, repair_individual


FitnessFunc = Callable[[Individual, KnapsackProblem], float]
SelectionFunc = Callable[[list[Individual]], Individual]
CrossoverFunc = Callable[[Individual, Individual], tuple[Individual, Individual]]




def import_data(file_name: str) -> KnapsackProblem:
   
    try:
        with open(file_name, 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
            
            if not lines:
                raise ValueError("Plik jest pusty.")

            first_line_parts = lines[0].split()

            if len(first_line_parts) == 2:
                try:
                    problem_size = float(first_line_parts[0])
                    capacity = float(first_line_parts[1])
                    
                    items = []
                    for i, line in enumerate(lines[1:]):
                        parts = line.split()
                        if len(parts) == 2:
                            value = float(parts[0])
                            weight = float(parts[1])
                            items.append(Item(i + 1, value, weight))
                        else:
                            raise ValueError(f"Błędny format linii przedmiotu: {line}")
                        
                    if len(items) != problem_size:
                        raise ValueError(f"Plik deklaruje {problem_size} przedmiotów, a znaleziono {len(items)}.")
                    return KnapsackProblem(capacity, items)
                except (ValueError, IndexError):
                    pass 

            if len(lines) >= 4:
                try:
                    problem_size = int(lines[0])
                    values = [int(v) for v in lines[1].split()]
                    capacity = int(lines[2])
                    weights = [int(v) for v in lines[3].split()]
                    
                    if len(values) != problem_size or len(weights) != problem_size:
                        raise ValueError("Niezgodna liczba przedmiotów, wartości lub wag.")
                    
                    items = []
                    for i in range(problem_size):
                        items.append(Item(i + 1, values[i], weights[i]))
                    return KnapsackProblem(capacity, items)
                except (ValueError, IndexError) as e:
                    raise ValueError(f"Nie udało się wczytać jako format 2: {e}")

            raise ValueError(f"Nie udało się sparsować pliku {file_name}. Nieznany format.")
    except Exception as e:
        print(f"Error loading data from {file_name}: {e}")
        return None



# --- Main Evolution Script ---

def genetic_algorithm(
    problem: KnapsackProblem,
    population_size: int,
    generations: int,
    crossover_probability: float, 
    mutation_probability: float,  
    selection_func: SelectionFunc,
    crossover_func: CrossoverFunc,
    initial_inclusion_prob: float = 0.5 
) -> tuple [Individual, list[float]]:
    
    chromosome_length = problem.num_items
    fitness_history = []
    population = [generate_random_individual(chromosome_length, initial_inclusion_prob) 
                  for _ in range(population_size)]

    for gen in range(generations):
        
        for individual in population:
            calculate_fitness(individual, problem)
        best_individual = max(population, key=lambda i: i.fitness)
        fitness_history.append(best_individual.fitness)
        new_population = []

        while len(new_population) < population_size:
            parent1 = selection_func(population)
            parent2 = selection_func(population)
            if random.random() < crossover_probability:
                offspring1, offspring2 = crossover_func(parent1, parent2)
            else:
                offspring1, offspring2 = Individual(parent1.chromosome[:]), Individual(parent2.chromosome[:])
            mutation(offspring1, mutation_probability)
            mutation(offspring2, mutation_probability)
            repair_individual(offspring1, problem)
            repair_individual(offspring2, problem)
            new_population.append(offspring1)

            if len(new_population) < population_size:
                new_population.append(offspring2)
        population = new_population
    
    for individual in population:
        calculate_fitness(individual, problem)
    final_best_individual = max(population, key=lambda i: i.fitness)

    return final_best_individual, fitness_history