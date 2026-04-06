from constraint import *
import math


if __name__ == '__main__':
    problem = Problem()

    variables = ["position" + str(i) for i in range(8)]
    domain = [i+1 for i in range(16)]
    problem.addVariables(variables, domain)
    
    magicSum = 34
    for first in [0, 4, 8, 12]:
        row_vars = [first + move for move in range(4)]
        problem.addConstraint(ExactSumConstraint(magicSum), row_vars)
    for first in [0, 1, 2, 3]:
        col_vars = [first + move for move in range(0, 16, 4)]
        problem.addConstraint(ExactSumConstraint(magicSum), col_vars)

    
    pass