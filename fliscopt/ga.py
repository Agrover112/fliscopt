import sys
import os
import time
sys.path.append(os.getcwd())

from .utils.util import plot_scores, print_schedule, read_file
from .base_algorithm import FlightAlgorithm,random
from .rs import RandomSearch
from .utils.ga_utils import crossover, mutation, circular_mutation
from .fitness import *
import random
import heapq
from abc import ABCMeta, abstractmethod



class BaseGA(FlightAlgorithm, metaclass=ABCMeta):
    
    """ 
    Base Class for Genetic Algorithm variants
    

    
    Attributes:
        domain (list): List containing the upper and lower bound.i.e domain of our inputs
        fitness_function (function): This parameter accepts a fitness function of given optimization problem.
        seed (int,optional): Set the seed value of the random seed generator. Defaults to random integer value.
        seed_init(bool, optional): True set's the seed of only population init generator, False sets all generators
        init (list, optional): List for initializing the initial solution. Defaults to [].
        epochs (int, optional): Number of times the algorithm runs. Defaults to 100.
        
        population_size (int, optional): The size of the population. Defaults to 100.
        number_generations (int,optional): The number of generations which our genetic algorithm produces.Defaults to 500.
        step (int, optional): The step length change in either direction.Defaults to 1.
        probability_mutation: (float, optional): The probability of mutation. Defaults to 0.2.
        probability_crossover: (float, optional): The probability of mutation. Defaults to 0.2
        elitism (float,optional): The top x% of population to retain. Defaults to 0.2
        search (bool, optional): True performs a local search (Random Search) and initializes the initial population of RS as the soln. False doesn't perform any local search.

    Returns:
        list: List containing the best_solution,
        int: The final cost after running the algorithm,
        list: List containing all costs during all epochs.
        int: The number of function evaluations(NFE) after running the algorithm
        int: Seed value used by random generators.
    """

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
      
    """ 
    Simple genetic algorithm is implemented.
    
    References:
    [1]Mitchell, Melanie (1996). An Introduction to Genetic Algorithms. Cambridge, MA: MIT Press. ISBN 9780585030944.
    
    Attributes:
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
    def __init__(self, domain=domain['domain'], fitness_function=fitness_function, seed=random.randint(10, 100), seed_init=True, init=[],max_time=100,
                 population_size=100, step=1, probability_mutation=0.2, elitism=0.2,
                 number_generations=500, search=False) -> None:
    
        super().__init__(domain, fitness_function, seed, seed_init, init,max_time, population_size, step, probability_mutation,
                         0, elitism, number_generations, search)
   
    def run(self,domain,fitness_function,seed) -> tuple:
        #self.__init__(domain, fitness_function, seed, self.seed_init, self.init,self.max_time)
        super().__init__(domain, fitness_function, seed, self.seed_init, self.init,self.max_time, self.population_size, self.step, self.probability_mutation,
                         0, self.elitism,self.number_generations, self.search)
        population = []
        scores = []
        nfe = 0
   
        for i in range(self.population_size):
            if self.search == True:
                solution, b_c, sc, r_nfe, s = RandomSearch(
                    ).run(self.domain, self.fitness_function, self.seed)
                nfe += r_nfe
            else:
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
                        crossover(self.domain, ordered_individuals[i1], ordered_individuals[i2]))

            if time.time()-self.start_time>self.max_time:
                return costs[0][1], costs[0][0], scores, nfe, self.seed

        return costs[0][1], costs[0][0], scores, nfe, self.seed


class ReverseGA(BaseGA):
   
    """ 
    Simple genetic algorithm but with operations performed in reverse order.
    
    References:
    [1]Mitchell, Melanie (1996). An Introduction to Genetic Algorithms. Cambridge, MA: MIT Press. ISBN 9780585030944.
    
    Attributes:
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
    def __init__(self, domain=domain['domain'], fitness_function=fitness_function, seed=random.randint(10, 100), seed_init=True, init=[],max_time=100,
                 population_size=100, step=1, probability_crossover=0.2, elitism=0.2,
                 number_generations=500, search=False) -> None:
        super().__init__(domain, fitness_function, seed, seed_init, init,max_time, population_size, step, 0.0,
                         probability_crossover, elitism, number_generations, search)                  

    def run(self,domain,fitness_function,seed) -> tuple:
        #self.__init__(domain, fitness_function, seed, self.seed_init, self.init,self.max_time)
        super().__init__(domain, fitness_function, seed, self.seed_init, self.init,self.max_time, self.population_size, self.step, 0.0,
                         self.probability_crossover,self. elitism,self.number_generations, self.search)

        population = []
        scores = []
        nfe = 0
    
        for i in range(self.population_size):
            if self.search == True:
                solution, b_c, sc, r_nfe, s = RandomSearch(
                    ).run(self.domain, self.fitness_function, self.seed)
                nfe += r_nfe
            else:
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
                        crossover(self.domain, ordered_individuals[i1], ordered_individuals[i2]))
                else:
                    m = random.randint(0, number_elitism)
                    population.append(
                        mutation(self.domain, self.step, ordered_individuals[m]))
        
            if time.time()-self.start_time>self.max_time:
                return costs[0][1], costs[0][0], scores, nfe, self.seed

        return costs[0][1], costs[0][0], scores, nfe, self.seed


class GAReversals(BaseGA):
     
    """ 
    A genetic algorithm that can perform reverse optimization, to escape local minimma inspired from [1]
    In this algorithm the minimzation process is reversed to a maxmimization process i/n_k times i.e process in reverse direction for step_length no. of times.
    
    References:
    
    [1]https://www.microsoft.com/en-us/research/blog/genetic-algorithm-in-reverse-mode/#:~:text=%20To%20summarize%3A%20%201%20Reversing%20genetic%20algorithm,Duration%20and%20frequency%20of%20reversal%20cycle...%20More%20
    
    Attributes:
        domain (list): List containing the upper and lower bound.i.e domain of our inputs
        fitness_function (function): This parameter accepts a fitness function of given optimization problem.
        seed (int,optional): Set the seed value of the random seed generator. Defaults to random integer value.
        seed_init(bool,optional): True set's the seed of only population init generator, False sets all generators
        init (list, optional): List for initializing the initial solution. Defaults to [].
        epochs (int, optional): Number of times the algorithm runs. Defaults to 100.
        
        n_k (int, optional): The denominator factor i/n_k which determines the number of iterations which are multiples of n_k where reversals take place.Defaults to 250.
        step_length (int, optional): The number of reversals steps/iterations to perform.Defeaults to 100 reversal steps.
    Returns:
        list: List containing the best_solution,
        int: The final cost after running the algorithm,
        list: List containing all costs during all epochs.
        int: The number of function evaluations(NFE) after running the algorithm
        int: Seed value used by random generators.
    """
    def __init__(self, domain=domain['domain'], fitness_function=fitness_function, seed=random.randint(10, 100), seed_init=True, init=[],max_time=100,
                 population_size=100, step=1, probability_mutation=0.2, elitism=0.2,
                 number_generations=500, search=False,n_k=250, step_length=100,) -> None:
        super().__init__(domain, fitness_function, seed, seed_init, init,max_time, population_size, step, probability_mutation,
                         0.0, elitism, number_generations, search)
        self.n_k = n_k
        self.step_length = step_length
    

    def run(self,domain,fitness_function,seed) -> tuple:
        #self.__init__(domain, fitness_function, seed, self.seed_init, self.init,self.max_time)
        super().__init__(domain, fitness_function, seed, self.seed_init, self.init,self.max_time, self.population_size, self.step, self.probability_mutation,
                         0.0, self.elitism, self.number_generations, self.search)
        population = []
        scores = []
        nfe = 0
        rev = 0
    
        for i in range(self.population_size):
            if self.search == True:
                solution, b_c, sc, r_nfe, s = RandomSearch(
                    ).run(self.domain, self.fitness_function,self.seed)
                nfe += r_nfe
            else:
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
        
class GARSReversals(BaseGA):
     
    """ 
    A genetic algorithm that can perform reverse optimization, to escape local minimma inspired from [1]
    In this algorithm the minimzation process is reversed to a maxmimization process i/n_k times i.e process in reverse direction for step_length no. of times.
    Unlike GAReversals we perform a RandomSearch in reverse direction to escape local minimas.
    
    References:
    
    [1]https://www.microsoft.com/en-us/research/blog/genetic-algorithm-in-reverse-mode/#:~:text=%20To%20summarize%3A%20%201%20Reversing%20genetic%20algorithm,Duration%20and%20frequency%20of%20reversal%20cycle...%20More%20
    
    Attributes:
        domain (list): List containing the upper and lower bound.i.e domain of our inputs
        fitness_function (function): This parameter accepts a fitness function of given optimization problem.
        seed (int,optional): Set the seed value of the random seed generator. Defaults to random integer value.
        seed_init(bool,optional): True set's the seed of only population init generator, False sets all generators
        init (list, optional): List for initializing the initial solution. Defaults to [].
        epochs (int, optional): Number of times the algorithm runs. Defaults to 100.
        
        n_k (int, optional): The denominator factor i/n_k which determines the number of iterations which are multiples of n_k where reversals take place.Defaults to 250.
        step_length (int, optional): The number of reversals steps/iterations to perform.Defeaults to 100 reversal steps.
    Returns:
        list: List containing the best_solution,
        int: The final cost after running the algorithm,
        list: List containing all costs during all epochs.
        int: The number of function evaluations(NFE) after running the algorithm
        int: Seed value used by random generators.
    """
    def __init__(self, domain=domain['domain'], fitness_function=fitness_function, seed=random.randint(10, 100), seed_init=True, init=[],max_time=100,
                 population_size=100, step=1, probability_mutation=0.2, elitism=0.2,
                 number_generations=500, search=False,n_k=250, step_length=100,) -> None:
        super().__init__(domain, fitness_function, seed, seed_init, init,max_time, population_size, step, probability_mutation,
                         0.0, elitism, number_generations, search)
        self.n_k = n_k
        self.step_length = step_length
    

    def run(self,domain,fitness_function,seed) -> tuple:
        #self.__init__(domain, fitness_function, seed, self.seed_init, self.init,self.max_time)
        super().__init__(domain, fitness_function, seed, self.seed_init, self.init,self.max_time, self.population_size, self.step, self.probability_mutation,
                         0.0, self.elitism, self.number_generations, self.search)
        population = []
        scores = []
        nfe = 0
        rev = 0
    
        for i in range(self.population_size):
            if self.search == True:
                solution, b_c, sc, r_nfe, s = RandomSearch(
                    ).run(self.domain, self.fitness_function,self.seed)
                nfe += r_nfe
            else:
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
                    best_cost = sys.maxsize
                    best_solution=[]
                    rev += 1
                    for _ in range(self.step_length - 1):
                        costs.sort(reverse=True)
                        solution = [self.r_init.randint(self.domain[i][0], self.domain[i][1])
                                        for i in range(len(self.domain))]

                        if not self.fitness_function.__name__ == 'fitness_function':
                            cost = self.fitness_function(solution)
                            #scores.append(cost)
                        else:
                            cost = self.fitness_function(solution, 'FCO')
                            #scores.append(cost)
                        
                        nfe += 1
                        if cost > self.best_cost:
                            best_cost = cost
                            best_solution = solution
                            
                        scores.append(best_cost)
                        population.append(best_solution)

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
    