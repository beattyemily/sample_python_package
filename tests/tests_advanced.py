from context import sample

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced tests."""

    def test_no_thoughts(self):
        self.assertIsNone(sample.hmm(False))
    
    def test_yes_thoughts(self):
        self.assertEqual(sample.hmm(True), 'hmm...')

if __name__ == '__main__':
    unittest.main()