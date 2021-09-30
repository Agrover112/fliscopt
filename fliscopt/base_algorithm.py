from abc import ABC, ABCMeta, abstractmethod
import random
import math
import sys

class FlightAlgorithm(metaclass=ABCMeta):
    def __init__(self, domain, fitness_function,seed=random.randint(10, 100),seed_init=True,init=None,max_time=1000)-> None:
        self.domain = domain
        self.fitness_function = fitness_function
        self.seed = seed
        self.seed_init = seed_init
        if init is None:
            self.init = []
        else:
            self.init = init
        self.max_time=1000
        if self.seed_init:
            # Set the seed for initial population only
            self.r_init = random.Random(self.seed)
        else:
            # Same seeds for both init and other random generators
            self.r_init = random.Random(self.seed)
            random.seed(self.seed)
        
        self.best_cost =0.0  # returned
    @abstractmethod
    def get_base(self) -> str:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def run(self,domain,fitness_function,seed) -> tuple:
        pass