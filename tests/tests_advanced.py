from context import sample

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced tests."""

    def test_no_thoughts(self):
        self.assertIsNone(sample.hmm(False))
    
    def test_yes_thoughts(self):
        self.assertEqual(sample.hmm(True), 'hmm...')

    def test_pretty_3_plus_5_is_8(self):
        self.assertEqual(sample.pretty_sum(3,5),'3 + 5 = 8')

    def test_pretty_minus3_plus_5_is_2(self):
        self.assertEqual(sample.pretty_sum(-3,5),'-3 + 5 = 2')
    
    def test_pretty_3_times_5_is_15(self):
        self.assertEqual(sample.pretty_multiply(3,5),'3 X 5 = 15')
    
    def test_pretty_3_times_minus5_is_minus15(self):
        self.assertEqual(sample.pretty_multiply(3,-5),'3 X -5 = -15')

if __name__ == '__main__':
    unittest.main()