# statistical-simulation-evolutionary-prisoners-dilemna

# Project Overview

This project simulates the evolution of cooperation and defection strategies using the **Prisoner’s Dilemma** in an **evolutionary game theory** framework. Over multiple generations, strategies compete in a round-robin tournament, and the most successful strategies are more likely to reproduce. The core mathematical principles driving this simulation are **Nash Equilibria, Replicator Dynamics, and Stochastic Evolutionary Stability**.

### Mathematical Model

#### 1. **Payoff Matrix and Game Dynamics**
Each round of the game follows the standard **Prisoner’s Dilemma** payoff matrix:

$$\begin{bmatrix}
(3,3) & (0,5) \\
(5,0) & (1,1)
\end{bmatrix}$$

where:
- **C (Cooperate)** and **D (Defect)** are the two possible actions.
- If both players cooperate, they each get **3** points.
- If one defects while the other cooperates, the defector gets **5** points while the cooperator gets **0**.
- If both defect, they each get **1** point.

Given a strategy set $S = \{s_1, s_2, ..., s_n\}$ and probability distribution over strategies $P = (p_1, p_2, ..., p_n)$, the expected payoff for a strategy $s_i$ is:

$$U(s_i) = \sum_{j} p_j \cdot M(s_i, s_j)$$

where $M(s_i, s_j)$ is the payoff function from the above matrix.

#### 2. **Evolutionary Dynamics: Replicator Equation**
To model the evolution of strategies, we use the **Replicator Equation**:

$$\frac{dx_i}{dt} = x_i (U(s_i) - \bar{U})$$

where:
- $x_i$ is the frequency of strategy $s_i$ in the population.
- $U(s_i)$ is the expected utility of strategy $s_i$.
- $\bar{U}$ is the average utility of all strategies.

A strategy $s^*$ is said to be **Evolutionarily Stable (ESS)** if, when a small fraction of a mutant strategy $s'$ appears, it has a lower fitness than $s^*$, meaning:

$$U(s^*, s') > U(s', s')$$

for all possible mutant strategies $s'$.

#### 3. **Selection and Mutation**
After each tournament, strategies are selected proportionally to their fitness using **fitness-proportionate selection**:

$$P(s_i) = \frac{U(s_i)}{\sum_j U(s_j)}$$

To maintain diversity, a small fraction of new strategies are mutated with probability $\mu$, randomly choosing a new strategy from the set $S$.

---

# Folder Structure

```
project-root/
├── scripts/
│   ├── 01_initialize_population.py  # Creates the initial population of strategies
│   ├── 02_run_tournament.py         # Runs round-robin tournament for all strategies
│   ├── 03_evolve_population.py      # Selects best strategies and generates next generation
│   ├── 04_visualize_results.py      # Generates graphs for strategy success
├── outputs/                         # Stores results (CSV, graphs, logs)
│   ├── tournament_results.csv
│   ├── evolution_summary.json
│   ├── strategy_distribution.png
│   ├── fitness_over_generations.png
├── requirements.txt                 # Python dependencies
├── README.md                         # Project documentation
```

---

# Usage

### 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```sh
pip install -r requirements.txt
```

### 2. Initialize the population:
```sh
python scripts/01_initialize_population.py
```

### 3. Run the tournament:
```sh
python scripts/02_run_tournament.py
```

### 4. Evolve the population:
```sh
python scripts/03_evolve_population.py
```

### 5. Visualize results:
```sh
python scripts/04_visualize_results.py
```

---

# Requirements

The project requires Python 3.x and the following dependencies:

```
numpy
matplotlib
csv
random
```

Install dependencies via:
```sh
pip install -r requirements.txt
```