import heapq
import math
import random
import sys

from utils.ga_utils import crossover, mutation ,multi_mutation
from utils.utils import plot_scores, print_schedule



def random_search(domain, fitness_function, seed=random.randint(10, 100), seed_init=True, init=[], epochs=100):
    """ Random search algorithm implemented

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
    if seed_init:
        # Set the seed for initial population only
        r_init = random.Random(seed)
    else:
        # Same seeds for both init and other random generators
        r_init = random.Random(seed)
        random.seed(seed)

    best_cost = sys.maxsize
    scores = []
    nfe = 0
    if len(init) > 0:
        solution = init
    else:
        solution = [r_init.randint(domain[i][0], domain[i][1])
                    for i in range(len(domain))]
    for i in range(epochs):
        if i != 0:
            solution = [random.randint(domain[i][0], domain[i][1])
                        for i in range(len(domain))]
        if not fitness_function.__name__ == 'fitness_function':
            cost = fitness_function(solution)
        else:
            cost = fitness_function(solution, 'FCO')
        nfe += 1
        if cost < best_cost:
            best_cost = cost
            best_solution = solution
        scores.append(best_cost)
    return best_solution, best_cost, scores, nfe, seed


def hill_climb(domain, fitness_function, seed=random.randint(10, 100), seed_init=True, init=[], epochs=100):
    """ Simple Hill Climbing algorithm implemented

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
    if seed_init:
        # Set the seed for initial population only
        r_init = random.Random(seed)
    else:
        # Same seeds for both init and other random generators
        r_init = random.Random(seed)
        random.seed(seed)
    count = 0
    scores = []
    nfe = 0
    if len(init) > 0:
        solution = init
    else:
        solution = [r_init.randint(domain[i][0], domain[i][1])
                    for i in range(len(domain))]
    while True:
        neighbors = []
        for i in range(len(domain)):
            if solution[i] > domain[i][0]:
                if solution[i] != domain[i][1]:  # cannot change value of 9 to 10
                    neighbors.append(
                        solution[0:i]+[solution[i]+1]+solution[i+1:])
            if solution[i] < domain[i][1]:
                if solution[i] != domain[i][0]:
                    neighbors.append(
                        solution[0:i] + [solution[i] - 1] + solution[i + 1:])

        #actual = fitness_function(solution, 'FCO')
        if not fitness_function.__name__ == 'fitness_function':
            actual = fitness_function(solution)
        else:
            actual = fitness_function(solution, 'FCO')
        nfe += 1
        best = actual
        for i in range(len(neighbors)):
            count += 1
            #cost = fitness_function(neighbors[i], 'FCO')
            if not fitness_function.__name__ == 'fitness_function':
                cost = fitness_function(neighbors[i])
            else:
                cost = fitness_function(neighbors[i], 'FCO')
            nfe += 1
            if cost < best:
                best = cost
                solution = neighbors[i]
            scores.append(best)

        if best == actual:
            print('Count: ', count)
            #print('NFE: ',nfe)
            break
    return solution, best, scores, nfe, seed


def simulated_annealing(domain, fitness_function, seed=random.randint(10, 100), seed_init=True, init=[], temperature=50000.0, cooling=0.95, step=1):
    """ Simulated annealing algorithm implemented with temeperature and cooling parameters.


    Args:
        domain (list): List containing the upper and lower bound.i.e domain of our inputs
        fitness_function (function): This parameter accepts a fitness function of given optimization problem.
        init (list, optional): List for initializing the initial solution. Defaults to [].
        seed (int,optional): Set the seed value of the random seed generator. Defaults to random integer value.
        seed_init(bool,optional): True set's the seed of only population init generator, False sets all generators
        epochs (int, optional): Number of times the algorithm runs. Defaults to 100.
        temperature (float, optional): This parameter controls the degree of randomness.Increasing it increases the search space. Defaults to 50000.0.
        cooling (float, optional): The margin by which temperature decreases at each epoch. Defaults to 0.95.
        step (int, optional): Number of steps to the right or left to make changes in given solution. Defaults to 1.

    Returns:
        list: List containing the best_solution,
        int: The final cost after running the algorithm,
        list: List containing all costs during all epochs.
        int: The number of function evaluations(NFE) after running the algorithm
        int: Seed value used by random generators.
    """
    if seed_init:
        # Set the seed for initial population only
        r_init = random.Random(seed)
    else:
        # Same seeds for both init and other random generators
        r_init = random.Random(seed)
        random.seed(seed)
    count = 0
    nfe = 0
    scores = []
    simulated_annealing.temp = []

    if len(init) > 0:
        solution = init
    else:
        solution = [r_init.randint(domain[i][0], domain[i][1])
                    for i in range(len(domain))]

    while temperature > 0.1:
        i = random.randint(0, len(domain) - 1)
        direction = random.randint(-step, step)
        temp_solution = solution[:]
        temp_solution[i] += direction
        if temp_solution[i] < domain[i][0]:
            temp_solution[i] = domain[i][0]
        elif temp_solution[i] > domain[i][1]:
            temp_solution[i] = domain[i][1]

        count += 1
        #cost = fitness_function(solution, 'FCO')
        if not fitness_function.__name__ == 'fitness_function':
            cost = fitness_function(solution)
        else:
            cost = fitness_function(solution, 'FCO')
        nfe += 1
        #cost_temp = fitness_function(temp_solution, 'FCO')
        if not fitness_function.__name__ == 'fitness_function':
            cost_temp = fitness_function(solution)
        else:
            cost_temp = fitness_function(solution, 'FCO')
        nfe += 1
        try:
            prob = pow(math.e, (-cost_temp - cost) / temperature)
        except OverflowError:
            prob = float('inf')
        best = cost
        if (cost_temp < cost or random.random() < prob):
            best = cost_temp
            solution = temp_solution
        scores.append(best)
        simulated_annealing.temp.append(temperature)
        temperature = temperature * cooling

    print('Count: ', count)
    return solution, best, scores, nfe, seed


def genetic_algorithm(domain, fitness_function, seed=random.randint(10, 100), seed_init=True, init=[], population_size=100, step=1,
                      probability_mutation=0.2, elitism=0.2,
                      number_generations=500, search=False):
    """ Genetic algorithm implemented with elitisim.


    Args:
        domain (list): List containing the upper and lower bound.i.e domain of our inputs
        fitness_function (function): This parameter accepts a fitness function of given optimization problem.
        init (list, optional): List for initializing the initial solution. Defaults to [].
        seed (int,optional): Set the seed value of the random seed generator. Defaults to random integer value.
        seed_init(bool,optional): True set's the seed of only population init generator, False sets all generators
        population_size (int, optional): The maximum size of the population to generate. Defaults to 100.
        probability_mutation (float, optional): Controls the rate of mutation of genes. Defaults to 0.2.
        elitism (float, optional): The percentage of population which proceeds onto next iter without changes. Defaults to 0.2.
        number_generations (int, optional): Analgous to epochs, but in this context refers to number of generations the algorithm evolves to . Defaults to 500.
        search (bool, optional): If True  solution is initialized as the result of a RandomSearch . Defaults to False.
        step (int, optional): Number of steps to the right or left to make changes in given solution. Defaults to 1.

    Returns:
        list: List containing the best_solution,
        int: The final cost after running the algorithm,
        list: List containing all costs during all epochs.
        int: The number of function evaluations(NFE) after running the algorithm
        int: Seed value used by random generators.
    """
    if seed_init:
        # Set the seed for initial population only
        r_init = random.Random(seed)
    else:
        # Same seeds for both init and other random generators
        r_init = random.Random(seed)
        random.seed(seed)
    population = []
    scores = []
    nfe = 0
    for i in range(population_size):
        if search == True:
            solution, b_c, sc, r_nfe, s = random_search(
                domain, fitness_function, seed)
            nfe += r_nfe
        if len(init) > 0:
            solution = init
        else:
            solution = [r_init.randint(domain[i][0], domain[i][1])
                        for i in range(len(domain))]

        population.append(solution)

    number_elitism = int(elitism * population_size)

    for i in range(number_generations):
        if not fitness_function.__name__ == 'fitness_function':
            costs = [(fitness_function(individual), individual)
                     for individual in population]
        else:
            costs = [(fitness_function(individual, 'FCO'), individual)
                     for individual in population]
        # costs = [(fitness_function(individual, 'FCO'), individual)
        #         for individual in population]
        nfe += 1
        # costs.sort()
        heapq.heapify(costs)
        ordered_individuals = [individual for (cost, individual) in costs]
        population = ordered_individuals[0:number_elitism]
        if not fitness_function.__name__ == 'fitness_function':
            scores.append(fitness_function(population[0]))
        else:
            scores.append(fitness_function(population[0], 'FCO'))
        #scores.append(fitness_function(population[0], 'FCO'))
        nfe += 1
        while len(population) < population_size:
            if random.random() < probability_mutation:
                m = random.randint(0, number_elitism)
                population.append(
                    mutation(domain, step, ordered_individuals[m]))
            else:
                i1 = random.randint(0, number_elitism)
                i2 = random.randint(0, number_elitism)
                population.append(
                    crossover(domain, ordered_individuals[i1], ordered_individuals[i2]))
    return costs[0][1], costs[0][0], scores, nfe, seed


def genetic_algorithm_reversed(domain, fitness_function, seed=random.randint(10, 100), seed_init=True, init=[], population_size=100, step=1,
                               probability_mutation=0.2, elitism=0.2,
                               number_generations=500, search=False):
    """ Genetic algorithm implemented with elitisim.


    Args:
        domain (list): List containing the upper and lower bound.i.e domain of our inputs
        fitness_function (function): This parameter accepts a fitness function of given optimization problem.
        init (list, optional): List for initializing the initial solution. Defaults to [].
        seed (int,optional): Set the seed value of the random seed generator. Defaults to random integer value.
        seed_init(bool,optional): True set's the seed of only population init generator, False sets all generators
        population_size (int, optional): The maximum size of the population to generate. Defaults to 100.
        probability_mutation (float, optional): Controls the rate of mutation of genes. Defaults to 0.2.
        elitism (float, optional): The percentage of population which proceeds onto next iter without changes. Defaults to 0.2.
        number_generations (int, optional): Analgous to epochs, but in this context refers to number of generations the algorithm evolves to . Defaults to 500.
        search (bool, optional): If True  solution is initialized as the result of a RandomSearch . Defaults to False.
        step (int, optional): Number of steps to the right or left to make changes in given solution. Defaults to 1.

    Returns:
        list: List containing the best_solution,
        int: The final cost after running the algorithm,
        list: List containing all costs during all epochs.
        int: The number of function evaluations(NFE) after running the algorithm
        int: Seed value used by random generators.
    """
    if seed_init:
        # Set the seed for initial population only
        r_init = random.Random(seed)
    else:
        # Same seeds for both init and other random generators
        r_init = random.Random(seed)
        random.seed(seed)
    population = []
    scores = []
    nfe = 0
    for i in range(population_size):
        if search == True:
            solution, b_c, sc, r_nfe, s = random_search(
                domain, fitness_function, seed)
            nfe += r_nfe
        if len(init) > 0:
            solution = init
        else:
            solution = [r_init.randint(domain[i][0], domain[i][1])
                        for i in range(len(domain))]

        population.append(solution)

    number_elitism = int(elitism * population_size)

    for i in range(number_generations):
        if not fitness_function.__name__ == 'fitness_function':
            costs = [(fitness_function(individual), individual)
                     for individual in population]
        else:
            costs = [(fitness_function(individual, 'FCO'), individual)
                     for individual in population]
        nfe += 1
        # costs.sort()
        heapq.heapify(costs)
        ordered_individuals = [individual for (cost, individual) in costs]
        population = ordered_individuals[0:number_elitism]
        if not fitness_function.__name__ == 'fitness_function':
            scores.append(fitness_function(population[0]))
        else:
            scores.append(fitness_function(population[0], 'FCO'))
        #scores.append(fitness_function(population[0], 'FCO'))
        nfe += 1
        while len(population) < population_size:
            if random.random() < probability_mutation:
                i1 = random.randint(0, number_elitism)
                i2 = random.randint(0, number_elitism)
                population.append(
                    crossover(domain, ordered_individuals[i1], ordered_individuals[i2]))
            else:
                m = random.randint(0, number_elitism)
                population.append(
                    mutation(domain, step, ordered_individuals[m]))

    return costs[0][1], costs[0][0], scores, nfe, seed


def genetic_algorithm_with_reversals(domain, fitness_function, seed=random.randint(10, 100), seed_init=True, init=[], population_size=100, step=1,
                                     probability_mutation=0.2, elitism=0.2, n_k=250, step_length=100,
                                     number_generations=500, search=False):
    """ Genetic algorithm implemented with elitisim with n number of reversals.
        No. of reversals= number_generations/n_keach of n iter=step_length i.e n step reversal.


    Args:
        domain (list): List containing the upper and lower bound.i.e domain of our inputs
        fitness_function (function): This parameter accepts a fitness function of given optimization problem.
        init (list, optional): List for initializing the initial solution. Defaults to [].
        seed (int,optional): Set the seed value of the random seed generator. Defaults to random integer value.
        seed_init(bool,optional): True set's the seed of only population init generator, False sets all generators
        population_size (int, optional): The maximum size of the population to generate. Defaults to 100.
        probability_mutation (float, optional): Controls the rate of mutation of genes. Defaults to 0.2.
        elitism (float, optional): The percentage of population which proceeds onto next iter without changes. Defaults to 0.2.
        number_generations (int, optional): Analgous to epochs, but in this context refers to number of generations the algorithm evolves to . Defaults to 500.
        n_k (int, optional): Divides number of generations to get actual no of reversals. Defaults to 50.
        step_length (int,optional): The number of reversal steps in a given reversal. Defaults to 120.
        search (bool, optional): If True  solution is initialized as the result of a RandomSearch . Defaults to False.
        step (int, optional): Number of steps to the right or left to make changes in given solution. Defaults to 1.

    Returns:
        list: List containing the best_solution,
        int: The final cost after running the algorithm,
        list: List containing all costs during all epochs.
        int: The number of function evaluations(NFE) after running the algorithm
        int: Seed value used by random generators.
    """
    if seed_init:
        # Set the seed for initial population only
        r_init = random.Random(seed)
    else:
        # Same seeds for both init and other random generators
        r_init = random.Random(seed)
        random.seed(seed)
    population = []
    scores = []
    nfe = 0
    rev = 0
    for i in range(population_size):
        if search == True:
            solution, b_c, sc, r_nfe, s = random_search(
                domain, fitness_function, seed)
            nfe += r_nfe
        if len(init) > 0:
            solution = init
        else:
            solution = [r_init.randint(domain[i][0], domain[i][1])
                        for i in range(len(domain))]

        population.append(solution)

    number_elitism = int(elitism * population_size)

    for i in range(number_generations):
        if not fitness_function.__name__ == 'fitness_function':
            costs = [(fitness_function(individual), individual)
                     for individual in population]
        else:
            costs = [(fitness_function(individual, 'FCO'), individual)
                     for individual in population]
        nfe += 1
        if i % n_k == 0 and i != 0:
            if step_length == 1:
                costs.sort(reverse=True)
                rev += 1
            else:
                rev += 1
                for _ in range(step_length-1):
                    costs.sort(reverse=True)
                    ordered_individuals = [
                        individual for (cost, individual) in costs]
                    population = ordered_individuals[0:number_elitism]
                    if not fitness_function.__name__ == 'fitness_function':
                        scores.append(fitness_function(population[0]))
                    else:
                        scores.append(fitness_function(population[0], 'FCO'))
                    nfe += 1
                    while len(population) < population_size:
                        if random.random() < probability_mutation:
                            i1 = random.randint(0, number_elitism)
                            i2 = random.randint(0, number_elitism)
                            population.append(
                                crossover(domain, ordered_individuals[i1], ordered_individuals[i2]))
                        else:
                            m = random.randint(0, number_elitism)
                            population.append(
                                mutation(domain, step, ordered_individuals[m]))
            print(rev)  # To print the number of reversals
        else:
            heapq.heapify(costs)
        ordered_individuals = [individual for (cost, individual) in costs]
        population = ordered_individuals[0:number_elitism]
        if not fitness_function.__name__ == 'fitness_function':
            scores.append(fitness_function(population[0]))
        else:
            scores.append(fitness_function(population[0], 'FCO'))
        nfe += 1
        while len(population) < population_size:
            if random.random() < probability_mutation:
                i1 = random.randint(0, number_elitism)
                i2 = random.randint(0, number_elitism)
                population.append(
                    crossover(domain, ordered_individuals[i1], ordered_individuals[i2]))
            else:
                m = random.randint(0, number_elitism)
                population.append(
                    mutation(domain, step, ordered_individuals[m]))

    return costs[0][1], costs[0][0], scores, nfe, seed




