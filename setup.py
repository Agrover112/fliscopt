import setuptools
from setuptools import setup
import os

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='flight_algorithms',
   version='0.5',
   description='Flight scheduling algorithms',
   license="MIT",
   long_description=long_description,
   author='agrover112',
   author_email='agrover112@gmail.com',
   packages=['flight_algorithms'],

   install_requires=[
       'matplotlib',
   ],

   python_requires='>=3.8')