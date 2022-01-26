---
description: >
    Chaining procedure inspired by Nevergrad
hide_description: false
---

Iterated chaining is where you initialize the final solution vector of one algorithm, as the initial population of the other algorithm and continue this procedure for a number of times.Thus, any algorithm can be “Chained” together.
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
