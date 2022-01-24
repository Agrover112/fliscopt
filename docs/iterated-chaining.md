---
layout: page
title: Iterated Chaining
description: >
 tldr
hide_description: true
sitemap: false
permalink: /docs/iterated-chaining
---

# Iterated Chaining

This method involves the use of a Chaining procedure inspired by Nevergrad .Where you initialize the final solution vector of one algorithm, as the initial population of the other algorithm and continue this procedure for a number of times.
Thus, any algorithm can be “Chained” together.
One of the disadvantages of chaining is that cost can easily diverge, and thus we have introduced an Early Stopping mechanism similar to those in Deep Learning libraries such as Keras/Tensorflow or PyTorch.

Use ``tolerance`` and ``n_obs`` parameters to control the Early Stopping. 

## Parameters


``tolerance:int``
Tolerance value is for how much we can tolerate a divergence in our loss/cost value. The higher the tolerance the more we tolerate essentially ,vice-versa.

``n_obs:int``
N_obs is used for calculating the average costs over the given number of observations.

``rounds:int``
We refer to the iterations of Iterated Chaining as `rounds`, so as to prevent confusion with respect to the ``iterations`` parameter of the ``algorithm_1/2`` local searches running inside it.

 ``def run(self,algorithm_1, algorithm_2)``

 ``algorithm_1``
Algorithm 1 here is the initial algorithm that can be passed here from the fliscopt algorithm implementations. Think of it as a WEAK algorithm. This algorithm passes it’s calculated solution to algorithm_2. Thus, a weak algorithm is better since it can provide more diversity artificially.
``algorithm_2``
Algorithm 2 here is the initial algorithm that can be passed here from the fliscopt algorithm implementations. Think of it as a relatively STRONG algorithm. A Strong algorithm refers to an algorithm that is better than algorithm_1 . 
We use a ``RS + Hill Climb`` combination in our experiments.

The main idea is that combining such algorithms can often result in a cost which is less than that of it’s two constituents.
