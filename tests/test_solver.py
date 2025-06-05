import unittest
import random
from solver import Item, fitness, crossover, mutate

class TestFitness(unittest.TestCase):
    def test_fitness_under_weight(self):
        items = [Item("A", 1.0, 10), Item("B", 2.0, 20)]
        individual = [1, 0]
        # value 10 + bonus for 1 item
        self.assertEqual(fitness(individual, items, 5.0), 20)

    def test_fitness_over_weight(self):
        items = [Item("A", 2.0, 10), Item("B", 4.0, 20)]
        individual = [1, 1]
        # total weight 6 > 5 -> fitness 0
        self.assertEqual(fitness(individual, items, 5.0), 0)

class TestCrossover(unittest.TestCase):
    def test_crossover_reproducible(self):
        random.seed(0)
        parent1 = [1, 1, 1, 1]
        parent2 = [0, 0, 0, 0]
        child = crossover(parent1, parent2)
        self.assertEqual(child, [1, 1, 0, 0])

class TestMutate(unittest.TestCase):
    def test_mutate_reproducible(self):
        random.seed(0)
        individual = [0, 0, 0, 0]
        mutated = mutate(individual, 0.5)
        self.assertEqual(mutated, [0, 0, 1, 1])

if __name__ == "__main__":
    unittest.main()
