from context import sample

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth(self):
        assert True
    
    def test_3_plus_5(self):
        self.assertEqual(sample.submod.extras.sum(3,5), 8)
    
    def test_3_times_5(self):
        self.assertEqual(sample.submod.extras.multiply(3, 5),15)

if __name__ == '__main__':
    unittest.main()