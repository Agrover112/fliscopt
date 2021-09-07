import sys
import os
import time
sys.path.append(os.getcwd())
from final.utils.util import plot_scores, print_schedule, read_file
from final.base_algorithm import FlightAlgorithm
from final.rs import RandomSearch
from final.utils.ga_utils import crossover, mutation
from fitness import *
import random
import heapq
from abc import ABCMeta, abstractmethod



class BaseGA(FlightAlgorithm, metaclass=ABCMeta):

    def __init__(self, domain=domain['domain'], fitness_function=fitness_function, seed=random.randint(10, 100), seed_init=True, init=[],max_time=100,
                 population_size=100, step=1, probability_mutation=0.2, probability_crossover=0.2, elitism=0.2,
                 number_generations=500, search=False) -> None:
        super().__init__(domain, fitness_function, seed, seed_init, init,max_time)
        self.population_size = population_size
        self.step = step
        self.probability_mutation = probability_mutation
        self.probability_crossover = probability_crossover
        self.elitism = elitism
        self.number_generations = number_generations
        self.search = search


    def get_base(self) -> str:
        return self.__class__.__base__.__name__

    def get_name(self) -> str:
        pass
    
    @abstractmethod
    def run(self,domain,fitness_function,seed) -> tuple:
        pass




class GA(BaseGA):
    def __init__(self, domain=domain['domain'], fitness_function=fitness_function, seed=random.randint(10, 100), seed_init=True, init=[],max_time=100,
                 population_size=100, step=1, probability_mutation=0.2, elitism=0.2,
                 number_generations=500, search=False) -> None:
        super().__init__(domain, fitness_function, seed, seed_init, init,max_time, population_size, step, probability_mutation,
                         0, elitism, number_generations, search)

    def run(self,domain,fitness_function,seed) -> tuple:
        population = []
        scores = []
        nfe = 0
        for i in range(self.population_size):
            if self.search == True:
                solution, b_c, sc, r_nfe, s = RandomSearch(
                    ).run(self.domain, self.fitness_function, self.seed)
                nfe += r_nfe
            if len(self.init) > 0:
                solution = self.init
            else:
                solution = [self.r_init.randint(self.domain[i][0], self.domain[i][1])
                            for i in range(len(self.domain))]

            population.append(solution)

        number_elitism = int(self.elitism * self.population_size)
        self.start_time=time.time()
        for i in range(self.number_generations):
            if not self.fitness_function.__name__ == 'fitness_function':
                costs = [(self.fitness_function(individual), individual)
                         for individual in population]
            else:
                costs = [(self.fitness_function(individual, 'FCO'), individual)
                         for individual in population]
            nfe += 1
            # costs.sort()
            heapq.heapify(costs)
            ordered_individuals = [individual for (cost, individual) in costs]
            population = ordered_individuals[0:number_elitism]
            if not self.fitness_function.__name__ == 'fitness_function':
                scores.append(self.fitness_function(population[0]))
            else:
                scores.append(self.fitness_function(population[0], 'FCO'))
            # scores.append(fitness_function(population[0], 'FCO'))
            nfe += 1
            while len(population) < self.population_size:
                if random.random() < self.probability_mutation:
                    m = random.randint(0, number_elitism)
                    population.append(
                        mutation(self.domain, self.step, ordered_individuals[m]))
                else:
                    i1 = random.randint(0, number_elitism)
                    i2 = random.randint(0, number_elitism)
                    population.append(
                        crossover(domain, ordered_individuals[i1], ordered_individuals[i2]))

            if time.time()-self.start_time>self.max_time:
                return costs[0][1], costs[0][0], scores, nfe, self.seed

        return costs[0][1], costs[0][0], scores, nfe, self.seed


class ReverseGA(BaseGA):
    def __init__(self, domain=domain['domain'], fitness_function=fitness_function, seed=random.randint(10, 100), seed_init=True, init=[],max_time=100,
                 population_size=100, step=1, probability_crossover=0.2, elitism=0.2,
                 number_generations=500, search=False) -> None:
        super().__init__(domain, fitness_function, seed, seed_init, init,max_time, population_size, step, 0.0,
                         probability_crossover, elitism, number_generations, search)

    def run(self,domain,fitness_function,seed) -> tuple:
        population = []
        scores = []
        nfe = 0
        for i in range(self.population_size):
            if self.search == True:
                solution, b_c, sc, r_nfe, s = RandomSearch(
                    ).run(self.domain, self.fitness_function, self.seed)
                nfe += r_nfe
            if len(self.init) > 0:
                solution = self.init
            else:
                solution = [self.r_init.randint(self.domain[i][0], self.domain[i][1])
                            for i in range(len(self.domain))]

            population.append(solution)

        number_elitism = int(self.elitism * self.population_size)
        self.start_time=time.time()
        for i in range(self.number_generations):
            if not self.fitness_function.__name__ == 'fitness_function':
                costs = [(self.fitness_function(individual), individual)
                         for individual in population]
            else:
                costs = [(self.fitness_function(individual, 'FCO'), individual)
                         for individual in population]
            nfe += 1
            # costs.sort()
            heapq.heapify(costs)
            ordered_individuals = [individual for (cost, individual) in costs]
            population = ordered_individuals[0:number_elitism]
            if not self.fitness_function.__name__ == 'fitness_function':
                scores.append(self.fitness_function(population[0]))
            else:
                scores.append(self.fitness_function(population[0], 'FCO'))
            # scores.append(fitness_function(population[0], 'FCO'))
            nfe += 1
            while len(population) < self.population_size:
                if random.random() < self.probability_crossover:
                    i1 = random.randint(0, number_elitism)
                    i2 = random.randint(0, number_elitism)
                    population.append(
                        crossover(domain, ordered_individuals[i1], ordered_individuals[i2]))
                else:
                    m = random.randint(0, number_elitism)
                    population.append(
                        mutation(self.domain, self.step, ordered_individuals[m]))
        
            if time.time()-self.start_time>self.max_time:
                return costs[0][1], costs[0][0], scores, nfe, self.seed

        return costs[0][1], costs[0][0], scores, nfe, self.seed



class GAReversals(BaseGA):
    def __init__(self, domain=domain['domain'], fitness_function=fitness_function, seed=random.randint(10, 100), seed_init=True, init=[],max_time=100,
                 population_size=100, step=1, probability_mutation=0.2, elitism=0.2,
                 number_generations=500, search=False,n_k=250, step_length=100,) -> None:
        super().__init__(domain, fitness_function, seed, seed_init, init,max_time, population_size, step, probability_mutation,
                         0.0, elitism, number_generations, search)
        self.n_k = n_k
        self.step_length = step_length

    def run(self,domain,fitness_function,seed) -> tuple:
        population = []
        scores = []
        nfe = 0
        rev = 0
        for i in range(self.population_size):
            if self.search == True:
                solution, b_c, sc, r_nfe, s = RandomSearch(
                    ).run(self.domain, self.fitness_function,self.seed)
                nfe += r_nfe
            if len(self.init) > 0:
                solution = self.init
            else:
                solution = [self.r_init.randint(self.domain[i][0], self.domain[i][1])
                            for i in range(len(self.domain))]

            population.append(solution)

        number_elitism = int(self.elitism * self.population_size)
        self.start_time=time.time()
        for i in range(self.number_generations):
            if not self.fitness_function.__name__ == 'fitness_function':
                costs = [(self.fitness_function(individual), individual)
                        for individual in population]
            else:
                costs = [(self.fitness_function(individual, 'FCO'), individual)
                        for individual in population]
            nfe += 1
            if i % self.n_k == 0 and i != 0:
                if self.step_length == 1:
                    costs.sort(reverse=True)
                    rev += 1
                else:
                    rev += 1
                    for _ in range(self.step_length - 1):
                        costs.sort(reverse=True)
                        ordered_individuals = [
                            individual for (cost, individual) in costs]
                        population = ordered_individuals[0:number_elitism]
                        if not self.fitness_function.__name__ == 'fitness_function':
                            scores.append(self.fitness_function(population[0]))
                        else:
                            scores.append(self.fitness_function(population[0], 'FCO'))
                        nfe += 1
                        while len(population) < self.population_size:
                            if random.random() < self.probability_mutation:
                                i1 = random.randint(0, number_elitism)
                                i2 = random.randint(0, number_elitism)
                                population.append(
                                    crossover(self.domain, ordered_individuals[i1], ordered_individuals[i2]))
                            else:
                                m = random.randint(0, number_elitism)
                                population.append(
                                    mutation(self.domain, self.step, ordered_individuals[m]))
                print(rev)  # To print the number of reversals
            else:
                heapq.heapify(costs)
            ordered_individuals = [individual for (cost, individual) in costs]
            population = ordered_individuals[0:number_elitism]
            if not self.fitness_function.__name__ == 'fitness_function':
                scores.append(self.fitness_function(population[0]))
            else:
                scores.append(self.fitness_function(population[0], 'FCO'))
            nfe += 1
            while len(population) < self.population_size:
                if random.random() < self.probability_mutation:
                    i1 = random.randint(0, number_elitism)
                    i2 = random.randint(0, number_elitism)
                    population.append(
                        crossover(self.domain, ordered_individuals[i1], ordered_individuals[i2]))
                else:
                    m = random.randint(0, number_elitism)
                    population.append(
                        mutation(self.domain, self.step, ordered_individuals[m]))
                        
            if time.time()-self.start_time>self.max_time:
                    return costs[0][1], costs[0][0], scores, nfe, self.seed

        return costs[0][1], costs[0][0], scores, nfe, self.seed
            

if __name__ == '__main__':
    read_file('flights.txt')
    sga = ReverseGA(seed_init=False,search=True)

    soln, cost, scores, nfe, seed = sga.run(domain=domain['domain'], fitness_function=fitness_function,
                    seed=5)
    plot_scores(scores, sga.get_base(),fname='flight_scheduling', save_fig=False)
    print_schedule(soln, 'FCO')
