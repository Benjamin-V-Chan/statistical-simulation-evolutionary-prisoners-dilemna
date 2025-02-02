import csv
import matplotlib.pyplot as plt

def plot_strategy_distribution():
    with open("outputs/population.csv", "r") as file:
        strategies = [row["strategy"] for row in csv.DictReader(file)]

    counts = {s: strategies.count(s) for s in set(strategies)}

    plt.bar(counts.keys(), counts.values())
    plt.xlabel("Strategy")
    plt.ylabel("Frequency")
    plt.title("Strategy Distribution in Population")
    plt.savefig("outputs/strategy_distribution.png")

if __name__ == "__main__":
    plot_strategy_distribution()