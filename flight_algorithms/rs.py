import sys
import os 
sys.path.append(os.getcwd())
import time
from abc import ABCMeta
from utils.utils import plot_scores, print_schedule, read_file
from flight_algorithms.base_algorithm import FlightAlgorithm
import random
import sys
from fitness import *


class RandomSearch(FlightAlgorithm, metaclass=ABCMeta):
    def __init__(self, domain=domain['domain'], fitness_function=fitness_function, seed=random.randint(10, 100),
                 seed_init=True, init=[],max_time=1000,epochs=100) -> None:
        super().__init__(domain, fitness_function, seed, seed_init, init,max_time)        
        self.epochs = epochs
        self.best_cost=sys.maxsize
        self.best_solution=0.0
        
    def get_base(self) -> str:
        pass
    
    def get_name(self) -> str:
        return self.__class__.__name__

 
        
    def run(self,domain,fitness_function,seed):
            scores = []
            nfe = 0
            if len(self.init) > 0:
                solution = self.init
            else:
                solution = [self.r_init.randint(self.domain[i][0], self.domain[i][1])
                            for i in range(len(self.domain))]

            self.start_time=time.time()
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
                if time.time()-self.start_time>self.max_time:
                    return self.best_solution, self.best_cost, scores, nfe, self.seed
            return self.best_solution, self.best_cost, scores, nfe, self.seed

if __name__ == '__main__':
    read_file('flights.txt')
    rs=RandomSearch(max_time=0.00001)  #def run():
    soln, cost, scores, nfe, seed=rs.run(domain=domain['domain'],fitness_function=fitness_function,seed=5)
    #plot_scores(scores,rs.get_name(),fname='flight_scheduling',save_fig=False)
    #print_schedule(soln,'FCO')
    """"
    2. Docstrings 
    4. Unit tests
    """