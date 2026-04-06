from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))
    
    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(AllDifferentConstraint(), variables)

    problem.addConstraint(lambda s: s != 0, ["S"])
    problem.addConstraint(lambda m: m != 0, ["M"])

    def send_more_money(s, e, n, d, m, o, r, y):
        send = 1000*s + 100*e + 10*n + d
        more = 1000*m + 100*o + 10*r + e
        money = 10000*m + 1000*o + 100*n + 10*e + y
        return send + more == money
    
    problem.addConstraint(send_more_money, variables)





    # problem.addConstraint(ExactSumConstraint(variables['Y']), [variables['D'], variables['E']])
    # problem.addConstraint(ExactSumConstraint(variables['E']), [variables['N'], variables['R']])
    # problem.addConstraint(ExactSumConstraint(variables['N']), [variables['E'], variables['O']])
    # problem.addConstraint(ExactSumConstraint(variables['O']), [variables['S'], variables['D']])
    # ----------------------------------------------------
    
    print(problem.getSolution())
    