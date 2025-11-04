import random

class Item:
    def __init__(self, index, value, weight):
        self.index = index
        self.value = value
        self.weight = weight
    
    def __repr__(self):
        return f"Item(idx={self.index}, w={self.weight}, v={self.value})"

class KnapsackProblem:
    """Problem data"""
    def __init__(self, capacity, items):
        self.capacity = capacity
        self.items = items
        self.num_items = len(items)

class Individual:
    """Single chromosome"""
    def __init__(self, chromosome: list[int]):
        self.chromosome = chromosome
        self.fitness = 0.0
        self.total_weight = 0
    
    def __len__(self):
        return len(self.chromosome)
    
    def __repr__(self):
        repr_chrom = str(self.chromosome[:10] + ['...'] if len(self.chromosome) > 10 else self.chromosome)
        return f"Individual(Fitness={self.fitness:.2f}, Weight={self.total_weight}, Chrom={repr_chrom})"

def generate_random_individual(length: int) -> Individual:
    """Random chromosome with given length"""
    chromosome = [random.randint(0, 1) for _ in range(length)]
    return Individual(chromosome)