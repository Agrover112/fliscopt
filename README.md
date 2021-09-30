# Fliscopt 


FLight SCheduling OPTimization or *fliscopt* is an simple optimization library for flight scheduling and related problems in the discrete domain.The library supports plotting,asynchronous multiprocessing and unimodal optimization benchmarks.
The following repository contains code for the paper "XYZ" . The experiments were performed in **PyPy3.7** and **CPython 3.8.10.**

Following algorithms have been implemented and test as of date:

**Algorithms**:
- Hill Climbing
- Random Search
- Simulated Annealing
- Genetic Algorithm
- Genetic Algorithm in Reverse Mode
- Genetic  Algorithm with Reversals
- Iterated Chaining

 


# Getting Started

Install the library using pip:
```
pip install fliscopt
```
Or for development:
```
git clone https://github.com/Agrover112/fliscopt.git
cd fliscopt
pip install .
```

Download the flights.txt file from the following [link](https://drive.google.com/file/d/1-wxzUMLloeF1tGYEVHvBG_Dh6jfZ-pzR/view) and add it to a data/ directory within your parent directory.

Checkout out the examples in the examples/ directory.

## For PyPy users
The instructions for setup are mentioned in setup directory. Alternatively, you can setup using this bash script. A requirements file is provided just in case.
The script creates and activates an PyPy conda  environment with all libraries and dependencies.
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
Results were compared by using the same seeds. The following table shows the results for the experiments.
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
│   ├── booth/....
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





# Contributing Guidelines
Refer [Contributing.md](./CONTRIBUTING.md) and Project Board for mode details.
# References
[1] []
[2] []    
