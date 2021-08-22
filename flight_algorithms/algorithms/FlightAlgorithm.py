from abc import ABC, abstractmethod

import random


class FlightAlgorithm(ABC):
    def __init__(self, set_all_generators=False):
        self.best_solution = None
        self.best_cost = None
        self.scores = None
        self.nfe = None

        self.seed = None
        self.r_init = None

        self.init_seed(set_all_generators)

    def init_seed(self, set_all_generators):
        self.seed = random.randint(10, 100)
        self.r_init = random.Random(self.seed)

        if set_all_generators:
            random.seed(self.seed)

    @abstractmethod
    def run(self, **kwargs) -> tuple:
        pass
