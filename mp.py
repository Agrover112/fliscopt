import multiprocessing
from multiprocessing import Pool ,Process ,Queue
import time
from algorithms import random_search
from flightscheduling import domain ,fitness_function
import os
import sys
import random
from multiprocessing import Process, Lock

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


Q=Queue()
jobs = []
dic={}
SCORES, BEST_COST, BEST_SOLUTION=[],[],[]
"""def random_search(domain, fitness_function,init=[],epochs=1000):
  best_cost = sys.maxsize
  scores=[]
  if len(init) > 0:
    solution = init
  else:
    solution = [random.randint(domain[i][0],domain[i][1]) for i in range(len(domain))]
  for i in range(epochs):
    if i!=0:
      solution = [random.randint(domain[i][0],domain[i][1]) for i in range(len(domain))]
    cost=fitness_function(solution,'FCO')
    if cost< best_cost:
      best_cost=cost
      best_solution=solution
    scores.append(best_cost)
  return best_solution,best_cost,scores  
  #Q.put(str(best_solution)+" "+str(best_cost))
  #print(best_cost) 
"""
if __name__ == '__main__':
    
    d=domain
    f=fitness_function
    inputs=[(d,f)]*10
    #inputs=[(d,f)]
    # Multiprocessing starts here
    start=time.time()
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result=pool.starmap_async(random_search,inputs)   #Async run
    pool.close()
    pool.join()                                      #Close the pool
    print("",(time.time()-start))
    res=result.get()
    #print(res)
    for i,r in enumerate(res):
        print(i,r[0],r[1])
    #print(result._value[0][1])




















    #for i in result :
    #  print(i)
    
    #print(v.get())
    #jobs = []
    #for i in range(10):
    #   print(multiprocessing.Process(target=random_search, args=(domain,fitness_function)))
    #montecarlos = [random_search(domain,fitness_function) ]
    #jobs = [multiprocessing.Process(mc) for mc in montecarlos]
    #for job in jobs: job.start()
    #for job in jobs: job.join()
    #results = [mc.results for mc in montecarlos]
    
    #for i in range(10):
    #    p = Process(target=random_search, args=(domain,fitness_function))
    #    jobs.append(p)
    #    p.start()
    #    p.join()
    #    print(Q.get())



  

    