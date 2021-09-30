try:
    import fliscopt
except:
    import sys
    sys.path.append("..")
import unittest

from fliscopt.utils.util import read_file
from fliscopt.chaining import IteratedChaining


class TestChaining(unittest.TestCase):
    def test_iter_1(self): # An bug in eariler version caused this test to fail
        self.assertIsNotNone(IteratedChaining(rounds=1, n_obs=2, tol=90).run('RandomSearch', 'HillClimb'))
    
    def test_iter_odd(self):
        self.assertIsNotNone(IteratedChaining(rounds=3, n_obs=2, tol=90).run('RandomSearch', 'HillClimb'))

    def test_iter_even(self):
        self.assertIsNotNone(IteratedChaining(rounds=4, n_obs=2, tol=90).run('RandomSearch', 'HillClimb'))
if __name__ == '__main__':
    read_file('flights.txt')
    unittest.main()
