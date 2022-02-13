# Fliscopt 
![Stars](https://img.shields.io/github/stars/Agrover112/fliscopt) ![Forks](	https://img.shields.io/github/forks/Agrover112/fliscopt) ![License](https://img.shields.io/github/license/Agrover112/fliscopt)  ![Issues](https://img.shields.io/github/issues/Agrover112/fliscopt) 
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/CharlesAverill/satyrn/graphs/commit-activity)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![PyPI](https://img.shields.io/pypi/v/fliscopt)](https://pypi.org/project/fliscopt/)
![Tweet](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2FAgrover112%2Ffliscopt)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/Agrover112)

![image](./images/fliscopt_graphic.jpg)

FLIght SCheduling OPTimization 🛫 or *fliscopt* is a simple optimization library for flight scheduling and related problems in the discrete domain. The library supports plotting, asynchronous multiprocessing, and unimodal optimization benchmarks.
The following repository contains code for the paper "XYZ". The experiments were performed in **PyPy3.7** and **CPython 3.8.10.**

Following algorithms have been implemented and test as of date:

**Algorithms**:
- Hill Climbing 
- Random Search 
- Simulated Annealing 
- Genetic Algorithm 
- Genetic Algorithm in Reverse Mode
- Genetic  Algorithm with Reversals
- Genetic Algorithm with Random Search as a Reversal/Reverse Process
- Iterated Chaining

Take a look at the [docs](https://gizmotronn.github.io/fliscopt/docs) 
# Getting Started

Install the library using pip:
```bash
pip install fliscopt
```
Or for unreleased versions:
```bash
pip install git+https://github.com/Agrover112/fliscopt/fliscopt@branchname
```
Or for development:
```bash
git clone https://github.com/Agrover112/fliscopt.git
cd fliscopt
pip install .
```

Download the flights.txt file from the following [link](https://drive.google.com/file/d/1-wxzUMLloeF1tGYEVHvBG_Dh6jfZ-pzR/view) and add it to a data/ directory within your parent directory.

A sample code demonstrating how to use fliscopt:
```python
from fliscopt.utils.util import print_schedule, read_file,plot_scores
from fliscopt.rs import RandomSearch
from fliscopt.ga import GA, ReverseGA, GAReversals, GARSReversals
from fliscopt.hc import HillClimb
from fliscopt.chaining import IteratedChaining
from fliscopt.fitness import fitness_function,domain,griewank



read_file('flights.txt')
sga=GAReversals(seed_init=False,search=False,n_k=250,number_generations=1000)
soln, cost, scores, nfe, seed = sga.run(domain=domain['domain'], fitness_function=fitness_function,seed=5)
plot_scores(scores, sga.get_base(),fname='flight_scheduling', save_fig=False)


sga2=GARSReversals(seed_init=False,search=False,n_k=250,number_generations=1000)
soln, cost, scores, nfe, seed = sga2.run(domain=domain['domain'], fitness_function=fitness_function,seed=5)
plot_scores(scores, sga2.get_base(),fname='flight_scheduling', save_fig=False)

```
This results in the following two plots:

![](https://github.com/Agrover112/fliscopt/blob/master/examples/image.png)

Checkout out the examples in the [examples](https://github.com/Agrover112/fliscopt/tree/master/examples) directory or run in [Google Collab](https://colab.research.google.com/drive/1C9tPvDvauUPxxkL4ItGYP1Azlg6NUBaW?usp=sharing)

## For PyPy users
The instructions for setup are mentioned in the setup directory. Alternatively, you can set up using this bash script. A requirements file is provided just in case.
The script creates and activates a PyPy Conda environment with all libraries and dependencies.
```bash
cd ./setup.sh
source setup.sh
```
Then install using:

```bash
pypy -mpip install fliscopt
```
# Testing
After adding any new algorithm, you can run the tests to check if the code is working properly.
```bash
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
# References 
Read the following for detailed understanding of our project.

[1] [Alicea B., Grover A., Lim A. ,Parent J, Unified Theory of Switching. Flash Talk to be  presented at: 4th Neuromatch Conference; December 1 - 2, 2021](https://youtu.be/aTqgPbKQUD8)

# Contributing Guidelines
Refer [Contributing.md](./CONTRIBUTING.md) and Project Board for mode details.
This repository follows [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)!
