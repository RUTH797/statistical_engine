import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):
    
    def test_mean_calculation(self):
        engine = StatEngine([1, 2, 3, 4, 5, 6])
        self.assertEqual(engine.get_mean(), 3.5)
    
    def test_median_odd(self):
        engine = StatEngine([1, 2, 3, 4, 5])
        self.assertEqual(engine.get_median(), 3)
    
    def test_median_even(self):
        engine = StatEngine([1, 2, 3, 4, 5, 6])
        self.assertEqual(engine.get_median(), 3.5)
    
    def test_empty_data(self):
        with self.assertRaises(ValueError):
            StatEngine([])
    
    def test_data_cleaning(self):
        engine = StatEngine([1, "2", 3.5, None])
        self.assertEqual(engine.data, [1.0, 2.0, 3.5])

if __name__ == "__main__":
    unittest.main()