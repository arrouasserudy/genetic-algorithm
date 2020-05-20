import os
import statistics
import numpy as np
import matplotlib.pyplot as plt
from chromosome import Chromosome
from constants import population_number, elitism


# The Generation class represents a population made of Chromosomes
class Generation:
    counter = 0
    fittest_over_time = []
    average_over_time = []

    # Build a generation according to a given population
    def __init__(self, population=None):
        if population:
            self.population = population
        else:
            self.population = [Chromosome() for _ in range(population_number)]
        self.fitness_scores = [chromosome.fitness_score for chromosome in self.population]
        self.weights = self.get_weights()
        self.fittest_score = max(self.fitness_scores)
        self.average_score = statistics.mean(self.fitness_scores)
        Generation.counter += 1
        Generation.fittest_over_time.append(self.fittest_score)
        Generation.average_over_time.append(self.average_score)

    # Get the n fittest chromosomes
    def get_n_fittest(self, n=1):
        zipped = list(zip(self.population, self.fitness_scores))
        sorted_zip = sorted(zipped, key=lambda chromosome: chromosome[1], reverse=True)
        sorted_population = [list(t) for t in zip(*sorted_zip)]
        return sorted_population[0][:n]

    # Get the fittest chromosome
    def get_fittest(self):
        return self.get_n_fittest()[0]

    # Get the next generation
    def get_next_generation(self):
        elite_number = round(population_number * elitism)
        new_generation = self.get_n_fittest(elite_number)

        for i in range(population_number - elite_number):
            child = self.crossover()
            child.mutate()
            new_generation.append(child)
        return Generation(new_generation)

    # Made a crossover with biased selection according to the chromosome's weights
    def crossover(self):
        a, b = np.random.choice(range(population_number), size=2, p=self.weights)
        child = Chromosome(self.population[a], self.population[b])
        return child

    # Get the chromosome's weights
    def get_weights(self):
        denominator = sum(self.fitness_scores)
        weights = [score / denominator for score in self.fitness_scores]
        return weights

    def found_solution(self):
        return self.get_fittest().found_solution()

    # Show the result graph
    @classmethod
    def show_result_graph(cls):
        plt.plot([i for i in range(cls.counter)], cls.fittest_over_time, label="Fittest")
        plt.scatter([i for i in range(cls.counter)], cls.fittest_over_time)
        plt.plot([i for i in range(cls.counter)], cls.average_over_time, label="Average")
        plt.scatter([i for i in range(cls.counter)], cls.average_over_time)

        plt.legend()
        plt.xlabel("generation #")
        plt.ylabel("Fitness Score")
        plt.title("Fitness scores by generation")

        plt.savefig(os.path.join(os.path.dirname(__file__), "answer.png"))
        plt.show()
