import random
import sys
from utils import plot_scores
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('TKAgg')
domain=[(-32,32)]*2
from fitness import ackley_N2
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
            cost = fitness_function(solution[0],solution[1])
        else: cost = fitness_function(solution,'FCO')
        nfe += 1
        if cost < best_cost:
            best_cost = cost
            best_solution = solution
        scores.append(best_cost)
    return best_solution, best_cost, scores, nfe, seed

if __name__ == '__main__':
    soln,cost,scores,nfe,seed=random_search(domain,ackley_N2)
    plot_scores(scores,'random_search',save_fig=False)
