
import math
import multiprocessing
import os
import random
from multiprocessing import Pool, Process, Queue

import matplotlib
import matplotlib.pyplot as plt

from algorithms import (genetic_algorithm, genetic_algorithm_reversed,
                        genetic_algorithm_with_reversals, hill_climb,
                        random_search, simulated_annealing)

from fitness import *
from utils.ga_utils import multi_mutation, mutation
from utils.utils import people, plot_scores, print_schedule, read_file, time
    
matplotlib.use('TKAgg') # Remove if not using WSL

_FLIGHTS_FILE_='flights.txt'

read_file(_FLIGHTS_FILE_)  # 12 flights with 10 possibilites 10^12


def multiple_runs(algorithm,domain,fitness_function, init=[], use_multiproc=False, n_proc=multiprocessing.cpu_count(), n=10):
    f = open(os.path.join('/mnt/d/MINOR PROJECT/final/results/multi_proc/' +fitness_function.__name__+'/'+
             algorithm.__name__+"_results.csv"), 'a+')
    if use_multiproc:
        d = domain
        fn = fitness_function
        seeds=[10,24,32,100,20,67,13,19,65,51,35,61,154,85,144,162,48,79,69,186]
        if n>0 and n<20:
            seeds=seeds[:n] # Some defined seeds
        temp_inputs = [(d, fn)]*n              # Temp inputs
        inputs=[]
        for idx,seed in enumerate(seeds):           # Add seeds to all inputs
            inputs.append(temp_inputs[idx]+(seed,))   

        # Multiprocessing starts here
        start = time.time()
        pool = multiprocessing.Pool(n_proc)

        # result=pool.starmap_async(random_search,inputs)   #Async run
        result = pool.starmap_async(algorithm, inputs)
        pool.close()
        pool.join()  # Close the pool
        #diff = round(time.time()-start, 3)
        diff=time.time()-start
        print("Total time:", diff)
        f.write('MRun_no'+","+'Cost'+","+'Run_Time'+","+'Solution'+","+'Nfe'+","+'Seed'+"\n")
        res = result.get()
        for i, r in enumerate(res):
            f.write(str(i)+","+str(r[1])+","+str((diff/10))+","+str(r[0])+","+str(r[3])+","+str(r[4])+"\n")
        f.close()

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

def multiple_runs_itr_chaining(algorithm_1, algorithm_2,domain,fitness_function,seed=random.randint(10,100), rounds=10 , n_obs=2, tol=90, save_fig=False,n=20):
    res=list([])
    seeds=[10,24,32,100,20,67,13,19,65,51,35,61,154,85,144,162,48,79,69,186]
    if n>0 and n<20:
            seeds=seeds[:n]
    for i in seeds:
        start=time.time()
        final_soln,cost,scores,nfe = sol_chaining(algorithm_1,algorithm_2 ,domain,fitness_function,save_fig=True,seed=i,rounds=rounds,n_obs=n_obs,tol=tol)
        res.append([cost,time.time()-start,nfe])
    
    with open('./results/multi_proc/fitness_function/iterated_solution_chaining.csv','w+') as f:
        f.write("Cost"+","+"Run_Time"+","+"NFE"+"\n")
        for item in res:
            f.write(str(item[0]) + "," + str(item[1]) +"," + str(item[2])+ "\n")

 
def single_run(algorithm,domain,fitness_function,init=[],seed=random.randint(10,100),seed_init=True,save_fig=False, print_sch=True): 
    global scores

    start = time.time()
    soln, cost, scores,nfe,seed= algorithm(domain, fitness_function,seed,seed_init,init)
    diff = round(time.time()-start, 3)
    print("Time taken for single run ", diff)
    if algorithm.__name__ == 'simulated_annealing':
        plot_scores(scores, algorithm.__name__, save_fig, temp=algorithm.temp,fname=fitness_function.__name__)
    else:
        plot_scores(scores, algorithm.__name__, save_fig,fname=fitness_function.__name__)
        
    if print_sch and fitness_function.__name__ == 'fitness_function':
        print_schedule(soln, 'FCO')
    return soln, cost,nfe

def sol_chaining(algorithm_1, algorithm_2,domain,fitness_function,seed=random.randint(10,100), rounds=10 , n_obs=2, tol=90, save_fig=False):
   # Note scores here is the best cost of each particular single_run
    scores = []
    NFE=0
    for i in range(rounds):
        if i == 0:
            soln, cost,nfe = single_run(algorithm_1,domain,fitness_function,save_fig=True, print_sch=False,seed=seed)
            soln=mutation(domain,random.randint(0,1),soln) # Either 1 step or no step InitMutation
            #soln=multi_mutation(domain,1,soln)
            scores.append(cost)
            NFE+=nfe
            print("Cost at {}=={}".format(i, cost))
        elif i == rounds-1:
            final_soln, cost,nfe = single_run(
                algorithm_2,domain=domain,fitness_function=fitness_function, init=soln, save_fig=True, print_sch=False)
            scores.append(cost)
            NFE+=nfe
            print("Cost at {}=={}".format(i, cost))
            plot_scores(scores, sol_chaining.__name__, save_fig)
            return final_soln, scores[-1], scores,NFE
        else:
            soln, cost,nfe = single_run(
                algorithm_1,domain=domain,fitness_function=fitness_function, init=init, save_fig=True, print_sch=False)
            print("Cost at {}=={}".format(i, cost))
            soln=mutation(domain,random.randint(0,1),soln)
            #soln=multi_mutation(domain,1,soln)
            scores.append(cost)
            NFE+=nfe

        final_soln, cost,nfe = single_run(algorithm_2,domain=domain,fitness_function=fitness_function, init=soln,save_fig=True, print_sch=False)
        scores.append(cost)
        NFE+=nfe
        if cost - random.randint(tol, 100) > int(sum(scores[-n_obs:])/n_obs):
            print("----Ending early at iteration{}----".format(i))
            print("Cost{}".format(cost))
            if fitness_function.__name__ == 'fitness_function':
                print_schedule(final_soln, 'FCO')
            #plot_scores(scores, sol_chaining.__name__, save_fig)
            return final_soln, scores[-1], scores,NFE
        print("Cost at {}=={}".format(i, cost))
        init = mutation(domain,1,final_soln)  # IntMutation



def main():
    soln, cost,nfe = single_run(genetic_algorithm_with_reversals,domain['griewank']*13,griewank,seed_init=False, save_fig=False, print_sch=True)
    print(soln,cost,nfe)
    print_schedule(soln,'FCO')
    #multiple_runs(simulated_annealing,domain[ 'matyas'],matyas,n=20,use_multiproc=True)
    #multiple_runs(random_search,domain['matyas'],matyas,n=20,use_multiproc=True)
    #multiple_runs(hill_climb,domain['griewank']*13,griewank,n=20,use_multiproc=True)
    #multiple_runs(genetic_algorithm,domain['three_hump_camel'],three_hump_camel,n=20,use_multiproc=True)
    #multiple_runs(genetic_algorithm_reversed,domain['three_hump_camel'],three_hump_camel,n=20,use_multiproc=True)
    #multiple_runs(genetic_algorithm_with_reversals,domain['three_hump_camel'],three_hump_camel,n=20,use_multiproc=True)
    #soln,cost=single_run(simulated_annealing,save_fig=False,print_sch=False,domain=domain['griewank']*13,fitness_function=griewank,seed=10)

if __name__ == "__main__":
    #CHANGES In order:
    #    1. Exception handling
    #    2. SHorten parameter names?
    #    3. Change to multiproc functions/restructuring?
    main()
    

