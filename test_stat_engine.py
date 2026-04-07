"""
Unit Tests for Statistical Engine
"""

import unittest
import sys
import os

# Add the parent directory to path so we can import src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):
    """Test cases for StatEngine class"""
    
    def setUp(self):
        """Set up test data"""
        self.even_data = [1, 2, 3, 4, 5, 6]
        self.odd_data = [1, 2, 3, 4, 5]
        self.dirty_data = [1, 2, "3", 4.5, None]
    
    def test_mean_calculation(self):
        """Test mean calculation"""
        engine = StatEngine(self.even_data)
        self.assertEqual(engine.get_mean(), 3.5)
        
        engine2 = StatEngine(self.odd_data)
        self.assertEqual(engine2.get_mean(), 3.0)
    
    def test_median_odd_list(self):
        """Test median for odd number of elements"""
        engine = StatEngine(self.odd_data)
        self.assertEqual(engine.get_median(), 3)
    
    def test_median_even_list(self):
        """Test median for even number of elements"""
        engine = StatEngine(self.even_data)
        self.assertEqual(engine.get_median(), 3.5)
    
    def test_mode_unique_values(self):
        """Test mode when all values are unique"""
        engine = StatEngine(self.even_data)
        result = engine.get_mode()
        self.assertEqual(result, "All values are unique (no mode)")
    
    def test_mode_multiple_modes(self):
        """Test mode with multiple modes"""
        data = [1, 1, 2, 2, 3]
        engine = StatEngine(data)
        modes = engine.get_mode()
        self.assertIsInstance(modes, list)
        self.assertIn(1, modes)
        self.assertIn(2, modes)
    
    def test_empty_data_error(self):
        """Test that empty data raises ValueError"""
        with self.assertRaises(ValueError):
            StatEngine([])
    
    def test_data_cleaning(self):
        """Test that data cleaning works"""
        engine = StatEngine(self.dirty_data)
        self.assertEqual(engine.data, [1.0, 2.0, 3.0, 4.5])
    
    def test_invalid_data_type(self):
        """Test that invalid data raises TypeError"""
        with self.assertRaises(TypeError):
            StatEngine([1, 2, "not a number"])
    
    def test_variance_sample_vs_population(self):
        """Test difference between sample and population variance"""
        engine = StatEngine([1, 2, 3, 4, 5])
        sample_var = engine.get_variance(is_sample=True)
        pop_var = engine.get_variance(is_sample=False)
        self.assertGreater(sample_var, pop_var)
    
    def test_outlier_detection(self):
        """Test outlier detection"""
        data = [1, 2, 3, 100, 200, 300]
        engine = StatEngine(data)
        outliers = engine.get_outliers(threshold=2)
        self.assertIn(300.0, outliers)

if __name__ == "__main__":
    unittest.main()