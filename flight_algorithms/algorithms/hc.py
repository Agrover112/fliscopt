import sys
import os 
sys.path.append(os.getcwd())
#sys.path.append("/mnt/d/MINOR PROJECT/final/")
from abc import ABCMeta
from utils.utils import plot_scores, print_schedule, read_file
from flight_algorithms.algorithms.base_algorithm import FlightAlgorithm
import heapq
import math
import random
import sys
from fitness import *

class HillClimb(FlightAlgorithm,metaclass=ABCMeta):
    def __init__(self, domain, fitness_function, seed=random.randint(10, 100),
                 seed_init=True, init=[], epochs=100) -> None:
        super().__init__(domain, fitness_function, seed, seed_init, init)        
        self.epochs = epochs
        self.best_solution=0.0

    def run(self,*args,**kwargs) -> tuple:
        count = 0
        scores = []
        nfe = 0
        if len(self.init) > 0:
            solution = self.init
        else:
            solution = [self.r_init.randint(self.domain[i][0], self.domain[i][1])
                        for i in range(len(self.domain))]
        while True:
            neighbors = []
            for i in range(len(self.domain)):
                if solution[i] > self.domain[i][0]:
                    if solution[i] != self.domain[i][1]:  # cannot change value of 9 to 10
                        neighbors.append(
                            solution[0:i] + [solution[i] + 1] + solution[i + 1:])
                if solution[i] < self.domain[i][1]:
                    if solution[i] != self.domain[i][0]:
                        neighbors.append(
                            solution[0:i] + [solution[i] - 1] + solution[i + 1:])

            # actual = fitness_function(solution, 'FCO')
            if not self.fitness_function.__name__ == 'fitness_function':
                actual = self.fitness_function(solution)
            else:
                actual = self.fitness_function(solution, 'FCO')
            nfe += 1
            best_cost = actual
            for i in range(len(neighbors)):
                count += 1
                # cost = fitness_function(neighbors[i], 'FCO')
                if not self.fitness_function.__name__ == 'fitness_function':
                    cost = self.fitness_function(neighbors[i])
                else:
                    cost = self.fitness_function(neighbors[i], 'FCO')
                nfe += 1
                if cost < best_cost:
                    best_cost = cost
                    solution = neighbors[i]
                scores.append(best_cost)

            if best_cost == actual:
                print('Count: ', count)
                # print('NFE: ',nfe)
                break
        return solution, best_cost, scores, nfe, self.seed
        
if __name__ == '__main__':
    read_file('flights.txt')
    rs=HillClimb(domain=domain['griewank']*5,fitness_function=griewank,seed=5,seed_init=False)
    soln, cost, scores, nfe, seed=rs.run()
    plot_scores(scores,rs.__class__.__name__,save_fig=False)
    #print_schedule(soln,'FCO')