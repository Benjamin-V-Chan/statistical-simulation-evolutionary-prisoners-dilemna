import csv
import random

def compute_fitness():
    scores = {}
    with open("outputs/tournament_results.csv", "r") as file:
        for row in csv.DictReader(file):
            id1, id2, score1, score2 = int(row["id1"]), int(row["id2"]), int(row["score1"]), int(row["score2"])
            scores[id1] = scores.get(id1, 0) + score1
            scores[id2] = scores.get(id2, 0) + score2

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

def evolve_population():
    ranked = compute_fitness()
    top_half = [x[0] for x in ranked[:len(ranked)//2]]

    with open("outputs/population.csv", "r") as file:
        population = {int(row["id"]): row["strategy"] for row in csv.DictReader(file)}

    new_population = [{"id": i, "strategy": population[random.choice(top_half)]} for i in range(100)]

    with open("outputs/population.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "strategy"])
        writer.writeheader()
        writer.writerows(new_population)

if __name__ == "__main__":
    evolve_population()