import random
import numpy as np
from visualization import Visualization
from constants import chromosome_length, mutation_rate, colors, graph, max_possible_errors


# The Chromosome class represents one potential solution to the problem
class Chromosome:

    # Build an empty chromosome or a child made by crossover
    def __init__(self, chromosome1=None, chromosome2=None):
        if chromosome1 and chromosome2:
            self.colors = [None] * chromosome_length
            self.crossover(chromosome1, chromosome2)
        else:
            self.colors = random.choices(colors, k=chromosome_length)
        self.fitness_score = self.eval_fitness_score()

    # Mutate a chromosome according to the mutation_rate
    def mutate(self):
        changed = False
        for i in range(chromosome_length):
            if random.random() < mutation_rate:
                changed = True
                self.colors[i] = random.choices(colors)[0]
        if changed:
            self.fitness_score = self.eval_fitness_score()

    # Show the colored map
    def show(self):
        visual_tool = Visualization(600, 450, 20)
        visual_tool.draw_shapes(self.colors)
        visual_tool.draw()

    # Return the fitness score between 0 and 1
    def eval_fitness_score(self):
        errors = 0
        for i, value in enumerate(self.colors):
            for j in graph[i + 1]:
                if value == self.colors[j - 1]:
                    errors += 1
        score = max_possible_errors - (errors / 2)
        return score / max_possible_errors

    # Make a child from two parents
    def crossover(self, chromosome1, chromosome2):
        cut_index = np.random.choice(range(chromosome_length))
        self.colors[:cut_index] = chromosome1.colors[:cut_index]
        self.colors[cut_index:] = chromosome2.colors[cut_index:]
        self.fitness_score = self.eval_fitness_score()

    def found_solution(self):
        return self.fitness_score == 1

    def __str__(self):
        return "<Chromosome: Grade {}% - {}>".format(round(self.fitness_score, 2) * 100, self.colors)

    def __repr__(self):
        return self.__str__()
