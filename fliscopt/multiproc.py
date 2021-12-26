import os
import sys
sys.path.append("..")


import multiprocessing
import time
from multiprocessing import Queue
from .utils.util import read_file

from .fitness import *
from .ga import GA, GARSReversals,ReverseGA, GAReversals

import rich

""" Asynchronous multiprocessing implementation for searching algorithms"""

def multiple_runs(algorithm, domain, fitness_function, init=[], record=False, n_proc=multiprocessing.cpu_count(),
                  n=10):
        if not os.path.exists(os.getcwd() + '/results'):
            os.makedirs(os.getcwd()+ '/' + 'results', exist_ok=True)
        if not os.path.exists(os.getcwd() + '/results/multi_proc'):
            os.makedirs(os.getcwd() +'/results/multi_proc', exist_ok=True)
        if not os.path.exists(os.getcwd() + '/results/multi_proc/'+fitness_function.__name__):
            os.makedirs(os.getcwd() +'/results/multi_proc/'+fitness_function.__name__, exist_ok=True)


        f = open(os.path.join(os.getcwd()+'/results/multi_proc/' + fitness_function.__name__ + '/' +
                            algorithm.__name__ + "_results.csv"), 'a+',newline='\n')

        d = domain
        fn = fitness_function
        algo=algorithm()
        seeds = [10, 24, 32, 100, 20, 67, 13, 19, 65, 51, 35, 61, 154, 85, 144, 162, 48, 79, 69, 186]
        if n > 0 and n < 20:
            seeds = seeds[:n]  # Some defined seeds
        temp_inputs = [(d, fn)] * n  # Temp inputs
        inputs = []
        for idx, seed in enumerate(seeds):  # Add seeds to all inputs
            inputs.append(temp_inputs[idx] + (seed,))

            # Multiprocessing starts here
        start = time.time()
        pool = multiprocessing.Pool(n_proc)

        # result=pool.starmap_async(random_search,inputs)   #Async run
        result = pool.starmap_async(algo.run, inputs)
        pool.close()
        pool.join()  # Close the pool
        # diff = round(time.time()-start, 3)
        diff = time.time() - start
        print("Total time:", diff)
        res = result.get()
        if record:
            f.write('MRun_no' + "," + 'Cost' + "," + 'Run_Time' + "," + 'Solution' + "," + 'Nfe' + "," + 'Seed' + "\n")
            for i, r in enumerate(res):
                f.write(str(i) + "," + str(r[1]) + "," + str((diff / 10)) + "," + str(r[0]) + "," + str(r[3]) + "," + str(
                    r[4]) + "\n")
            f.close()
        else: 
            f.close()
            rich.print("[bold red]Run_Number[/bold red]\t[bold green]Solution[bold green]\t      [bold magenta]Cost[/bold magenta]  [bold magenta]NFE[/bold magenta] SEED", )
            for i, r in enumerate(res):
                print(i, r[0], r[1], r[3], r[4])


 



if __name__ == '__main__':
    read_file('flights.txt')
    multiple_runs(GA, domain['domain'], fitness_function, record=True, n=10)

    