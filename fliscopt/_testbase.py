from abc import ABC, ABCMeta, abstractmethod
import random
import math


class FlightAlgorithm(metaclass=ABCMeta):
    def __init__(self, domain, fitness_function, seed=random.randint(10, 100),
                 set_all_generators=False, init=[]):
        self.domain = domain
        self.fitness_function = fitness_function
        self.seed = seed
        self.init = init
        self.init_seed(set_all_generators)

        self.start_time = 0.0  # Loop starting time

    def init_seed(self, set_all_generators=False):
        self.r_init = random.Random(self.seed)

        if set_all_generators:
            random.seed(self.seed)

    @abstractmethod
    def get_base(self) -> str:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def run(self, **kwargs) -> tuple:
        pass
