from constraint import Problem, BacktrackingSolver, AllDifferentConstraint



if __name__ == '__main__':
    K = int(input())
    grid = [list(map(int, input().split())) for _ in range(K)]
    N = max(map(max, grid))  # Number of regions

    problem = Problem(solver=BacktrackingSolver())

    # Dodadete gi promenlivite i domenite tuka.
    # Add the variables and domains here.
    variables = ["star_" + str(i) for i in range(N)]
    domain = tuple(i for i in range(K*K))
    
    problem.addVariables(variables, domain)
    

    # Dodadete gi ogranichuvanjata tuka.
    # Add the constraints here.

    def cross_region(pos1, pos2):
        x1 = pos1%K
        y1 = pos1//K

        x2 = pos2%K
        y2 = pos2//K

        if grid[y1][x1] == grid[y2][x2]:
            return True
        
        if x1 == x2 or y1 == y2:
            return False
        return True
        
    def same_region(pos1, pos2):
        x1 = pos1%K
        y1 = pos1//K

        x2 = pos2%K
        y2 = pos2//K

        if grid[y1][x1] != grid[y2][x2]:
            return True
        
        manhattan = abs(x1 - x2) + abs(y1 - y2)

        return manhattan > 1
    

    for i, var1 in enumerate(variables):
        for var2 in variables[i+1:]:
            problem.addConstraint(cross_region, [var1, var2])
            problem.addConstraint(same_region, [var1, var2])

    def region_cap(vars, region):
        count = 0
        for pos in vars:
            x1 = pos%K
            y1 = pos//K
            if grid[y1][x1] == region:
                count += 1
        return count < 3
    
    for region in range(1, N+1):
        problem.addConstraint(
            lambda *positions, r=region: region_cap(positions, r), variables
        )



    problem.addConstraint(AllDifferentConstraint(), variables)



    result = problem.getSolution()

    # Ispechatete go reshenieto vo baraniot format.
    # Print the solution in the required format.

    resultGrid = grid[::]
    if result is None:
        print("No Solution!")
    else:
        for star, pos in result.items():
            x = pos%K
            y = pos//K
            resultGrid[y][x] = "*"
        for row in resultGrid:
            print(' '.join(map(str, row)))