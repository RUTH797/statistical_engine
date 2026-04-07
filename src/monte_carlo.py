"""
Monte Carlo Simulation for Server Crash Probability
Demonstrates Law of Large Numbers (LLN)
"""

import random
from typing import Dict, List

class ServerCrashSimulation:
    """
    Simulates server crashes with a fixed theoretical probability.
    Demonstrates how sample size affects accuracy.
    """
    
    def __init__(self, theoretical_probability: float = 0.045):
        """
        Initialize with theoretical crash probability.
        
        Args:
            theoretical_probability: True probability (default 4.5%)
        """
        self.theoretical_probability = theoretical_probability
    
    def simulate_day(self) -> bool:
        """
        Simulate a single day.
        
        Returns:
            True if crash occurred, False otherwise
        """
        return random.random() < self.theoretical_probability
    
    def simulate_crashes(self, days: int) -> Dict:
        """
        Simulate crashes for given number of days.
        
        Args:
            days: Number of days to simulate
            
        Returns:
            Dictionary with simulation results
        """
        crashes = 0
        
        for _ in range(days):
            if self.simulate_day():
                crashes += 1
        
        simulated_probability = crashes / days
        
        return {
            "days": days,
            "crashes": crashes,
            "simulated_probability": simulated_probability,
            "theoretical_probability": self.theoretical_probability,
            "error_percentage": abs(simulated_probability - self.theoretical_probability) / self.theoretical_probability * 100
        }
    
    def run_multiple_simulations(self, day_counts: List[int]) -> List[Dict]:
        """
        Run simulations for multiple time periods.
        
        Args:
            day_counts: List of day counts to simulate
            
        Returns:
            List of simulation results
        """
        results = []
        
        for days in day_counts:
            result = self.simulate_crashes(days)
            results.append(result)
        
        return results
    
    def print_results(self, results: List[Dict]) -> None:
        """
        Print formatted simulation results.
        
        Args:
            results: List of simulation results
        """
        print("\n" + "=" * 70)
        print("MONTE CARLO SIMULATION: SERVER CRASH PROBABILITY")
        print("=" * 70)
        print(f"Theoretical Probability: {self.theoretical_probability * 100}%\n")
        
        for result in results:
            print(f"Days Simulated: {result['days']:,}")
            print(f"  Total Crashes: {result['crashes']}")
            print(f"  Simulated Probability: {result['simulated_probability'] * 100:.4f}%")
            print(f"  Error from Theory: {result['error_percentage']:.2f}%")
            print("-" * 40)
        
        print("\n" + "=" * 70)
        print("LAW OF LARGE NUMBERS DEMONSTRATION")
        print("=" * 70)
        print("As the number of days increases, the simulated probability")
        print("gets closer to the theoretical 4.5% probability.")