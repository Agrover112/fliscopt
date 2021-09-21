import setuptools
from setuptools import setup,find_packages
import os

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='final',
   version='0.5',
   description='Flight scheduling and genetic algorithms for optimization',
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