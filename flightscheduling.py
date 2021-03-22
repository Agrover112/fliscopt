
import math
import multiprocessing
import os
from multiprocessing import Pool, Process, Queue

import matplotlib
import matplotlib.pyplot as plt

from algorithms import hill_climb, random_search, simulated_annealing
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
        start = time.time()
        pool = multiprocessing.Pool(n_proc)
        # result=pool.starmap_async(random_search,inputs)   #Async run
        result = pool.starmap_async(algorithm, inputs)
        pool.close()  # Close the pool
        diff = round(time.time()-start, 3)
        f.write('MRun_no'+","+'Cost'+","+'Run_Time'+","+'Solution'+"\n")
        res = result.get()
        for i, r in enumerate(res):
            f.write(str(i)+","+str(r[1])+","+str((diff/10))+","+str(r[0])+"\n")
        f.close()
        print("Total time:", diff)
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


def single_run(algorithm, init=[], save_fig=False):
    start = time.time()
    soln, cost, scores = algorithm(domain, fitness_function, init)
    diff = round(time.time()-start, 3)
    print("Time taken for single run ", diff)
    if algorithm.__name__ == 'simulated_annealing':
        plot_scores(scores, algorithm.__name__, save_fig, temp=algorithm.temp)
    else:
        plot_scores(scores, algorithm.__name__, save_fig)
    print_schedule(soln, 'FCO')
    return soln, cost


if __name__ == "__main__":
    # soln,cost,scores=random_search(domain,fitness_function)
    # print(soln)
    # print_schedule(soln,'FCO')
    multiple_runs(simulated_annealing, n=20, use_multiproc=True)
    # soln,cost=single_run(random_search,save_fig=True)
    # multiple_runs(hill_climb,soln)
    # soln,cost=single_run(hill_climb,init=soln,save_fig=True)
