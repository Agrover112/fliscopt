
from utils import read_file , time, plot_scores ,print_schedule , people
from fitness import fitness_function
from algorithms import random_search ,hill_climb, simulated_annealing
import os

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TKAgg')


domain = [(0,9)] * (len(people) * 2) # 9 times * no.of people * to-from
read_file('flights.txt')  # 12 flights with 10 possibilites 10^12



def multiple_runs(algorithm,init=[],use_multithreading=False,n=10):
    f=open(os.path.join('/mnt/d/MINOR PROJECT/final/results/'+algorithm.__name__+"_results.csv"),'a+')
    f.write('Run_no'+","+'Cost'+","+'Run_Time'+","+'Solution'+"\n")
    for i in range(n):
        start=time.time()
        soln,cost,_=algorithm(domain,fitness_function)
        diff=round(time.time()-start,3)
        f.write(str(i)+","+str(cost)+","+str(diff)+","+str(soln)+"\n")
    f.close()

def single_run(algorithm,init=[],save_fig=False): 
     start=time.time()
     soln,cost,scores=algorithm(domain,fitness_function,init)
     diff=round(time.time()-start,3)
     print("Time taken for single run ",diff)
     if algorithm.__name__ == 'simulated_annealing':
         plot_scores(scores,algorithm.__name__,save_fig,temp=algorithm.temp)
     else: 
         plot_scores(scores,algorithm.__name__,save_fig)
     print_schedule(soln,'FCO')
     return soln,cost


if __name__=="__main__":
    #soln,cost,scores=random_search(domain,fitness_function)
    #print(soln)
    #print_schedule(soln,'FCO')
    #multiple_runs(hill_climb)
    soln,cost=single_run(random_search,save_fig=True)
    multiple_runs(hill_climb,soln)
    soln,cost=single_run(hill_climb,init=soln,save_fig=True)
