---
layout: page
title: Documentation
description: >
  Algo list
hide_description: true
sitemap: false
permalink: /docs/algolist
---


# Algorithms List

1. [Genetic Algorithm](https://github.com/Agrover112/fliscopt/blob/docs/docs/genetic.md)

2. GA with Reversals

3. GA with Stochastic Reversals

4. Hill Climb

6. Simulated Annealing

8. Random Search

10. [Iterated Chaining](https://github.com/Agrover112/fliscopt/blob/docs/docs/iterated-chaining.md)




## Parameters

Each algorithm has these common fn parameters:


``domain:list(tuples)``

This function accepts a list of tuples, where each tuple entry indicates the domain at that position 

**For Ex:** 
``domain`` for x,y a 2-D list would be ``[(-5,5),(-5,7)]``

``fitness_function``
This parameter accepts the actual cost function which needs to be minimized.

``seed:int ``

The random seed to initialize for stochastic operations in the algorithm.

``seed_init:bool ``

This random seed only sets the generator which generates the initial population.
The rest of the stochasticity is handled by the seed operator. 
Thus, if you want to evaluate your algorithm but want to have the same initial population then setting this seed is helpful.

``init:list ``

This parameter accepts a list in the form of a 1-D list ,which can be used to set the initial population/search space.

``max_time:int``

This parameter controls the amount of time after which we can terminate our algorithm.

``epochs:int``

To set the number of iterations of the algorithm.
These are common parameters present in all the algorithms.
