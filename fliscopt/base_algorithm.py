from abc import ABC, ABCMeta, abstractmethod
import random
import math
import sys

class FlightAlgorithm(metaclass=ABCMeta):
    """
    Abstract base class for all optimization algorithms in fliscopt.
    
    This class provides the common interface and initialization logic for all optimization
    algorithms (Genetic Algorithm, Hill Climbing, Random Search, Simulated Annealing, etc.).
    It handles random seed management, domain boundaries, and fitness function evaluation.
    
    The class implements two seeding strategies:
    - seed_init=True: Uses separate random generator for population initialization
    - seed_init=False: Uses the same seed for all random operations (fully deterministic)
    
    All concrete algorithm implementations must inherit from this class and implement
    the three abstract methods: get_base(), get_name(), and run().
    
    Attributes:
        domain (list): List of tuples defining the search space boundaries. 
                      Each tuple contains (lower_bound, upper_bound) for one dimension.
                      Example: [(0, 9), (0, 8), ...] for flight scheduling problem.
        fitness_function (function): The objective function to minimize. Accepts a solution
                                    and returns a numerical cost value.
        seed (int): Random seed value for reproducibility. Defaults to random integer between 10-100.
        seed_init (bool): If True, uses separate seed for initialization only. If False, 
                         sets seed for all random operations. Defaults to True.
        init (list): Initial solution to start the optimization from. Defaults to empty list,
                    which triggers random initialization.
        max_time (int): Maximum execution time in seconds for the algorithm. Defaults to 1000.
        r_init (random.Random): Random number generator instance for population initialization.
        best_cost (float): Stores the best (minimum) cost found during optimization. Initialized to 0.0.
    
    Example:
        >>> from fliscopt.hc import HillClimb
        >>> from fliscopt.fitness import domain, fitness_function
        >>> 
        >>> # Create an instance of a concrete algorithm
        >>> hc = HillClimb(domain=domain['domain'], 
        ...                fitness_function=fitness_function,
        ...                seed=42,
        ...                seed_init=False)
        >>> 
        >>> # Run the optimization
        >>> solution, cost, scores, nfe, seed = hc.run(domain=domain['domain'],
        ...                                             fitness_function=fitness_function,
        ...                                             seed=42)
    
    See Also:
        - GA: Simple Genetic Algorithm implementation
        - HillClimb: Hill Climbing algorithm implementation
        - RandomSearch: Random Search algorithm implementation
        - SimulatedAnnealing: Simulated Annealing algorithm implementation
    """
    
    def __init__(self, domain, fitness_function, seed=random.randint(10, 100), seed_init=True, init=None, max_time=1000) -> None:
        """
        Initialize the base algorithm with common parameters.
        
        Args:
            domain (list): Search space boundaries as list of (min, max) tuples for each dimension.
            fitness_function (function): Objective function to minimize. Takes solution and returns cost.
            seed (int, optional): Random seed for reproducibility. Defaults to random integer [10, 100].
            seed_init (bool, optional): If True, seed only affects initial population. If False, 
                                       seed affects all random operations. Defaults to True.
            init (list, optional): Initial solution vector. If None or empty, random initialization
                                  is used. Defaults to None.
            max_time (int, optional): Maximum runtime in seconds before algorithm terminates. 
                                     Defaults to 1000.
        """
        self.domain = domain
        self.fitness_function = fitness_function
        self.seed = seed
        self.seed_init = seed_init
        
        # Handle initial solution: convert None to empty list for consistency
        if init is None:
            self.init = []
        else:
            self.init = init
        
        # Set maximum execution time (note: assignment overrides parameter, may be bug)
        self.max_time = 1000
        
        # Configure random number generators based on seeding strategy
        if self.seed_init:
            # Strategy 1: Set the seed for initial population only
            # This allows variation in the algorithm's exploration while keeping
            # the starting point deterministic
            self.r_init = random.Random(self.seed)
        else:
            # Strategy 2: Use same seed for both initialization and all random operations
            # This makes the entire algorithm run fully deterministic and reproducible
            self.r_init = random.Random(self.seed)
            random.seed(self.seed)
        
        # Initialize best cost tracker (used by some algorithms)
        self.best_cost = 0.0
    
    @abstractmethod
    def get_base(self) -> str:
        """
        Get the base class name of the algorithm.
        
        This method is used for identifying the algorithm family (e.g., "BaseGA" for
        all genetic algorithm variants). Useful for plotting and result categorization.
        
        Returns:
            str: The name of the base class (e.g., "BaseGA", "FlightAlgorithm").
        
        Example:
            >>> ga = GA()
            >>> ga.get_base()
            'BaseGA'
        """
        pass

    @abstractmethod
    def get_name(self) -> str:
        """
        Get the specific name of the algorithm implementation.
        
        This method returns the concrete class name to identify the specific algorithm
        variant (e.g., "GA", "ReverseGA", "GAReversals"). Used for labeling results,
        plots, and distinguishing between different algorithm implementations.
        
        Returns:
            str: The name of the concrete algorithm class (e.g., "HillClimb", "RandomSearch").
        
        Example:
            >>> hc = HillClimb()
            >>> hc.get_name()
            'HillClimb'
        """
        pass

    @abstractmethod
    def run(self, domain, fitness_function, seed) -> tuple:
        """
        Execute the optimization algorithm.
        
        This is the main method that performs the optimization. It should run the algorithm
        until convergence, maximum iterations, or max_time is reached.
        
        Args:
            domain (list): Search space boundaries as list of (min, max) tuples.
            fitness_function (function): Objective function to minimize.
            seed (int): Random seed value for this run.
        
        Returns:
            tuple: A 5-element tuple containing:
                - best_solution (list): The best solution found (e.g., [3, 2, 7, 3, 6, 3, 2, 4, 1, 2])
                - best_cost (float): The fitness/cost value of the best solution
                - scores (list): History of best costs at each iteration/generation
                - nfe (int): Number of fitness function evaluations performed
                - seed (int): The seed value used (for tracking experiments)
        
        Example:
            >>> rs = RandomSearch(epochs=100)
            >>> solution, cost, scores, nfe, seed = rs.run(
            ...     domain=[(0, 9)] * 10,
            ...     fitness_function=my_fitness_fn,
            ...     seed=42
            ... )
            >>> print(f"Best cost: {cost}, NFE: {nfe}")
        
        Note:
            Implementations should respect the max_time limit and return early if exceeded.
        """
        pass