import multiprocessing
import random
import sys
import time
from multiprocessing import Lock, Pool, Process, Queue

from algorithms import genetic_algorithm, genetic_algorithm_reversed,genetic_algorithm_with_reversals, hill_climb, random_search, simulated_annealing
from flightscheduling import domain, fitness_function
from fitness import *
"""def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()"""

""" Asynchronous multiprocessing implementation for searching algorithms"""
Q = Queue()
jobs = []
dic = {}
SCORES, BEST_COST, BEST_SOLUTION = [], [], []

def main():
    #d = domain['rosenbrock']*15
    d=domain['domain']
    f = fitness_function
    #f=rosenbrock
    #seeds=random.sample(range(10,100),10)  #List of seeds N seeds = N runs
    seeds=[10,24,32,100,20,67,13,19,65,51]
    temp_inputs = [(d,f)]*10
    inputs=[]
    for idx,seed in enumerate(seeds):
        inputs.append(temp_inputs[idx]+(seed,))



    # inputs=[(d,f)]
    # Multiprocessing starts here
    start = time.time() 
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.starmap_async(genetic_algorithm_with_reversals, inputs)  # Async run
    pool.close()
    pool.join()  # Close the pool
    print("", (time.time()-start))
    res = result.get()
    print("Run_Number\tSolution\t      Cost  NFE SEED",)
    for i, r in enumerate(res):
        print(i, r[0], r[1],r[3],r[4])

if __name__ == '__main__':
    main()
    
    # print(result._value[0][1])

    # for i in result :
    #  print(i)

    # print(v.get())
    #jobs = []
    # for i in range(10):
    #   print(multiprocessing.Process(target=random_search, args=(domain,fitness_function)))
    #montecarlos = [random_search(domain,fitness_function) ]
    #jobs = [multiprocessing.Process(mc) for mc in montecarlos]
    #for job in jobs: job.start()
    #for job in jobs: job.join()
    #results = [mc.results for mc in montecarlos]

    # for i in range(10):
    #    p = Process(target=random_search, args=(domain,fitness_function))
    #    jobs.append(p)
    #    p.start()
    #    p.join()
    #    print(Q.get())
