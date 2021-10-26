try:
    import fliscopt
except:
    import sys
    sys.path.append("..")
import unittest
from fliscopt.fitness import ackley_N2, booth, brown, fitness_function, griewank, matyas, rosenbrock, schaffer_N1, schwefel, sphere, three_hump_camel, zakharov,fitness_function
from fliscopt.utils.util import read_file
class TestFitness(unittest.TestCase):

    def test_fitness(self):
        self.assertEqual(fitness_function(
        [1, 4, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3], "FCO"), 5451, msg="The evaluated cost not matching the total cost associated :{} . Refer fitness_function of total_price + total_wait and expected output of type Int ".format(5451))
        self.assertEqual(fitness_function(
        [1, 3, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3], "FCO"), 5304, msg="The evaluated cost not matching the total cost associated :{} . Refer fitness_function of total_price + total_wait and expected output of type Int ".format(5304))
        

    def test_ackley_N2(self):
        self.assertEqual(ackley_N2([0, 0]), -200, msg="The Ackley function f(0,0) not matching the value:{}".format(-200))
    
    def test_matyas(self):
        self.assertEqual(matyas([0, 0]),0, msg="The Matyas function f(0,0) not matching the value:{}".format(0))

    def test_booth(self):
        self.assertEqual(booth([1, 3]), 0, msg="The Booth function f(1,3) not matching the value:{}".format(0))
    
    def test_griewank(self):
        self.assertEqual(griewank([0, 0, 0]), 0, msg="The Griewank function f(0,0) not matching the value:{}".format(0))

    def test_sphere(self):
        self.assertEqual(sphere([0, 0, 0]), 0, msg="The Sphere function f(0,0,0) not matching the value:{}".format(0))
    
    def test_three_hump_camel(self):
        self.assertEqual(three_hump_camel([0, 0]), 0, msg="The Three_hump_camel function f(0,0) not matching the value:{}".format(0))

    def test_schaffer_N1(self):
        self.assertEqual(schaffer_N1([0, 0]), 0, msg="The Schaffer_N1 function f(0,0) not matching the value:{}".format(0))
    
    def test_schwefel(self):
        self.assertEqual(schaffer_N1([0, 0]),0, msg="The Schwefel function f(0,0) not matching the value:{}".format(0))

    def test_brown(self):
        self.assertEqual(brown([0, 0, 0]), 0, msg="The Brown function f(0,0) not matching the value:{}".format(0))

    def test_rosenbrock(self):
        self.assertEqual(rosenbrock([1, 1, 1]), 0, msg="The Rosenbrock function f(1,1,1) not matching the value:{}".format(0))

    def test_zakharov(self):
        self.assertEqual(zakharov([0, 0, 0]), 0, msg="The Zakharov function f(0,0,0) not matching the value:{}".format(0))




if __name__ == '__main__':
    read_file('flights.txt')
    unittest.main()