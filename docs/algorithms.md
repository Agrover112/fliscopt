Algorithms Available
Genetic Algorithm

Simple Genetic Algorithm has been implemented. All the variants of GA have these shared parameters as listed below:
population_size:int 
The initial population size of the Genetic Algorithm
step:int
This step parameter controls the amount of mutation.
Each mutation is a simple addition or subtraction of the particular gene by a step.

Note:Make sure that the step size is not too large, or else it will result in genes being out of the Upper or Lower Bounds of their domain.

probability_mutation:float
Controls the rate of mutation and crossover.
elitism:float
A float value which takes the top x% of population with minimum cost, and then appends it to the new population for Elitist selection.
number_generations:float
The number of generations of your GA.
search:bool
This parameter triggers a Random Search at the initial stage and sets the result of a Random Search as the initial population. The other way to set this is to use the init parameter (common to all) , where you can pass any arbitrary initial population.

GA with Reverse Operations

This method is like Differential Evolution but without its own mutation and cross-over operators. Thus the mutation and crossover rates are reversed.
Therefore, while initializing probability_mutation= probability_crossover in this case.

GA with Reversals

In this method we introduce Switching i.e maximize after a period of time and then continue to minimize our cost function. This is a switch in the behavior of our algorithm.

i/nk=0 & i ≠ 0 Reversal Process happens 
, i is the current iteration number.

n_k: This parameter is the denominator which if divisible by the current iteration number I, (other than the first iteration) , results in a reversal process instead of the normal minimization process.
The denominator factor i/n_k which determines the number of iterations which are multiples of n_k where reversals take place.Defaults to 250.

step_length: This controls the number of reverse steps i.e number of reverse (maximization) iterations.


GA with Stochastic Reversals
We perform the switching similarly as above, but we use a Random Search in the maximization stage , whereas the GA minimizes in the normal stage.
Hill Climb
Simulated Annealing
Random Search
Iterated Chaining

This method involves the use of a Chaining procedure inspired by Nevergrad .Where you initialize the final solution vector of one algorithm, as the initial population of the other algorithm and continue this procedure for a number of times.Thus, any algorithm can be “Chained” together.
One of the disadvantages of chaining is that cost can easily diverge, and thus we have introduced an Early Stopping mechanism similar to those in Deep Learning libraries such as Keras/Tensorflow or PyTorch.
Use tolerance and n_obs parameters to control the Early Stopping. 


tolerance:int
Tolerance value is for how much we can tolerate a divergence in our loss/cost value. The higher the tolerance the more we tolerate essentially ,vice-versa.
n_obs:int
N_obs is used for calculating the average costs over the given number of observations.

	rounds:int
We refer to the iterations of Iterated Chaining as rounds, so as to prevent confusion with respect to the Iterations parameter of the algorithm_1/2 local searches running inside it.

 def run(self,algorithm_1, algorithm_2)

 algorithm_1
Algorithm 1 here is the initial algorithm that can be passed here from the fliscopt algorithm implementations. Think of it as a WEAK algorithm. This algorithm passes it’s calculated solution to algorithm_2. Thus, a weak algorithm is better since it can provide more diversity artificially.
 algorithm_2
Algorithm 2 here is the initial algorithm that can be passed here from the fliscopt algorithm implementations. Think of it as a relatively STRONG algorithm. A Strong algorithm refers to an algorithm that is better than algorithm_1 . 
We use a RS + Hill Climb combination in our experiments.

The main idea is that combining such algorithms can often result in a cost which is less than that of it’s two constituents.

Some of the common, parameters are as follows:

domain:list
This function accepts a list of tuples, where each tuple entry indicates the domain at that position 
For Ex: domain for x,y a 2-D list would be [(-5,5),(-5,7)]

fitness_function
This parameter accepts the actual cost function which needs to be minimized.

seed:int 
The random seed to initialize for stochastic operations in the algorithm.

seed_init:bool  
This random seed only sets the generator which generates the initial population.The rest of the stochasticity is handled by the seed operator. Thus, if you want to evaluate your algorithm but want to have the same initial population then setting this seed is helpful.

init:list 
This parameter accepts a list in the form of a 1-D list ,which can be used to set the initial population/search space.

max_time:int
This parameter controls the amount of time after which we can terminate our algorithm.

epochs:int
To set the number of iterations of the algorithm.

These are common parameters present in all the algorithms.
