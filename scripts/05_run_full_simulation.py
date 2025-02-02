import os

os.system("python scripts/01_initialize_population.py")
for _ in range(10):  # 10 generations
    os.system("python scripts/02_run_tournament.py")
    os.system("python scripts/03_evolve_population.py")
os.system("python scripts/04_visualize_results.py")