import setuptools
from setuptools import setup,find_packages
import os
from fliscopt import __version__
with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='fliscopt',
   version=__version__,
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

   python_requires='>=3.7.10')