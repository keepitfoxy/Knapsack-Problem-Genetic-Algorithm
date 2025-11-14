print(f"=========================================================")
print("=============URUCHAMIANIE EWOLUCJI ALGORYTMU==============")
print(f"=========================================================")



# --- Potrzebne importy danych ---
import matplotlib.pyplot as plt
import copy 
from ga_core import import_data
from operators import (
    roulette_wheel_selection, 
    ranking_selection, 
    tournament_selection,
    single_point_crossover,
    two_point_crossover )
from data_models import KnapsackProblem, Individual
from main_experiment import run_and_collect_results, report_results_and_plot






def run_experiments_comparisons(data_file_name: str, scenarios: list, experiment_title: str):
    problem = import_data(data_file_name) 
    if problem is None:
        print(f"Pominięto eksperyment dla {data_file_name}: Nie udało się przeprowadzić ewolucji algorytmu.")
        return
    
    print(f"\n============================================================================")
    print(f"===URUCHAMIANIE EWOLUCJI ALGORYTMU {experiment_title} dla {data_file_name} ===")
    print(f"==============================================================================")
    results = run_and_collect_results(problem, scenarios)
    report_results_and_plot(f"{experiment_title} \n(Plik: {data_file_name})", results)






if __name__ == "__main__":
    
    DATA_FILES = [

# --- Dane low dimensional ---

    "dane AG/low-dimensional/f1_l-d_kp_10_269",
    "dane AG/low-dimensional/f2_l-d_kp_20_878",
    "dane AG/low-dimensional/f5_l-d_kp_15_375",
    "dane AG/low-dimensional/f10_l-d_kp_20_879",

# --- Dane large dimensional ---

    "dane AG/large_scale/knapPI_1_1000_1000_1",
    "dane AG/large_scale/knapPI_1_2000_1000_1"
    ]
    
    BASE_PARAMS = {
        'pop_size': 100, 
        'generations': 150,
        'p_crossover': 0.85,
        'p_mutation': 0.05,  
        'selection_func': roulette_wheel_selection, 
        'crossover_func': single_point_crossover
    }

    



# --- OCENA 3.5 ---
# --- Wykresy dla różnych współczynników mutacji i krzyżowania ---

    scenarios_rates = [
        {
            'label': 'Baseline: Pc=0.85, Pm=0.05', 
            'p_crossover': 0.85, 'p_mutation': 0.05,
            **{k: v for k, v in BASE_PARAMS.items() if k not in ['p_crossover', 'p_mutation']}
        },
        {
            'label': 'High Crossover: Pc=0.95, Pm=0.05', 
            'p_crossover': 0.95, 'p_mutation': 0.05,
            **{k: v for k, v in BASE_PARAMS.items() if k not in ['p_crossover', 'p_mutation']}
        },
        {
            'label': 'Low Mutation: Pc=0.85, Pm=0.01', 
            'p_crossover': 0.85, 'p_mutation': 0.01,
            **{k: v for k, v in BASE_PARAMS.items() if k not in ['p_crossover', 'p_mutation']}
        },
        {
            'label': 'High Mutation: Pc=0.85, Pm=0.10', 
            'p_crossover': 0.85, 'p_mutation': 0.10,
            **{k: v for k, v in BASE_PARAMS.items() if k not in ['p_crossover', 'p_mutation']}
        }
    ]






# --- OCENA 4.5 ---
# --- Selekcja Rankingowa vs Ruletkowa ---

    scenarios_selection_4_5 = [
        {
            'label': 'Selection: Roulette', 
            'selection_func': roulette_wheel_selection,
            **{k: v for k, v in BASE_PARAMS.items() if k not in ['selection_func']}
        },
        {
            'label': 'Selection: Ranking', 
            'selection_func': ranking_selection,
            **{k: v for k, v in BASE_PARAMS.items() if k not in ['selection_func']}
        }
    ]

# --- Single vs Two piont crossover ---

    scenarios_crossover_4_5 = [
        {
            'label': 'Crossover: Single-Point', 
            'crossover_func': single_point_crossover,
            **{k: v for k, v in BASE_PARAMS.items() if k not in ['crossover_func']}
        },
        {
            'label': 'Crossover: Two-Point', 
            'crossover_func': two_point_crossover,
            **{k: v for k, v in BASE_PARAMS.items() if k not in ['crossover_func']}
        }
    ]






# --- OCENA 5.0 ---
# --- Wykresy porównujące selekcję rankingową, ruletkową oraz turniejową ---

    scenarios_selection_5_0 = [
        {
            'label': 'Selection: Roulette', 
            'selection_func': roulette_wheel_selection,
            **{k: v for k, v in BASE_PARAMS.items() if k not in ['selection_func']}
        },
        {
            'label': 'Selection: Ranking', 
            'selection_func': ranking_selection,
            **{k: v for k, v in BASE_PARAMS.items() if k not in ['selection_func']}
        },
        {
            'label': 'Selection: Tournament', 
            'selection_func': tournament_selection,
            **{k: v for k, v in BASE_PARAMS.items() if k not in ['selection_func']}
        }
    ]





# --- Pętla ---

    for filename in DATA_FILES:
        print(f"\n=======================================================")
        print(f"=== Rozpoczynam przetwarzanie zbioru: {filename} ========")
        print(f"=========================================================")
        
        
        run_experiments_comparisons(filename, scenarios_rates, 
                                  experiment_title="Ocena 3.5: Różne współczynniki mutacji i krzyżowania")
        
        
        run_experiments_comparisons(filename, scenarios_selection_4_5, 
                                  experiment_title="Ocena 4.5: Selekcja Ruletkowa vs Rankingowa")
        
        
        run_experiments_comparisons(filename, scenarios_crossover_4_5, 
                                  experiment_title="Ocena 4.5: Single vs Two piont crossover")
        
        
        run_experiments_comparisons(filename, scenarios_selection_5_0, 
                                  experiment_title="Ocena 5.0: Porównanie Selekcji (Ruletka, Ranking, Turniej)")
        

        print(f"\n=======================================================")
        print(f"--- URUCHAMIANIE EWOLUCJI ALGORYTMU ZAKOŃCZONE ---")
        print(f"=========================================================")