#!/bin/sh

echo -n "Running tests...."
echo  "\nTesting fitness functions"
pypy test_fitness.py
echo "\nTesting Optimization algorithms......"
pypy test_algorithms.py
echo -n "\nTesting Chaining algorithms......"
pypy test_chaining.py
echo "All tests done!"
echo -n "----------------------------------------------------------------------\n"