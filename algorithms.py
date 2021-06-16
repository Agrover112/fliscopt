import heapq
import math
import random
import sys

"""Add option to select mutation type in GA method.
       Add bit flip mutation
       Wrapp all different mutation types in a class XD
    """
def random_search(domain, fitness_function, init=[], epochs=100):
    """ Random search algorithm implemented

    Args:
        domain (list): List containing the upper and lower bound.i.e domain of our inputs
        fitness_function (function): This parameter accepts a fitness function of given optimization problem.
        init (list, optional): List for initializing the initial solution. Defaults to [].
        epochs (int, optional): Number of times the algorithm runs. Defaults to 100.

    Returns:
        list: List containing the best_solution,
        int: The final cost after running the algorithm,
        list: List containing all costs during all epochs.
    """

    best_cost = sys.maxsize
    scores = []
    if len(init) > 0:
        solution = init
    else:
        solution = [random.randint(domain[i][0], domain[i][1])
                    for i in range(len(domain))]
    for i in range(epochs):
        if i != 0:
            solution = [random.randint(domain[i][0], domain[i][1])
                        for i in range(len(domain))]
        cost = fitness_function(solution, 'FCO')
        if cost < best_cost:
            best_cost = cost
            best_solution = solution
        scores.append(best_cost)
    return best_solution, best_cost, scores


def hill_climb(domain, fitness_function, init=[], epochs=100):
    """ Simple Hill Climbing algorithm implemented

    Args:
        domain (list): List containing the upper and lower bound.i.e domain of our inputs
        fitness_function (function): This parameter accepts a fitness function of given optimization problem.
        init (list, optional): List for initializing the initial solution. Defaults to [].
        epochs (int, optional): Number of times the algorithm runs. Defaults to 100.

    Returns:
        list: List containing the best_solution,
        int: The final cost after running the algorithm,
        list: List containing all costs during all epochs.
    """
    count = 0
    scores = []
    if len(init) > 0:
        solution = init
    else:
        solution = [random.randint(domain[i][0], domain[i][1])
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

        actual = fitness_function(solution, 'FCO')
        best = actual
        for i in range(len(neighbors)):
            count += 1
            cost = fitness_function(neighbors[i], 'FCO')
            if cost < best:
                best = cost
                solution = neighbors[i]
            scores.append(best)

        if best == actual:
            print('Count: ', count)
            break

    return solution, best, scores


def simulated_annealing(domain, fitness_function, init=[], temperature=50000.0, cooling=0.95, step=1):
    """ Simulated annealing algorithm implemented with temeperature and cooling parameters.


    Args:
        domain (list): List containing the upper and lower bound.i.e domain of our inputs
        fitness_function (function): This parameter accepts a fitness function of given optimization problem.
        init (list, optional): List for initializing the initial solution. Defaults to [].
        epochs (int, optional): Number of times the algorithm runs. Defaults to 100.
        temperature (float, optional): This parameter controls the degree of randomness.Increasing it increases the search space. Defaults to 50000.0.
        cooling (float, optional): The margin by which temperature decreases at each epoch. Defaults to 0.95.
        step (int, optional): Number of steps to the right or left to make changes in given solution. Defaults to 1.

    Returns:
        list: List containing the best_solution,
        int: The final cost after running the algorithm,
        list: List containing all costs during all epochs.
    """
    count = 0
    scores = []
    simulated_annealing.temp = []

    if len(init) > 0:
        solution = init
    else:
        solution = [random.randint(domain[i][0], domain[i][1])
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
        cost = fitness_function(solution, 'FCO')
        cost_temp = fitness_function(temp_solution, 'FCO')
        prob = pow(math.e, (-cost_temp - cost) / temperature)
        best = cost
        if (cost_temp < cost or random.random() < prob):
            best = cost_temp
            solution = temp_solution
        scores.append(best)

        temperature = temperature * cooling
        simulated_annealing.temp.append(temperature)

    print('Count: ', count)
    return solution, best, scores


def mutation(domain, step, solution):
    gene = random.randint(0, len(domain)-1)
    mutant = solution
    if random.random() < 0.5:
        if solution[gene] != domain[gene][0]:
            mutant = solution[0:gene]+[solution[gene]-step]+solution[gene+1:]
    else:
        if solution[gene] != domain[gene][1]:
            mutant = solution[0:gene]+[solution[gene]+step]+solution[gene+1:]
    return mutant


def multi_mutation(domain, step, solution):
    li = [i for i in range(domain[0][0], domain[0][1]+1)]
    gene = random.randint(0, len(domain)-1)
    if gene in li:
        li.remove(gene)
    gene2 = random.choice(li)
    mutant = solution
    if random.random() < 0.5:
        if solution[gene] != domain[gene][0]:
            mutant = solution[0:gene]+[solution[gene]-step]+solution[gene+1:]
    else:
        if solution[gene] != domain[gene][1]:
            mutant = solution[0:gene]+[solution[gene]+step]+solution[gene+1:]
    if random.random() < 0.5:
        if solution[gene2] != domain[gene2][0]:
            mutant = solution[0:gene2] + \
                [solution[gene2]-step]+solution[gene2+1:]
    else:
        if solution[gene2] != domain[gene2][1]:
            mutant = solution[0:gene2] + \
                [solution[gene2]+step]+solution[gene2+1:]

    return mutant


def crossover(domain, solution_1, solution_2):
    gene = random.randint(1, len(domain) - 2)
    return solution_1[0:gene] + solution_2[gene:]


def genetic_algorithm(domain, fitness_function, init=[], population_size=100, step=1,
                      probability_mutation=0.2, elitism=0.2,
                      number_generations=500, search=False):
    """ Genetic algorithm implemented with elitisim.


    Args:
        domain (list): List containing the upper and lower bound.i.e domain of our inputs
        fitness_function (function): This parameter accepts a fitness function of given optimization problem.
        init (list, optional): List for initializing the initial solution. Defaults to [].
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
    """
    population = []
    scores = []
    for i in range(population_size):
        if search == True:
            solution = random_search(domain, fitness_function)
        if len(init) > 0:
            solution = init
        else:
            solution = [random.randint(domain[i][0], domain[i][1])
                        for i in range(len(domain))]

        population.append(solution)

    number_elitism = int(elitism * population_size)

    for i in range(number_generations):
        costs = [(fitness_function(individual, 'FCO'), individual)
                 for individual in population]
        # costs.sort()
        heapq.heapify(costs)
        ordered_individuals = [individual for (cost, individual) in costs]
        population = ordered_individuals[0:number_elitism]
        scores.append(fitness_function(population[0], 'FCO'))
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
    return costs[0][1], costs[0][0], scores


def genetic_algorithm_reversed(domain, fitness_function, init=[], population_size=100, step=1,
                      probability_mutation=0.2, elitism=0.2,
                      number_generations=500, search=False):
    """ Genetic algorithm implemented with elitisim.


    Args:
        domain (list): List containing the upper and lower bound.i.e domain of our inputs
        fitness_function (function): This parameter accepts a fitness function of given optimization problem.
        init (list, optional): List for initializing the initial solution. Defaults to [].
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
    """
    population = []
    scores = []
    for i in range(population_size):
        if search == True:
            solution = random_search(domain, fitness_function)
        if len(init) > 0:
            solution = init
        else:
            solution = [random.randint(domain[i][0], domain[i][1])
                        for i in range(len(domain))]

        population.append(solution)

    number_elitism = int(elitism * population_size)

    for i in range(number_generations):
        costs = [(fitness_function(individual, 'FCO'), individual)
                 for individual in population]
        # costs.sort()
        heapq.heapify(costs)
        ordered_individuals = [individual for (cost, individual) in costs]
        population = ordered_individuals[0:number_elitism]
        scores.append(fitness_function(population[0], 'FCO'))
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
                
    return costs[0][1], costs[0][0], scores


