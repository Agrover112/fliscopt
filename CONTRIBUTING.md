# CONTRIBUTING GUIDELINES
Please take a moment to review this document in order to make the contribution process easy and effective for everyone involved.

Following these guidelines helps to communicate that you respect the time of the developers managing and developing this open source project. In return, they should reciprocate that respect in addressing your issue or assessing patches and features 
## Some contributing rules you should follow 
 
 - Always use the English language.
 - Make use of [discussion](https://github.com/Agrover112/final/discussions) properly (proper language)
 -  Check if the feature you are adding already exists.
 -  Contribution to new algorithms is always welcome.
 -  While adding algorithms test it properly  and make sure all functionalities including single_run,multiple_run,benchmark are working properly.
 -  Contributing to docs or README is always welcome.
 -  Check for broken or re-located links.
- If this is your first contribution, You might also want to take up issues with the <b>good first</b> issue or the<b> help wanted </b>label.

- Discuss the changes you wish to make by creating an [issue](https://github.com/Agrover112/final/issues) or comment on an [existing issue]https://github.com/Agrover112/final/issues).
-  Description should start with a capital letter and be ended with proper punctuation.
- Once you have been assigned the issue by the maintainer, you can go ahead to fork the repo, clone and make changes to fix the issue. 
- Please follow [**conventional commits**](https://www.conventionalcommits.org/en/v1.0.0-beta.2/)


##  Specific Contribution Guidelines
These guidelines should be followed if you are changing the code base .
- Any suggestion on removing redundancy in CONTRUBUTING.md/README.md is welcome.
- You can always add new algorithms to the repostiory, there is a list of available algorithms online!.
- You could add a modified version of an algorithm such as adaptive version or other variants which you tested out on your own problems or on the flight-scheduling problem.
- Make sure to test the algorithm thoroughly before you add it to the repository.
- This can be done by running the algorithm on the flight-scheduling problem and benchmark functions and checking if it is working properly.
- IF algo is variant of existing algo--> sub-class it from existing one EX: GA with adaptive operators!?
- For other algorithms make a seperate file such as hc for hillclimbing.py and follow the style followed in other files.Well, I think the structure can be considered as an **Abstract Factory Design Pattern??**
- Make sure to write proper tests!
- Make sure to write good comments and use docstrings/etc.
- Update the chaining.py with your new algorithm.
- Finally make sure to update the list of algorithms in the README.md file, and it's performance in the Experimental results section.
- AND....finally update the ```___version___``` in the ```__init__.py``` file.( Refer semantic versioning for more details).
- If all tests work properly and it works on all benchmarks and problems, you can raise a PR!!!
  ### TLDR :(:
  - Algo should work a a single import
  - Algo should work with multiprocessing multiproc.py <Try this first
  - Algo should work with flight-sheduling and all benchmarks functions for wierd behaviours that you can encounter. IF you encounter one try fixing the function/algo and writing a test for it in test_fitness.py or test_algorithms.py
  - Algo should work with chaining test_chaining.py
  - ./test.sh should work
  
  (PS: If you are having trouble writing the algorithm, refer the algorithms.py file,which was the initial version upon which the entire project was built upon.)
## Making your Pull Request

- Good pull requests - patches, improvements, new features - are a fantastic help. They should remain focused in scope and avoid containing unrelated commits. 

- you can create a pull request referencing the number of the issue you fixed. 
 
- Once, you have completed this, your pull request would be reviewed by a maintainer, if it satisfies the requirements of the corresponding issue to which it was made, it would be merged.

Kudos to you :balloon:

---

Thank you for contributing to [awesome-semantic-search](https://github.com/Agrover112/awesome-semantic-search).