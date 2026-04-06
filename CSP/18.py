from constraint import *

if __name__ == '__main__':
    solver_input = input()
    problem = None
    if solver_input == 'BacktrackingSolver':
        problem = Problem(BacktrackingSolver())
    if solver_input == 'RecursiveBacktrackingSolver':
        problem = Problem(RecursiveBacktrackingSolver())
    if solver_input == 'MinConflictsSolver':
        problem = Problem(MinConflictsSolver())
    variables = list(range(81))
    domain = list(range(1, 10))
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranicuvanjata

    for row in range(9):
        local_vars = [row * 9 + col for col in range(9)]
        problem.addConstraint(AllDifferentConstraint(), local_vars)
    
    for col in range(9):
        local_vars = [row * 9 + col for row in range(9)]
        problem.addConstraint(AllDifferentConstraint(), local_vars)

    for box_row in range(3):
        for box_col in range(3):
            local_vars = []
            for r in range(3):
                for c in range(3):
                    local_vars.append((box_row*3 + r) * 9 + (box_col*3 + c))
            problem.addConstraint(AllDifferentConstraint(), local_vars)

    print(problem.getSolution())