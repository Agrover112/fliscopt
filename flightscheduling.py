
import math
import multiprocessing
import os
import random
from multiprocessing import Pool, Process, Queue

import matplotlib
import matplotlib.pyplot as plt

from algorithms import hill_climb, random_search, simulated_annealing ,genetic_algorithm
from fitness import fitness_function
from utils import people, plot_scores, print_schedule, read_file, time

matplotlib.use('TKAgg')

domain = [(0, 9)] * (len(people) * 2)  # 9 times * no.of people * to-from
read_file('flights.txt')  # 12 flights with 10 possibilites 10^12


def multiple_runs(algorithm, init=[], use_multiproc=False, n_proc=multiprocessing.cpu_count(), n=10):
    f = open(os.path.join('/mnt/d/MINOR PROJECT/final/results/' +
             algorithm.__name__+"_results.csv"), 'a+')
    if use_multiproc:
        d = domain
        fn = fitness_function
        inputs = [(d, fn)]*n

        # Multiprocessing starts here
        
        pool = multiprocessing.Pool(n_proc)
        start = time.time()
        # result=pool.starmap_async(random_search,inputs)   #Async run
        result = pool.starmap_async(algorithm, inputs)
        pool.close()  # Close the pool
        diff = round(time.time()-start, 3)
        f.write('MRun_no'+","+'Cost'+","+'Run_Time'+","+'Solution'+"\n")
        res = result.get()
        for i, r in enumerate(res):
            f.write(str(i)+","+str(r[1])+","+str((diff/10))+","+str(r[0])+"\n")
        f.close()
        print("Total time:", diff*n)
    else:
        f.write('Run_no'+","+'Cost'+","+'Run_Time'+","+'Solution'+"\n")
        times = []
        for i in range(n):
            start = time.time()
            soln, cost, _ = algorithm(domain, fitness_function)
            diff = round(time.time()-start, 3)
            times.append(diff)
            f.write(str(i)+","+str(cost)+","+str(diff)+","+str(soln)+"\n")
        f.close()
        print("Total time ", round(sum(times), 3))


def single_run(algorithm, init=[], save_fig=False, print_sch=True):
    start = time.time()
    global scores
    soln, cost, scores = algorithm(domain, fitness_function, init)
    diff = round(time.time()-start, 3)
    print("Time taken for single run ", diff)
    if algorithm.__name__ == 'simulated_annealing':
        plot_scores(scores, algorithm.__name__, save_fig, temp=algorithm.temp)
    elif algorithm.__name__ == 'genetic_algorithm':
        plot_scores(scores, algorithm.__name__, save_fig)
    else:
        plot_scores(scores, algorithm.__name__, save_fig)
    if print_sch:
        print_schedule(soln, 'FCO')
    return soln, cost


def sol_chaining(algorithm_1, algorithm_2, rounds=20, n_obs=2, tol=90,save_fig=False):
   #Note scores here is the best cost of each particular single_run 
    scores = []
    for i in range(rounds):
        if i == 0:
            soln, cost = single_run(algorithm_1, print_sch=False)
            scores.append(cost)
            print("Cost at {}=={}".format(i, cost))
        elif i == rounds-1:
            final_soln, cost = single_run(
                algorithm_2, init=soln, save_fig=False, print_sch=True)
            scores.append(cost)
            print("Cost at {}=={}".format(i, cost))
            plot_scores(scores,sol_chaining.__name__,save_fig)
            return final_soln,scores[-1],scores
        else:
            soln, cost = single_run(
                algorithm_1, init=init, save_fig=False, print_sch=False)
            print("Cost at {}=={}".format(i, cost))
            scores.append(cost)
        #random_solution = [random.randint(domain[i][0], domain[i][1])for i in range(len(domain))]
        # soln=soln+random_solution//2

        final_soln, cost = single_run(algorithm_2, init=soln, print_sch=False)
        scores.append(cost)
        if cost - random.randint(tol, 100) > int(sum(scores[-n_obs:])/n_obs):
            print("----Ending early at iteration{}----".format(i))
            print("Cost{}".format(cost))
            print_schedule(final_soln, 'FCO')
            plot_scores(scores,sol_chaining.__name__,save_fig)
            return final_soln, scores[-1],scores
        print("Cost at {}=={}".format(i, cost))
        init = final_soln


if __name__ == "__main__":
    # soln,cost,scores=random_search(domain,fitness_function)
    # print(soln)
    # print_schedule(soln,'FCO')
    multiple_runs(genetic_algorithm, n=5, use_multiproc=True)
    #final_soln,cost,scores = sol_chaining(hill_climb, simulated_annealing,save_fig=True)
    #soln, cost = single_run(genetic_algorithm, save_fig=False, print_sch=False)
    #multiple_runs(hill_climb,soln)
    # soln,cost=single_run(hill_climb,init=soln,save_fig=True)
