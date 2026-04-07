# Statistical Engineering & Simulation Assessment

## Project Overview
This project implements a complete pure-Python statistical engine from scratch (no NumPy/pandas) that demonstrates the Law of Large Numbers through Monte Carlo simulation. The statistical engine processes raw 1D numerical data and calculates mean, median, mode (including multimodal handling), variance (both population and sample with Bessel's correction), standard deviation, and outlier detection. The Monte Carlo simulation models a server with a 4.5% daily crash probability and shows how larger sample sizes converge to theoretical probability.

## Author
Ruth

---

## Mathematical Logic Implemented

### 1. Mean (Arithmetic Average)
**Formula:** μ = Σx / n

**Example:** [1, 2, 3, 4, 5] → 15/5 = 3.0

### 2. Median (Middle Value)
**Logic:**
- If n is odd: Middle element after sorting
- If n is even: Average of two middle elements

**Examples:**
- Odd: [1, 2, 3, 4, 5] → 3
- Even: [1, 2, 3, 4, 5, 6] → (3+4)/2 = 3.5

### 3. Mode (Most Frequent Value)
**Logic:**
- Count frequency of each value
- Find maximum frequency
- Return all values with max frequency (multimodal support)
- If all values appear once: Return message "All values are unique (no mode)"

**Examples:**
- [1, 1, 2, 2, 3] → [1, 2] (multimodal)
- [1, 2, 3, 4, 5] → "All values are unique (no mode)"

### 4. Variance
**Population Variance:** σ² = Σ(x - μ)² / N
- Used when you have ALL data
- Divides by N

**Sample Variance:** s² = Σ(x - x̄)² / (n - 1)
- Used when working with a sample
- Uses Bessel's correction (divides by n-1) for unbiased estimate

### 5. Standard Deviation
**Formula:** σ = √variance
- Square root of variance
- Measures dispersion in original units

### 6. Outlier Detection
**Method:** Standard deviation method
- Lower bound = mean - (threshold × std_dev)
- Upper bound = mean + (threshold × std_dev)
- Default threshold = 2 standard deviations
- Returns values outside bounds

---

## Setup Instructions

### Prerequisites
- Python 3.6 or higher
- No external libraries required (uses only: math, random, json, unittest, collections)

### Clone the Repository
```bash
git clone https://github.com/RUTH797/statistical_engine.git
cd statistical_engine

Run the Main Program
bash
python main.py
Testing
Run Unit Tests
bash
python -m unittest tests.test_stat_engine -v
Tests Included
test_mean_calculation: Verifies mean on even list [1,2,3,4,5,6] = 3.5
test_median_odd	: Verifies median on odd list [1,2,3,4,5] = 3
test_median_even: Verifies median on even list [1,2,3,4,5,6] = 3.5
test_empty_data: Graceful failure - raises ValueError
test_standard_deviation	: Matches known mathematical outcome


Sample Output
Statistical Analysis Output
text
======================================================================
STARTUP SALARIES STATISTICAL ANALYSIS
======================================================================

Total Employees: 50
Salary Range: $30,000 - $20,000,000

--- CENTRAL TENDENCY ---
Mean Salary: $1,291,340.00
Median Salary: $61,000.00
Mode: 42000.0

--- DISPERSION ---
Sample Variance: 14,912,157,249,387.76
Population Variance: 14,613,914,104,400.00
Sample Std Deviation: $3,861,626.24

--- OUTLIER DETECTION (2 Std Dev) ---
Number of Outliers: 3
Outlier Values: $10,000,000, $15,000,000, $20,000,000

======================================================================
KEY INSIGHT
======================================================================
⚠️ Mean ($1,291,340) vs Median ($61,000)
   Median represents 'typical' salary better when outliers exist
Monte Carlo Simulation Output
text
======================================================================
MONTE CARLO SIMULATION: SERVER CRASH PROBABILITY
======================================================================
Theoretical Probability: 4.5%

Days Simulated: 30
  Total Crashes: 3
  Simulated Probability: 10.0000%
  Error from Theory: 122.22%
----------------------------------------
Days Simulated: 365
  Total Crashes: 21
  Simulated Probability: 5.7534%
  Error from Theory: 27.85%
----------------------------------------
Days Simulated: 1,000
  Total Crashes: 41
  Simulated Probability: 4.1000%
  Error from Theory: 8.89%
----------------------------------------
Days Simulated: 10,000
  Total Crashes: 445
  Simulated Probability: 4.4500%
  Error from Theory: 1.11%
----------------------------------------

======================================================================
LAW OF LARGE NUMBERS DEMONSTRATION
======================================================================
As the number of days increases, the simulated probability
gets closer to the theoretical 4.5% probability.

======================================================================
LAW OF LARGE NUMBERS EXPLANATION
======================================================================
Small sample (30 days): High error, unreliable for budgeting
Large sample (10,000 days): Converges to true 4.5% probability
Theoretical probability ≠ small sample observation!
✅ Acceptance Criteria Checklist

##Core Statistical Engine
Passes empty list handling (raises ValueError)

Mixed data type cleaning (converts "3" to 3.0, removes None)

Multimodal mode returns list of all modes

Unique values mode returns descriptive message

Sample variance with Bessel's correction (divides by n-1)

Population variance (divides by N)

Outlier detection with configurable threshold

Even vs Odd median handled correctly

##Unit Testing
Correct mean on odd vs even list

Correct median on odd vs even list

Graceful failure on empty list

Standard deviation matches known outcome

##Monte Carlo & Law of Large Numbers
Simulates 4.5% theoretical probability

Runs for 30, 365, 1000, 10000 days

Error decreases as sample size increases

Demonstrates LLN convergence

##Documentation & Submission
Project Overview included

Mathematical Logic explained

Setup Instructions provided

Testing Instructions included

Acceptance Criteria Checklist present

Public GitHub repository

Proper folder structure (data/, src/, tests/)