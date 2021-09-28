import setuptools
from setuptools import setup,find_packages
import os

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='flopt:Flight scheduling OPtimization algorithms',
   version='0.1.0',
   description='Flight scheduling optimization using Genetic Algorithm variants and other algorithms. ',
   license="MIT",
   long_description=long_description,
   long_description_content_type='text/markdown',
   author='Ankit Grover, Jones Granatyr',
   author_email='agrover112@gmail.com',
    packages=find_packages(),
    platforms=['linux','macos','unix'],

   install_requires=[
       'matplotlib','rich'
   ],

   python_requires='>=3.8')