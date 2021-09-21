#!/bin/sh

function dots(){
    for i in {1..5};
    do
        echo -n "."
        sleep 0.1
    done
    echo ""
}
echo -n "Checking Conda installation";dots;
function check_conda_install()
{
    if $(which conda)> /dev/null;
    then
        echo -n "Conda found. Skipping installation.";dots;

    else

        echo "Conda not found. Installing.."
        echo "Updating and Upgrading Linux packages...."
        sudo apt update --yes
        sudo apt upgrade --yes
        #Get Miniconda and make it the main Python interpreter
        #Modified from Source: https://gist.github.com/arose13/fcc1d2d5ad67503ba9842ea64f6bac35 :/
        wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
        source ~/miniconda.sh -b -p ~/miniconda 
        rm ~/miniconda.sh

        export PATH=~/miniconda/bin:$PATH
        echo -n "Conda installed and PATH updated.";dots #Github Copilot wrote this line
    fi
}
check_conda_install
sleep 0.4
echo -n "Setting up conda PyPy environment";dots;
source ~/miniconda3/etc/profile.d/conda.sh
echo -n "Creating the environment";dots;
conda env create -f config.yml
sleep 0.5
echo -n "Setup done";dots;
echo -n "Activating environment";dots;
sleep 0.5
conda activate config 
echo "Done :D"


