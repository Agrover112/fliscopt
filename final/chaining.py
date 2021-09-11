import sys
import os
from typing import final 
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
        scores = []
        NFE = 0
        for i in range(self.rounds):
            if i == 0:
                soln, cost, scores, nfe, seed = self.choose(algorithm_1).run(self.domain, self.fitness_function, self.seed)
                soln = mutation(self.domain, random.randint(0, 1), soln)  # Either 1 step or no step InitMutation
                scores.append(cost)
                NFE += nfe
                rich.print("Cost at {}=={}".format(i, cost))
            elif i == self.rounds - 1:
                final_soln, cost, scores, nfe, seed = self.choose(algorithm_2).run(self.domain, self.fitness_function, self.seed)
                scores.append(cost)
                NFE += nfe
                rich.print("Cost at {}=={}".format(i, cost))
                return final_soln, scores[-1], scores, NFE
            else:
                soln, cost, scores, nfe, seed = self.choose(algorithm_1).run(self.domain, self.fitness_function, self.seed)
                rich.print("Cost at {}=={}".format(i, cost))
                soln = mutation(self.domain, random.randint(0, 1), soln)
                scores.append(cost)
                NFE += nfe

            final_soln, cost, scores, nfe, seed = self.choose(algorithm_2).run(self.domain, self.fitness_function, self.seed)
            scores.append(cost)
            NFE += nfe
            if self.rounds ==1:
                return soln, scores[-1], scores, NFE
            if cost - random.randint(self.tol, 100) > int(sum(scores[-self.n_obs:]) / self.n_obs):
                rich.print("----Ending early at iteration{}----".format(i))
                rich.print("Cost{}".format(cost))
                if fitness_function.__name__ == 'fitness_function':
                    print_schedule(final_soln, 'FCO')
                return final_soln, scores[-1], scores, NFE
            rich.print("Cost at {}=={}".format(i, cost))
            init = mutation(self.domain, 1, final_soln)  # IntMutation


if __name__ == '__main__':
    read_file('flights.txt')
    ic=IteratedChaining(rounds=10, n_obs=2, tol=90)
    soln, cost, scores, nfe=ic.run('RandomSearch', 'HillClimb')
    print_schedule(soln, 'FCO')
    #plot_scores(scores, "Chaining",save_fig=False)