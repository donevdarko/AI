import pygad
#grid size 10x10

N, M, R = map(float, input().split())
N = int(N)
M = int(M)

points = [tuple(map(float, input().split())) for _ in range(N)]

# Part 1.
def decode(solution):
    local_m = len(solution) // 3
    umbrellas = []
    for i in range(local_m):
        x = solution[3*i]
        y = solution[3*i + 1]
        active = solution[3*i + 2]
        if active >= 0.5:
            umbrellas.append((x, y))
    return umbrellas


def fitness_func(ga, solution, idx):
    umbrellas = decode(solution)
    num_active = len(umbrellas)
    cost = 0.0

    for (px, py) in points:
        covered = any(
            (px - ux) ** 2 + (py - uy) ** 2 <= R ** 2
            for (ux, uy) in umbrellas
        )
        if not covered:
            cost += 1_000.0
    
    for i in range(num_active):
        for j in range(i+1, num_active):
            ux1, uy1 = umbrellas[i]
            ux2, uy2 = umbrellas[j]
            d=(ux1 - ux2)**2 + (uy1 - uy2)**2

            if d < (8 * R / 5)**2:
                cost+= 100.0
            elif d < (2 * R)**2:
                cost+= 10.0
    
    cost += 1.0 * num_active

    return -cost


gene_space = (
    [{'low': 0, 'high': 10},
     {'low': 0, 'high': 10},  # {'low': R, 'high': 10 - R}, za cel cador
     {'low': 0, 'high': 1}]
     * M
)


params = {
    'num_generations': 500,
    'sol_per_pop': 100,
    'num_parents_mating': 50,

    'num_genes': 3*M,
    'gene_space': gene_space,

    'fitness_func': fitness_func,

    'mutation_num_genes': 1,
    'save_best_solutions': True
}


ga = pygad.GA(**params)

ga.run()

solution, _, _ = ga.best_solution()
fitness = fitness_func(None, solution, 0)
best_solutions = ga.best_solutions

print(solution)
print(fitness)


# Part 2.
step = max(1, len(best_solutions) // 5)
chromosomes = [best_solutions[i] for i in range(0, len(best_solutions), step)][:5]
submit_data(fitness_func, decode, chromosomes, best_solutions)