#!/bin/sh
echo "Setting up conda PyPy environment...."
source ~/miniconda3/etc/profile.d/conda.sh
echo "Creating the environment.."
conda env create -f config.yml
sleep 0.5
echo "Setup done..."
echo "Activating environment....."
sleep 0.5
conda activate config 
echo "Done :D"

