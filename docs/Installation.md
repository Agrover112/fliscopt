---
description: >
    Dedicated information about installing Fliscopt package to your project
hide_description: false
---

Install the library using pip:
```
pip install fliscopt
```
Or for unreleased versions:
```
pip install 'git+https://github.com/Agrover112/fliscopt/fliscopt@branchname
```
Or for development:
```
git clone https://github.com/Agrover112/fliscopt.git
cd fliscopt
pip install .
```

Download the flights.txt file from the following [link](https://drive.google.com/file/d/1-wxzUMLloeF1tGYEVHvBG_Dh6jfZ-pzR/view) and add it to a data/ directory within your parent directory.

Checkout out the examples in the [examples](https://github.com/Agrover112/fliscopt/tree/master/examples) directory or run in [Google Collab](https://colab.research.google.com/drive/1C9tPvDvauUPxxkL4ItGYP1Azlg6NUBaW?usp=sharing)

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
# References 
Read the following for detailed understanding of our project.

[1] [Alicea B., Grover A., Lim A. ,Parent J, Unified Theory of Switching. Flash Talk to be  presented at: 4th Neuromatch Conference; December 1 - 2, 2021](https://youtu.be/aTqgPbKQUD8)

# Contributing Guidelines
Refer [Contributing.md](./CONTRIBUTING.md) and Project Board for mode details.
This repository follows [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)!
