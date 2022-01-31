---
description: >
    Switching is introduced with these reversals
hide_description: false
---

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
