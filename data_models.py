import random

class Item:
    def __init__(self, index, value, weight):
        self.index = index
        self.value = value
        self.weight = weight
    
    def __repr__(self):
        return f"Item(idx={self.index}, w={self.weight}, v={self.value})"

class KnapsackProblem:
    def __init__(self, capacity, items):
        self.capacity = capacity
        self.items = items
        self.num_items = len(items)

class Individual:
    def __init__(self, chromosome: list[int]):
        self.chromosome = chromosome
        self.fitness = 0.0
        self.total_weight = 0
    
    def __len__(self):
        return len(self.chromosome)
    
    def __repr__(self):
        repr_chrom = str(self.chromosome[:10] + ['...'] if len(self.chromosome) > 10 else self.chromosome)
        return f"Individual(Fitness={self.fitness:.2f}, Weight={self.total_weight}, Chrom={repr_chrom})"

# --- Tworzy losowy chromosom o podanej długości ---
# --- Prawdopodobieństwo, że dany gen będzie miał wartość 1 (przedmiot zostanie wzięty) ---
# --- Domyślnie (50/50) ---

def generate_random_individual(length: int, inclusion_probability: float = 0.5) -> Individual:
    chromosome = [1 if random.random() < inclusion_probability else 0 for _ in range(length)]
    return Individual(chromosome)