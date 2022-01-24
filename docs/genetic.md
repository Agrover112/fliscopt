---
layout: page
title: Genetic Algorithms available
description: >
  tldrtldr
hide_description: true
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


**Note:**Make sure that the step size is not too large, or else it will result in genes being out of the Upper or Lower Bounds of their domain.

``probability_mutation:float``
Controls the rate of mutation and crossover.

``elitism:float``
A float value which takes the top x% of population with minimum cost, and then appends it to the new population for Elitist selection.

``number_generations:float``
The number of generations of your GA.

``search:bool``
This parameter triggers a Random Search at the initial stage and sets the result of a Random Search as the initial population. The other way to set this is to use the init parameter (common to all) , where you can pass any arbitrary initial population.
