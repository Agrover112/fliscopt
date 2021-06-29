# PyPy Setup 
## First update your distribution.
```
sudo apt-get update
sudo apt-get update -y
```
## Create a Conda virtual env
```
conda create -n pypy pypy
conda install -c conda-forge pypy3.7
conda create -n pypy
conda activate pypy
conda install -c conda-forge pypy3.7
```
## Install libraries to PyPy
```
pypy -mpip install matplotlib
/home/$USER/miniconda3/envs/pypy/bin/pypy -m ensurepip 
pypy -mpip install matplotlib
/home/$USER/miniconda3/envs/pypy/bin/pypy -m pip install --upgrade pip
pypy -mpip install matplotlib
```
# Run
```
pypy mp.py 
OR
pypy flightscheduling.py
```
**Note**: Use PATH -m ensurepip only if an error is enocountered or if prompt says so.
 