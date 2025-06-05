from dataclasses import dataclass
import random

# ---------------------------
# Definice datových struktur
# ---------------------------
@dataclass
class Item:
    name: str
    weight: float
    value: float

# Seznam položek (můžeš upravit nebo rozšířit)
items = [
    Item("Notebook", 3.0, 2000),
    Item("Foťák", 1.5, 1500),
    Item("Kniha", 0.5, 300),
    Item("Mobil", 0.3, 800),
    Item("Sluchátka", 0.4, 400),
    Item("Lahev s vodou", 1.0, 150),
    Item("Bunda", 2.0, 700),
    Item("Peněženka", 0.2, 200),
    Item("Powerbanka", 0.6, 600),
    Item("Hodinky", 0.2, 1000)
]

# Parametry problému
MAX_WEIGHT = 7.0
POPULATION_SIZE = 50
GENERATIONS = 100
MUTATION_RATE = 0.05

# ---------------------------
# Genetický algoritmus
# ---------------------------
def generate_individual(n_items):
    return [random.randint(0, 1) for _ in range(n_items)]

def generate_population(size, n_items):
    return [generate_individual(n_items) for _ in range(size)]

def fitness(individual, items, max_weight):
    total_weight = total_value = 0
    for gene, item in zip(individual, items):
        if gene == 1:
            total_weight += item.weight
            total_value += item.value
    if total_weight > max_weight:
        return 0  # penalizace za překročení hmotnosti
    # nový fitness: kombinace hodnoty a počtu položek (více věcí = lepší využití prostoru)
    item_count = sum(individual)
    return total_value + item_count * 10  # malý bonus za počet položek

def selection(population, fitnesses):
    return random.choices(population, weights=fitnesses, k=2)

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

def mutate(individual, mutation_rate):
    return [gene if random.random() > mutation_rate else 1 - gene for gene in individual]

# ---------------------------
# Hlavní běh algoritmu
# ---------------------------

def run_genetic_algorithm():
    population = generate_population(POPULATION_SIZE, len(items))

    for gen in range(GENERATIONS):
        fitnesses = [fitness(ind, items, MAX_WEIGHT) for ind in population]
        new_population = []

        for _ in range(POPULATION_SIZE):
            parent1, parent2 = selection(population, fitnesses)
            child = crossover(parent1, parent2)
            child = mutate(child, MUTATION_RATE)
            new_population.append(child)

        population = new_population

    # Vyhodnocení nejlepšího řešení
    fitnesses = [fitness(ind, items, MAX_WEIGHT) for ind in population]
    best_index = fitnesses.index(max(fitnesses))
    best_solution = population[best_index]

    print("\nNejlepší nalezené řešení:")
    total_weight = total_value = item_count = 0
    selected_items = []

    for gene, item in zip(best_solution, items):
        if gene == 1:
            selected_items.append(item)
            total_weight += item.weight
            total_value += item.value
            item_count += 1

    for item in selected_items:
        print(f"- {item.name} (hmotnost: {item.weight} kg, hodnota: {item.value} Kč)")

    print(f"\nCelková hmotnost: {total_weight:.2f} kg")
    print(f"Celková hodnota: {total_value:.2f} Kč")
    print(f"Počet položek v batohu: {item_count}")
    print("\nBinární reprezentace řešení:")
    print(" ".join(map(str, best_solution)))

if __name__ == "__main__":
    run_genetic_algorithm()
