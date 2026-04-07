"""
Main Entry Point - Statistical Analysis & Monte Carlo Simulation
"""

import json
import os
from src.stat_engine import StatEngine
from src.monte_carlo import ServerCrashSimulation

def load_salary_data():
    """Load salary data from JSON file"""
    file_path = os.path.join("data", "sample_salaries.json")
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['salaries']

def analyze_salaries():
    """Perform statistical analysis on salary data"""
    print("\n" + "=" * 70)
    print("STARTUP SALARIES STATISTICAL ANALYSIS")
    print("=" * 70)
    
    salaries = load_salary_data()
    print(f"\nTotal Employees: {len(salaries)}")
    print(f"Salary Range: ${min(salaries):,} - ${max(salaries):,}")
    
    engine = StatEngine(salaries)
    
    print("\n--- CENTRAL TENDENCY ---")
    print(f"Mean Salary: ${engine.get_mean():,.2f}")
    print(f"Median Salary: ${engine.get_median():,.2f}")
    
    mode_result = engine.get_mode()
    if isinstance(mode_result, list):
        print(f"Mode Salary(s): ${', $'.join([str(int(m)) for m in mode_result])}")
    else:
        print(f"Mode: {mode_result}")
    
    print("\n--- DISPERSION ---")
    print(f"Sample Variance: {engine.get_variance(is_sample=True):,.2f}")
    print(f"Population Variance: {engine.get_variance(is_sample=False):,.2f}")
    print(f"Sample Std Deviation: ${engine.get_standard_deviation(is_sample=True):,.2f}")
    
    print("\n--- OUTLIER DETECTION (2 Std Dev) ---")
    outliers = engine.get_outliers(threshold=2)
    print(f"Number of Outliers: {len(outliers)}")
    if outliers:
        print(f"Outlier Values: ${', $'.join([str(int(o)) for o in outliers[:5]])}")
        if len(outliers) > 5:
            print(f"... and {len(outliers) - 5} more")
    
    print("\n" + "=" * 70)
    print("KEY INSIGHT")
    print("=" * 70)
    print(f"⚠️ Mean (${engine.get_mean():,.0f}) vs Median (${engine.get_median():,.0f})")
    print("   Median represents 'typical' salary better when outliers exist")

def run_monte_carlo():
    """Run Monte Carlo simulation for server crashes"""
    simulation = ServerCrashSimulation(theoretical_probability=0.045)
    day_counts = [30, 365, 1000, 10000]
    results = simulation.run_multiple_simulations(day_counts)
    simulation.print_results(results)
    
    print("\n" + "=" * 70)
    print("LAW OF LARGE NUMBERS EXPLANATION")
    print("=" * 70)
    print("Small sample (30 days): High error, unreliable for budgeting")
    print("Large sample (10,000 days): Converges to true 4.5% probability")
    print("Theoretical probability ≠ small sample observation!")

def main():
    """Main entry point"""
    print("\n" + "=" * 70)
    print("STATISTICAL ENGINEERING & SIMULATION ASSESSMENT")
    print("=" * 70)
    
    analyze_salaries()
    run_monte_carlo()
    
    print("\n✅ ANALYSIS COMPLETE")

if __name__ == "__main__":
    main()