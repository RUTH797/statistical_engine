"""
Core Statistical Engine
Implements statistical calculations from scratch without numpy/pandas
"""

import math
from typing import List, Union, Tuple, Any

class StatEngine:
    """
    Statistical engine that processes 1D numerical data.
    Calculates mean, median, mode, variance, std deviation, and outliers.
    """
    
    def __init__(self, data: List[Any]):
        """
        Initialize with data and clean it.
        
        Args:
            data: List of numerical values (may contain None, strings, etc.)
        
        Raises:
            TypeError: If data contains non-numeric values after cleaning
            ValueError: If data is empty
        """
        # Clean and validate data
        self.raw_data = data
        self.data = self._clean_data(data)
        
        if not self.data:
            raise ValueError("Data cannot be empty after cleaning")
    
    def _clean_data(self, data: List[Any]) -> List[float]:
        """
        Clean data by converting numeric strings and removing None.
        
        Args:
            data: Raw input list
            
        Returns:
            List of floats (numeric values only)
            
        Raises:
            TypeError: If value cannot be converted to number
        """
        cleaned = []
        
        for value in data:
            # Skip None values
            if value is None:
                continue
            
            # Convert numeric strings to numbers
            if isinstance(value, str):
                try:
                    value = float(value)
                except ValueError:
                    raise TypeError(f"Cannot convert '{value}' to number")
            
            # Check if it's a number (int or float)
            if isinstance(value, (int, float)):
                cleaned.append(float(value))
            else:
                raise TypeError(f"Unsupported data type: {type(value)}")
        
        return cleaned
    
    def get_mean(self) -> float:
        """
        Calculate arithmetic mean.
        
        Returns:
            float: Average of all values
            
        Formula: mean = (sum of all values) / (number of values)
        """
        return sum(self.data) / len(self.data)
    
    def get_median(self) -> float:
        """
        Calculate median (middle value).
        
        Returns:
            float: Median value
            
        For odd count: middle element
        For even count: average of two middle elements
        """
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        
        if n % 2 == 1:
            # Odd number of elements
            return sorted_data[mid]
        else:
            # Even number of elements
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    
    def get_mode(self) -> Union[List[float], str]:
        """
        Calculate mode (most frequent value(s)).
        
        Returns:
            List of modes if multiple, or message if all values unique
            
        Handles multimodal distributions seamlessly.
        """
        from collections import Counter
        
        # Count frequencies
        freq_counter = Counter(self.data)
        
        # Find maximum frequency
        max_freq = max(freq_counter.values())
        
        # If all values appear once
        if max_freq == 1:
            return "All values are unique (no mode)"
        
        # Get all values with max frequency
        modes = [value for value, freq in freq_counter.items() if freq == max_freq]
        
        return modes if len(modes) > 1 else modes[0]
    
    def get_variance(self, is_sample: bool = True) -> float:
        """
        Calculate variance.
        
        Args:
            is_sample: True for sample variance (Bessel's correction)
                      False for population variance
        
        Returns:
            float: Variance value
            
        Formulas:
            Population: σ² = Σ(x - μ)² / N
            Sample: s² = Σ(x - x̄)² / (n - 1)
        """
        mean = self.get_mean()
        n = len(self.data)
        
        # Sum of squared differences
        squared_diff_sum = sum((x - mean) ** 2 for x in self.data)
        
        if is_sample:
            # Sample variance with Bessel's correction
            return squared_diff_sum / (n - 1)
        else:
            # Population variance
            return squared_diff_sum / n
    
    def get_standard_deviation(self, is_sample: bool = True) -> float:
        """
        Calculate standard deviation.
        
        Args:
            is_sample: True for sample standard deviation
                      False for population standard deviation
        
        Returns:
            float: Standard deviation (square root of variance)
        """
        variance = self.get_variance(is_sample)
        return math.sqrt(variance)
    
    def get_outliers(self, threshold: float = 2) -> List[float]:
        """
        Detect outliers using standard deviation method.
        
        Args:
            threshold: Number of standard deviations from mean
        
        Returns:
            List of values outside mean ± (threshold * std_dev)
        """
        mean = self.get_mean()
        std_dev = self.get_standard_deviation(is_sample=True)
        
        lower_bound = mean - (threshold * std_dev)
        upper_bound = mean + (threshold * std_dev)
        
        outliers = [x for x in self.data if x < lower_bound or x > upper_bound]
        
        return outliers