import sys
import os 
sys.path.append(os.getcwd())
import time
from abc import ABCMeta
from .utils.util import plot_scores, print_schedule, read_file
from .base_algorithm import FlightAlgorithm,random

#import random
from .fitness import *

class HillClimb(FlightAlgorithm,metaclass=ABCMeta):
    
    """
    Simple hill Climbing method implemented.[1]
    
    References:
    [1]https://en.wikipedia.org/wiki/Hill_climbing
    Args:
        domain (list): List containing the upper and lower bound.i.e domain of our inputs
        fitness_function (function): This parameter accepts a fitness function of given optimization problem.
        seed (int,optional): Set the seed value of the random seed generator. Defaults to random integer value.
        seed_init(bool,optional): True set's the seed of only population init generator, False sets all generators
        init (list, optional): List for initializing the initial solution. Defaults to [].
        epochs (int, optional): Number of times the algorithm runs. Defaults to 100.
    Returns:
        list: List containing the best_solution,
        int: The final cost after running the algorithm,
        list: List containing all costs during all epochs.
        int: The number of function evaluations(NFE) after running the algorithm
        int: Seed value used by random generators.
    """
    
    def __init__(self, domain=domain['domain'], fitness_function=fitness_function, seed=random.randint(10, 100),
                 seed_init=True, init=[], max_time=1000,epochs=100) -> None:
        super().__init__(domain, fitness_function, seed, seed_init, init)       
        self.epochs = epochs
        self.best_solution=0.0
        
    def get_base(self) -> str:
        pass
  
    def get_name(self) -> str:
        return self.__class__.__name__


    def run(self,domain,fitness_function,seed) -> tuple:
        self.__init__(domain,fitness_function,seed,self.seed_init, self.init,self.max_time)
        count = 0
        scores = []
        nfe = 0
       
        if len(self.init) > 0:
            solution = self.init
        else:
            solution = [self.r_init.randint(self.domain[i][0], self.domain[i][1])
                        for i in range(len(self.domain))]
                        
        self.start_time=time.time()
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

            if time.time()-self.start_time>self.max_time:
                return solution, best_cost, scores, nfe, self.seed

        return solution, best_cost, scores, nfe, self.seed

    
        
if __name__ == '__main__':
    read_file('flights.txt')
    hc=HillClimb(seed_init=False,max_time=0.0000001)
    soln, cost, scores, nfe, seed=hc.run(domain=domain['griewank']*5,fitness_function=griewank,seed=5)
    plot_scores(scores,hc.get_name(),fname='griewank',save_fig=False)
    #print_schedule(soln,'FCO')
