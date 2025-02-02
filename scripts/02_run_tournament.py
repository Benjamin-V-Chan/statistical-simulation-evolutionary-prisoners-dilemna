import csv
import random

PAYOFFS = {
    ("C", "C"): (3, 3),  # Mutual Cooperation
    ("C", "D"): (0, 5),  # One defects, the other cooperates
    ("D", "C"): (5, 0),
    ("D", "D"): (1, 1)   # Mutual Defection
}

def strategy_move(strategy, opponent_last_move=None):
    if strategy == "Always Cooperate":
        return "C"
    elif strategy == "Always Defect":
        return "D"
    elif strategy == "Tit-for-Tat":
        return opponent_last_move if opponent_last_move else "C"
    else:  # Random strategy
        return random.choice(["C", "D"])

def play_match(strategy1, strategy2):
    score1, score2 = 0, 0
    last_move1, last_move2 = None, None

    for _ in range(10):  # Each match consists of 10 rounds
        move1 = strategy_move(strategy1, last_move2)
        move2 = strategy_move(strategy2, last_move1)
        s1, s2 = PAYOFFS[(move1, move2)]
        score1 += s1
        score2 += s2
        last_move1, last_move2 = move1, move2

    return score1, score2

def run_tournament():
    with open("outputs/population.csv", "r") as file:
        population = list(csv.DictReader(file))

    results = []

    for i in range(len(population)):
        for j in range(i + 1, len(population)):
            score1, score2 = play_match(population[i]["strategy"], population[j]["strategy"])
            results.append({"id1": population[i]["id"], "id2": population[j]["id"], "score1": score1, "score2": score2})

    with open("outputs/tournament_results.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id1", "id2", "score1", "score2"])
        writer.writeheader()
        writer.writerows(results)

if __name__ == "__main__":
    run_tournament()