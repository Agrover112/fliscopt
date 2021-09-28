try:
    import flopt
except:
    import sys
    sys.path.append("..")
import unittest
from flopt.fitness import ackley_N2, booth, brown, fitness_function, griewank, matyas, rosenbrock, schaffer_N1, schwefel, sphere, three_hump_camel, zakharov,fitness_function
from flopt.utils.util import read_file
class TestFitness(unittest.TestCase):

    def test_fitness(self):
        self.assertEqual(fitness_function(
        [1, 4, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3], "FCO"), 5451)
        self.assertEqual(fitness_function(
        [1, 3, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3], "FCO"), 5304)
        

    def test_ackley_N2(self):
        self.assertEqual(ackley_N2([0, 0]), -200)
    
    def test_matyas(self):
        self.assertEqual(matyas([0, 0]),0)

    def test_booth(self):
        self.assertEqual(booth([1, 3]), 0)
    
    def test_griewank(self):
        self.assertEqual(griewank([0, 0, 0]), 0)

    def test_sphere(self):
        self.assertEqual(sphere([0, 0, 0]), 0)
    
    def test_three_hump_camel(self):
        self.assertEqual(three_hump_camel([0, 0]), 0)

    def test_schaffer_N1(self):
        self.assertEqual(schaffer_N1([0, 0]), 0)
    
    def test_schwefel(self):
        self.assertEqual(schaffer_N1([0, 0]),0)

    def test_brown(self):
        self.assertEqual(brown([0, 0, 0]), 0)

    def test_rosenbrock(self):
        self.assertEqual(rosenbrock([1, 1, 1]), 0)

    def test_zakharov(self):
        self.assertEqual(zakharov([0, 0, 0]), 0)




if __name__ == '__main__':
    read_file('flights.txt')
    unittest.main()