
# --- Funkcja Importująca Dane (Przeniesiona z Kroku A.2, aby używać klas) ---

def import_data(file_name: str) -> KnapsackProblem:
    """
    Imports Knapsack problem data from a text file.
    """
    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
            
            problem_size = int(lines[0].strip()) 
            values = [int(v) for v in lines[1].split()]
            capacity = int(lines[2].strip())
            weights = [int(w) for w in lines[3].split()]
            
            if len(values) != len(weights):
                raise ValueError("Inconsistent number of values and weights.")
            
            items = []
            for i in range(len(values)):
                items.append(Item(i + 1, values[i], weights[i]))
                
            return KnapsackProblem(capacity, items)

    except Exception as e:
        print(f"Error loading data: {e}")
        return None