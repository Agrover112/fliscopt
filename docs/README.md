---
description: >
  What is Fliscopt & how do I install it?
hide_description: false
permalink: /docs/
---

# About Fliscopt
### What is Fliscopt?
	Fliscopt is a short name for the term Flight Scheduling Optimization . It is a library you can use for scheduling flights which are round trips  from given locations to a given location and back. Fliscopt takes care of the constraints imposed such as waiting time, departure time, cost of the flight,etc. 

### Why should I use it?
You can easily run novel variants of Genetic Algorithm’s which have been tried and tested on benchmarks , to optimize for your given task. Moreover, fliscopt provides a simple interface which can be used to also learn about the algorithm’s and optimize your given task at hand. Simply plug your own cost function in based on the convention and enjoy the power of optimization.

### How to use it?
All the details are mentioned in the README.md, which explains beautifully how to install it as a package from PyPy or to clone it from the source.

# Installation
* [Using pip](/fliscopt/docs/Installation) -> Find prereleases & finished versions here
* [PyPi Project Page](https://pypi.org/project/fliscopt/) -> Find meta information & dependencies here

# Algorithms available
* [All algorithms](/fliscopt/docs/algolist) -> Descriptions of all algorithms with relevant params
* [Genetic Algorithms](/fliscopt/docs/genetic-algorithms) -> Solving both constrained & unconstrained optimisation problems
* [Genetic Reversal](/fliscopt/docs/genetic-reversal) -> Introducing switching to genetic algorithms
* [Iterated chaining](/fliscopt/docs/iterated-chaining) -> Chaining procedure inspired by Nevergrad
* [What is switching?](/fliscopt/docs/switching) -> A guide for what switching is and how it's used

<<<<<<< HEAD
# Suggested reading/viewing
* [Universal theory of switching](https://www.youtube.com/watch?v=aTqgPbKQUD8&feature=youtu.be)
* [arxiv pre-print incoming [Stay Tuned]](#)
=======
## For PyPy users
The instructions for setup are mentioned in the setup directory. Alternatively, you can set up using this bash script. A requirements file is provided just in case.
The script creates and activates a PyPy Conda environment with all libraries and dependencies.
```
cd ./setup.sh
source setup.sh
```
Then install using:

```
pypy -mpip install fliscopt
```
# Testing
After adding any new algorithm, you can run the tests to check if the code is working properly.
```
./run_tests.sh
```

# Results

## Experimental Results
Results were compared by using the same seeds. The following table shows the results of the experiments.
(Will be shortly added)

## Accessing results
After running the experiments, the results are stored in the results directory. The results are stored in the following format in subdirectories:
```
.
├── multi_proc
│   ├── ackley_N2
│   │   ├── genetic_algorithm_results.csv
│   │   ├── genetic_algorithm_reversed_results.csv
│   │   ├── genetic_algorithm_with_reversals_results.csv
│   │   ├── hill_climb_results.csv
│   │   ├── random_search_results.csv
│   │   └── simulated_annealing_results.csv
│   ├── booth/...
|   |
|   |
│   └── zakharov
│       ├── genetic_algorithm_results.csv
│       ├── genetic_algorithm_reversed_results                  
│       ├── genetic_algorithm_with_reversals_results.csv
│       ├── random_search_results.csv
│       └── simulated_annealing_results.csv
├── plots
│   ├── ackley_N2
│   ├── fitness_function
│   │   ├── hill_climb.png
│   │   └── random_search.png
│   ├── flight_scheduling
│   │   ├── simulated_annealing.png
│   │   ├── sol_chaining.png
│   │   └── sol_chaining_a1.png
│   └── griewank
```

# Algorithms available
>>>>>>> c50061e70af1d68e9fba10fd71a98bde042e8608
