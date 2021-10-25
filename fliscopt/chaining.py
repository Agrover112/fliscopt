import sys
import os
#from typing import final 
sys.path.append(os.getcwd())
import time 

from .utils.util import  plot_scores, print_schedule, read_file
from .utils.ga_utils import mutation
from .base_algorithm import FlightAlgorithm
from .rs import RandomSearch
from .hc import HillClimb
from .sa import SimulatedAnnealing
from .ga import GA, ReverseGA, GAReversals

import random
from .fitness import *

import rich

class IteratedChaining():
    """
        Iterated Chaining method which is a modification of Chaining [1] used by Facebook's Nevergrad. In this method 2 optimizers can be selected and passed which in turn functions 
        like :
        OptAlgo-1---mutation--->OptAlgo2---->repeat n no. of rounds until Early Stopping Criteria is reached
        We use an Early Stopping like mechanism to prevent running our algorithm if divergence occurs.
        
        Early Stopping algorithm summary:
        The algorithm uses tol (tolerance) and n_obs(number of observations) as parameters. We try to limit the divergence by averaging of the number of observations,
        and then comparing if our 
        current_cost value = current_cost- random-value_btwn_(tol,100) > avg of n obs. 
        We added tolerance to provide some leeway, rather than
        abruptly terminating. Higher tolerance equates to our above condtion being true LESS LIKELY, and vice versa.
        
        NOTE:Unlike Fb's implementation of Chaining, which uses
        budget allocation, we use Early Stopping criteria combined with mutations which influence local minima.
        In Fb's implementation the chaining stops after solns have passed to the last optimizer, however we chose to repeat the process(iteration).
        Also our implementation is limited to using 2 Optimizers and each algorithm can run for the number of default iterations specified , although 
        this can easily be changed by tweaking it in the code.
        
        
        
        
        [1]https://facebookresearch.github.io/nevergrad/optimizers_ref.html?highlight=chaining#nevergrad.families.Chaining
    
    Attributes:
        domain (list): List containing the upper and lower bound.i.e domain of our inputs
        fitness_function (function): This parameter accepts a fitness function of given optimization problem.
        rounds (int, optional): Number of times the iteration takes place. Defaults to 10.
        n_obs (int, optional): The number of rounds upto which Early Stopping tolerates the cost divergence and calculates the average.Defaults to 2.
        tol: (int, optional): The tolerance factor which determines how much divergence the Early Stopping algo tolerates.Defaults to 90.
        seed (int,optional): Set the seed value of the random seed generator. Defaults to random integer value.

    Returns:
        list: List containing the best_solution,
        int: The final cost after running the algorithm,
        list: List containing all costs during all epochs.
        int: The number of function evaluations(NFE) after running the algorithm
        int: Seed value used by random generators.
    Raises:
        ValueError: If algorithm not present in given package is passed as an argument.
    """



    def __init__(self, domain=domain['domain'], fitness_function=fitness_function, rounds=10,seed=random.randint(10, 100), n_obs=2, tol=90):
        self.domain = domain
        self.fitness_function = fitness_function
        self.seed=seed
        self.rounds = rounds
        self.n_obs = n_obs
        self.tol = tol
    
    def choose(self,algorithm):
        if algorithm == 'RandomSearch':
            return RandomSearch() 
        elif algorithm == 'HillClimb':
            return HillClimb()

        elif algorithm == 'SimulatedAnnealing':
            return SimulatedAnnealing()\

        elif algorithm == 'GA':
            return GA()

        elif algorithm == 'ReverseGA':
            return ReverseGA()

        elif algorithm == 'GAReversals':
            return GAReversals()

        else:
            raise ValueError("Algorithm not found")
   

    def run(self,algorithm_1, algorithm_2):
        # Note scores here is the best cost of each particular single_run
        SCORES = []
        NFE = 0

        for i in range(self.rounds):
            if i == 0:
                soln, cost, scores, nfe, seed = self.choose(algorithm_1).run(self.domain, self.fitness_function, self.seed)
                soln = mutation(self.domain, random.randint(0, 1), soln)  # Either 1 step or no step InitMutation
                SCORES.append(cost)
                NFE += nfe
                rich.print("Cost at {}=={}".format(i, cost))
            elif i == self.rounds - 1:
                final_soln, cost, scores, nfe, seed = self.choose(algorithm_2).run(self.domain, self.fitness_function, self.seed)
                SCORES.append(cost)
                NFE += nfe
                rich.print("Cost at {}=={}".format(i, cost))
                return final_soln, SCORES[-1], SCORES, NFE
            else:
                soln, cost, scores, nfe, seed = self.choose(algorithm_1).run(self.domain, self.fitness_function, self.seed)
                rich.print("Cost at {}=={}".format(i, cost))
                soln = mutation(self.domain, random.randint(0, 1), soln)
                SCORES.append(cost)
                NFE += nfe

            final_soln, cost, scores, nfe, seed = self.choose(algorithm_2).run(self.domain, self.fitness_function, self.seed)
            SCORES.append(cost)
            NFE += nfe
            if self.rounds ==1:
                return soln, SCORES[-1], SCORES, NFE
            if cost - random.randint(self.tol, 100) > int(sum(scores[-self.n_obs:]) / self.n_obs):
                rich.print("----Ending early at iteration{}----".format(i))
                rich.print("Cost{}".format(cost))
                if fitness_function.__name__ == 'fitness_function':
                    print_schedule(final_soln, 'FCO')
                return final_soln, SCORES[-1], SCORES, NFE
            rich.print("Cost at {}=={}".format(i, cost))
            init = mutation(self.domain, 1, final_soln)  # IntMutation


if __name__ == '__main__':
    read_file('flights.txt')
    ic=IteratedChaining(rounds=10, n_obs=2, tol=90)
    soln, cost, scores, nfe=ic.run('RandomSearch', 'HillClimb')
    print_schedule(soln, 'FCO')
    #plot_scores(scores, "Chaining",save_fig=False)
