import random
import csv

STRATEGIES = ["Always Cooperate", "Always Defect", "Tit-for-Tat", "Random"]
POPULATION_SIZE = 100

def initialize_population():
    population = [
        {"id": i, "strategy": random.choice(STRATEGIES)}
        for i in range(POPULATION_SIZE)
    ]
    
    with open("outputs/population.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "strategy"])
        writer.writeheader()
        writer.writerows(population)

if __name__ == "__main__":
    initialize_population()