import sys
import os
import time 
sys.path.append(os.getcwd())
from abc import ABCMeta
from .utils.util import plot_scores, print_schedule, read_file
from .base_algorithm import FlightAlgorithm
import heapq
import math

import random
from .fitness import *

class SimulatedAnnealing(FlightAlgorithm,metaclass=ABCMeta):
    def __init__(self, domain=domain['domain'], fitness_function=fitness_function, seed=random.randint(10, 100),
                 seed_init=True,init=[],max_time=1000,temperature=50000.0, cooling=0.95, step=1) -> None:
        super().__init__(domain, fitness_function, seed, seed_init, init,max_time) 
        self.best_solution=0.0
        self.temperature=temperature
        self.cooling=cooling
        self.step=step
        self.temp = []
    
    def get_base(self) -> str:
        pass

    def get_name(self) -> str:
        return self.__class__.__name__

    def run(self,domain,fitness_function,seed) -> tuple:
        self.domain=domain
        self.fitness_function=fitness_function
        self.seed=seed
        count = 0
        nfe = 0
        scores = []
        
        if len(self.init) > 0:
            solution = self.init
        else:
            solution = [self.r_init.randint(self.domain[i][0], self.domain[i][1])
                        for i in range(len(self.domain))]

        self.start_time=time.time()
        while self.temperature > 0.1:
            i = random.randint(0, len(self.domain) - 1)
            direction = random.randint(-self.step, self.step)
            temp_solution = solution[:]
            temp_solution[i] += direction
            if temp_solution[i] < self.domain[i][0]:
                temp_solution[i] = self.domain[i][0]
            elif temp_solution[i] > self.domain[i][1]:
                temp_solution[i] = self.domain[i][1]

            count += 1
            # cost = fitness_function(solution, 'FCO')
            if not self.fitness_function.__name__ == 'fitness_function':
                cost = self.fitness_function(solution)
            else:
                cost = self.fitness_function(solution, 'FCO')
            nfe += 1
            # cost_temp = fitness_function(temp_solution, 'FCO')
            if not self.fitness_function.__name__ == 'fitness_function':
                cost_temp = self.fitness_function(solution)
            else:
                cost_temp = self.fitness_function(solution, 'FCO')
            nfe += 1
            try:
                prob = pow(math.e, (-cost_temp - cost) / self.temperature)
            except OverflowError:
                prob = float('inf')
            best_cost = cost
            if (cost_temp < cost or random.random() < prob):
                best_cost = cost_temp
                solution = temp_solution
            scores.append(best_cost)
            self.temp.append(self.temperature)
            self.temperature = self.temperature * self.cooling

            if time.time()-self.start_time>self.max_time:
                return solution, best_cost, scores, nfe, self.seed

        print('Count: ', count)
        return solution, best_cost, scores, nfe, self.seed



if __name__ == '__main__':
    read_file('flights.txt')
    sa=SimulatedAnnealing(max_time=0.0003,temperature=50000.0,seed_init=False)
    soln, cost, scores, nfe, seed=sa.run(domain=domain['griewank']*5,fitness_function=griewank,seed=5)
    plot_scores(scores,sa.get_name(),fname='griewank',save_fig=False,temp=sa.temp)
    print_schedule(soln,'FCO')