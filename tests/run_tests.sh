#!/bin/sh

echo -n "Running tests...."
echo  "\nTesting fitness functions"
python3 test_fitness.py
echo "\nTesting Optimization algorithms......"
#python3 test_algorithms.py
echo -n "\nTesting Chaining algorithms......"
python3 test_chaining.py
echo "All tests done!"
echo -n "----------------------------------------------------------------------\n"