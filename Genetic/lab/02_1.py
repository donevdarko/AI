import pygad


N = int(input())
S, E = map(int, input().split())

dist = [list(map(float, input().split())) for _ in range(N)]
cities = [c for c in range(N) if c != S and c != E]
M = len(cities)

def decode(solution):
    order_genes = solution[:M]
    assign_genes = solution[M:]

    friend1=[]
    friend2=[]

    for i, city in enumerate(cities):
        order = order_genes[i]
        assigned = assign_genes[i]
        if assigned == 0:
            friend1.append((order, city))
        else:
            friend2.append((order, city))

    friend1.sort(key=lambda x: x[0])
    friend2.sort(key=lambda x: x[0])

    route1 = [S] + [c for _, c in friend1] + [E]
    route2 = [S] + [c for _, c in friend2] + [E]

    return route1, route2

def route_time(route):
    total = 0.0
    for i in range(len(route) - 1):
        total += dist[route[i]][route[i+1]]
    return total


def fitness_func(ga, solution, idx):
    route1, route2 = decode(solution)

    t1 = route_time(route1)
    t2 = route_time(route2)

    max_time = max(t1, t2)
    min_time = min(t1, t2)

    penalty = 0.0

    if min_time > 0 and max_time > 2*min_time:
        penalty += (max_time - 2 * min_time) * 5.0
    elif min_time == 00 and max_time > 0 and M > 1:
        penalty += max_time * 50.0

    n1 = len(route1) - 2
    n2 = len(route2) - 2
    imbalance = abs(n1-n2)
    if M>0:
        penalty+=(imbalance/M)*max_time
    return -(max_time + penalty)


gene_space = (
    [cities for _ in range(M)] +
    [[0, 1] for _ in range(M)]
)


params = {
    'num_generations': 500,
    'sol_per_pop': 100,
    'num_parents_mating': 50,

    'num_genes': 2*M,
    'gene_space': gene_space,

    'fitness_func': fitness_func,

    'mutation_num_genes': 2,
    'save_best_solutions': True
}


ga = pygad.GA(**params)

ga.run()

solution, _, _ = ga.best_solution()
fitness = fitness_func(None, solution, 0)
best_solutions = ga.best_solutions

route1, route2 = decode(solution)

print("Friend 1 route:", route1)
print("Friend 2 route:", route2)
print("Fitness:", fitness)

#submit_data(fitness_func, decode, best_solutions)
