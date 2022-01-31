---
layout: page
title: Genetic Algorithms available
description: >
  GA description
<<<<<<< HEAD
hide_description: false
=======
hide_description: true
>>>>>>> c50061e70af1d68e9fba10fd71a98bde042e8608
sitemap: false
permalink: /docs/genetic-algorithms
---
# Algorithms

## Genetic Algorithm (GA)

Simple Genetic Algorithm has been implemented. All the variants of GA have these shared parameters as listed below:

``population_size:int ``
The initial population size of the Genetic Algorithm.

``step:int``
This step parameter controls the amount of mutation.
Each mutation is a simple addition or subtraction of the particular gene by a step.


**Note:** Make sure that the step size is not too large, or else it will result in genes being out of the Upper or Lower Bounds of their domain.

``probability_mutation:float``
Controls the rate of mutation and crossover.

``elitism:float``
A float value which takes the top x% of population with minimum cost, and then appends it to the new population for Elitist selection.

``number_generations:float``
The number of generations of your GA.

``search:bool``
This parameter triggers a Random Search at the initial stage and sets the result of a Random Search as the initial population. The other way to set this is to use the init parameter (common to all) , where you can pass any arbitrary initial population.






# GA with Reverse Operations

This method is like Differential Evolution but without its own mutation and cross-over operators. Thus the mutation and crossover rates are reversed.
Therefore, while initializing probability_mutation= probability_crossover in this case.

# GA with Reversals

In this method we introduce Switching i.e maximize after a period of time and then continue to minimize our cost function. This is a switch in the behavior of our algorithm.

`i/nk=0 & i ≠ 0 `
Reversal Process happens 
, `i` is the current iteration number.

`n_k:int` 
This parameter is the denominator which if divisible by the current iteration number `i`, (other than the first iteration) , results in a reversal process instead of the normal minimization process.
The denominator factor i/n_k which determines the number of iterations which are multiples of `n_k` where reversals take place.Defaults to 250.

`step_length:int` 
This controls the number of reverse steps i.e number of reverse (maximization) iterations.


# GA with Stochastic Reversals
We perform the switching similarly as above, but we use a Random Search in the maximization stage , whereas the GA minimizes in the normal stage.

