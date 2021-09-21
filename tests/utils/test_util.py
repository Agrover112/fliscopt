try:
    import final
except:
    import sys
    sys.path.append("../../")

import unittest
from final.utils.util import *

class TestUtil(unittest.TestCase):
    def test_read_file(self):
        self.assertEqual(read_file("flights.txt"), "------File Read-----")
        self.assertIsNotNone(flights)

    def test_get_minutes(self):
        self.assertEqual(get_minutes("1:00"), 60)
        self.assertEqual(get_minutes("6:13"), 373)
        self.assertEqual(get_minutes("0:00"), 0)
    

if __name__ == '__main__':
    unittest.main()
    