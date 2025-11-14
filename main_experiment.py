import matplotlib.pyplot as plt
import copy 
from ga_core import genetic_algorithm, import_data
from operators import * 
from data_models import KnapsackProblem, Individual





def run_and_collect_results(
    problem_data: KnapsackProblem, 
    scenarios: list
) -> list[dict]:
    
    results = []
    
    print(f"=========================================================")
    print("================ STARTING EXPERIMENT =====================")
    print(f"=========================================================")

    for scenario in scenarios:
        
        # run the GA, using a deep copy of the problem data
        best_individual, fitness_history = genetic_algorithm(
            problem=copy.deepcopy(problem_data), 
            population_size=scenario['pop_size'],
            generations=scenario['generations'],
            crossover_probability=scenario['p_crossover'],
            mutation_probability=scenario['p_mutation'],
            selection_func=scenario['selection_func'],
            crossover_func=scenario['crossover_func']
        )
        
        # save results
        results.append({
            'label': scenario['label'],
            'final_fitness': best_individual.fitness,
            'final_weight': best_individual.total_weight,
            'fitness_history': fitness_history, # list of fitness values per iteration
        })
        
        print(f"Scenario '{scenario['label']}' finished. Max Fitness: {best_individual.fitness:.2f} (Weight: {best_individual.total_weight})")

    return results






def report_results_and_plot(experiment_name: str, results: list[dict]):
    
    # final results table (console)
    print(f"\n--- EXPERIMENT REPORT: {experiment_name} ---")
    print("\n[Table 1: Best Final Results]")
    print(f"| {'SCENARIO':<40} | {'MAX FITNESS':<15} | {'WEIGHT':<10} |")
    print(f"|{'-'*42}|{'-'*17}|{'-'*12}|")
    for r in results:
        print(f"| {r['label']:<40} | {r['final_fitness']:<15.2f} | {r['final_weight']:<10} |")

    # visualization
    import matplotlib.pyplot as plt

    plt.figure(figsize=(12, 7))
    
    for r in results:
        plt.plot(r['fitness_history'], label=r['label'], linewidth=2)
    
    # plot details
    plt.title(experiment_name)
    plt.xlabel("Iteration")
    plt.ylabel("Best Fitness Value")
    plt.legend()
    plt.grid(True, linestyle='--')
    plt.tight_layout()
    plt.show()