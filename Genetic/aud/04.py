import pygad
import numpy as np

N = 5
# 2 4 6 5
dist = [
    [0,  2,  9, 10, 7],
    [2,  0,  6,  4, 3],
    [9,  6,  0,  8, 5],
    [10, 4,  8,  0, 6],
    [7,  3,  5,  6, 0]
]

def fitness_func(ga, solution, idx):
    total_distance = 0
    for i in range(N-1):
        start = int(solution[i])
        end = int(solution[i+1])
        total_distance += dist[start][end]
    return -total_distance
    


params = {
    'num_generations': 500,
    'num_parents_mating': 25,
    'sol_per_pop': 50,
    'num_genes': N,

    'fitness_func': fitness_func,

    'gene_space': list(range(N)),
    'allow_duplicate_genes': False,
    'mutation_num_genes': 1
}


ga = pygad.GA(**params)

ga.run()

solution, _, _ = ga.best_solution()
fitness = fitness_func(None, solution, 0)

print(solution)
print(fitness)