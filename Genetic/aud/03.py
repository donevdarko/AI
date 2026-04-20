import pygad

N = 5
values = [10, 5, 15, 7, 6]
weights = [2, 3, 5, 7, 1]
C = 10


def fitness_func(ga, solution, idx):
    total_value = 0
    total_weight = 0
    for i, sol in enumerate(solution):
        if sol:
            total_value+=values[i]
            total_weight+=weights[i]
    
    overflow = total_weight - C

    if overflow < 0:
        return total_value
    else:
        return total_value - overflow*max(v/w for v, w in zip(values, weights))
        

params = {
    'num_generations': 500,
    'num_parents_mating': 50,
    'sol_per_pop': 100,
    'num_genes': N,

    'fitness_func': fitness_func,

    'gene_space': [0, 1],
    'mutation_num_genes': 1
}


ga = pygad.GA(**params)

ga.run()

solution, _, _ = ga.best_solution()
fitness = fitness_func(None, solution, 0)

print(solution)
print(fitness)