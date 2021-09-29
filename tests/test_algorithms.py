try:
    import fliscopt
except:
    import sys
    sys.path.append("..")

import unittest

from fliscopt.rs import RandomSearch
from fliscopt.sa import SimulatedAnnealing
from fliscopt.ga import GA
from fliscopt.hc import HillClimb
from fliscopt.utils.util import read_file
from fliscopt.fitness import griewank,domain

class TestAlgorithms(unittest.TestCase):
    def test_rs(self):
        rs = RandomSearch(max_time=0.00001)
        res=rs.run(domain=domain['griewank']*5,fitness_function=griewank,seed=5)
        self.assertIsNotNone(res[0])
        self.assertEqual(len(res[0]),5)
        self.assertIsNotNone(res[1])
        self.assertIsNotNone(res[2])
        self.assertIsNotNone(res[3])
        self.assertIsNotNone(res[4])
        del res

    def test_sa(self):
        sa = SimulatedAnnealing(max_time=0.0003,temperature=50000.0,seed_init=False)
        res=sa.run(domain=domain['griewank']*5,fitness_function=griewank,seed=5)
        self.assertIsNotNone(res[0])
        self.assertEqual(len(res[0]),5)
        self.assertIsNotNone(res[1])
        self.assertIsNotNone(res[2])
        self.assertIsNotNone(res[3])
        self.assertIsNotNone(res[4])
        del res

    def test_ga(self):
        ga = GA(seed_init=False,search=False)
        res=ga.run(domain=domain['griewank']*5,fitness_function=griewank,seed=5)
        self.assertIsNotNone(res[0])
        self.assertEqual(len(res[0]),5)
        self.assertIsNotNone(res[1])
        self.assertIsNotNone(res[2])
        self.assertIsNotNone(res[3])
        self.assertIsNotNone(res[4])
        del res

    def test_hc(self):
        hc = HillClimb(seed_init=False,max_time=0.0000001)
        res=hc.run(domain=domain['griewank']*5,fitness_function=griewank,seed=5)
        self.assertIsNotNone(res[0])
        self.assertEqual(len(res[0]),5) 
        self.assertIsNotNone(res[1])      
        self.assertIsNotNone(res[2])    
        self.assertIsNotNone(res[3])
        self.assertIsNotNone(res[4])
        del res

if __name__ == '__main__':
    read_file('flights.txt')
    unittest.main()
