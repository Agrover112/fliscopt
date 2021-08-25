import sys
import os 
sys.path.append(os.getcwd())
from abc import ABCMeta
from utils.utils import plot_scores, print_schedule, read_file
from flight_algorithms.algorithms.base_algorithm import FlightAlgorithm
import heapq
import math
import random
import sys
from fitness import *


class RandomSearch(FlightAlgorithm, metaclass=ABCMeta):
    def __init__(self, domain, fitness_function, seed=random.randint(10, 100),
                 seed_init=True, init=[], epochs=100):
        super().__init__(domain, fitness_function, seed, seed_init, init)         
        self.epochs = epochs
        self.best_cost=sys.maxsize
        self.best_solution=0.0


    def run(self, **kwargs) -> tuple:
        scores = []
        nfe = 0
        if len(self.init) > 0:
            solution = self.init
        else:
            solution = [self.r_init.randint(self.domain[i][0], self.domain[i][1])
                        for i in range(len(self.domain))]
        for i in range(self.epochs):
            if i != 0:
                solution = [random.randint(self.domain[i][0], self.domain[i][1])
                            for i in range(len(self.domain))]
            if not self.fitness_function.__name__ == 'fitness_function':
                cost = self.fitness_function(solution)
            else:
                cost = self.fitness_function(solution, 'FCO')
            nfe += 1
            if cost < self.best_cost:
                self.best_cost = cost
                self.best_solution = solution
            scores.append(self.best_cost)
        return self.best_solution, self.best_cost, scores, nfe, self.seed
        


if __name__ == '__main__':
    read_file('flights.txt')
    rs=RandomSearch(domain=domain['domain'],fitness_function=fitness_function,seed=5,seed_init=False)
    soln, cost, scores, nfe, seed=rs.run()
    plot_scores(scores,rs.__class__.__name__,save_fig=False)
    print_schedule(soln,'FCO')
    """"
    1. Change all algorithms
    2. Docstrings 
    3. Type hinting
    4. Unit tests
    5. Change all single_runs
    6. Change all multiple runs
    
    """