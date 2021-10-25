from fliscopt.utils.util import print_schedule, read_file,plot_scores
from fliscopt.rs import RandomSearch
from fliscopt.ga import GA, ReverseGA, GAReversals
from fliscopt.hc import HillClimb
from fliscopt.chaining import IteratedChaining
from fliscopt.multiproc import multiple_runs
from fliscopt.fitness import fitness_function,domain,griewank


"""

Now why is this useful? Well you can use the data file and the algoeithms for something known as
optimization. Here all algorithms can be used to minimize any arbitrary function.
Now minimzing any function such as let's say minimize the time taken to reach a place .

So basically you can read a file using read_file. This contains the flight data.
Then using the above imports, you should theoretically as of now be able to run
each of the search algorithms on the data.
You can then provide a fitness function to the search algorithms and the respective domain.
Default domain and fitness function are domain['domain'], fitness_function respectively.
Other's can simply be added in domain=domain['griewank] , fitness_function=griewank which are the names of 
the fucntions to be optimized. 
Each of the algorithms has a different set of parameters. Depending on the algorithm,
and all of them have common parameters such as domain, init for initialzing the list of solutions if you need 
to yourself otherwise it starts from a totally random point; fitness_function which is to be optimized,
and the number of iterations lol.

Now .run() allows us to use multiprocessing.
and Iterated Chaining under the hood just runs algo1 then passes the soln it generates to algo2
and repeats the process for n-number of iterations. Basically 
algo1--soln-->algo2--algo2soln-->algo1.....n-times

Iterated Chaining and GAReversals and ReverseGA are algos I haven;t really found being 
implemented. So I implemented them.

"""



read_file('flights.txt')
ic=IteratedChaining(rounds=5, n_obs=2, tol=90)
soln, cost, scores, nfe=ic.run('RandomSearch', 'HillClimb') 
print_schedule(soln,'FCO')
#multiple_runs(ReverseGA, domain, fitness_function, record=False, n=2)

read_file('flights.txt')
sga=GAReversals(seed_init=False,search=False,n_k=250,number_generations=1000)
soln, cost, scores, nfe, seed = sga.run(domain=domain['domain'], fitness_function=fitness_function,seed=5)
plot_scores(scores, sga.get_base(),fname='flight_scheduling', save_fig=False)

hc=HillClimb(seed_init=False,max_time=0.0000001)
# All domains defined with a single-tuple/or without a multiplier have n-dimensional Input Domain
soln, cost, scores, nfe, seed=hc.run(domain=domain['griewank']*5,fitness_function=griewank,seed=5)
plot_scores(scores,hc.get_name(),fname='griewank',save_fig=False)