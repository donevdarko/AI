from constraint import *

def notEqualColors(color_1, color_2):
    return color_1 != color_2

if __name__ == "__main__":
    problem = Problem()

    variables = ["WA", "NT", "Q", "NSW", "V", "SA", "T"]
    problem.addVariables(variables, ["R", "G", "B"])

    pairs = [("WA", "NT"), ("WA", "SA"), ("SA", "NT"), ("SA", "NSW"), ("SA", "Q"), ("SA", "V"), ("NT", "Q"), ("Q", "NSW"), ("NSW", "V")]
    for pair in pairs:
        problem.addConstraint(notEqualColors, pair)

    print(problem.getSolution())
    print(problem.getSolutions())