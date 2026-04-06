from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    n = int(input())
    variables = list(range(1, n+1))
    variables = variables[::-1]
    domain = [(i, j) for i in range(n) for j in range(n)]

    problem.addVariables(variables, domain)

    problem.addConstraint(AllDifferentConstraint(), variables)

    def no_attack(q1, q2):
        r1, c1 = q1
        r2, c2 = q2
        return (r1 != r2 and c1 != c2 and abs(r1-r2) != abs(c1-c2))
    
    for i in range(n):
        for j in range(i+1, n):
            problem.addConstraint(no_attack, [variables[i], variables[j]])

    if n<=6:
        solutions = problem.getSolutions()
        print(len(solutions))
    else:
        print(problem.getSolution())