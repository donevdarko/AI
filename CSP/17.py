from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["A", "B", "C", "D", "E", "F"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(100))))
    
    # ---Tuka dodadete gi ogranichuvanjata----------------
    
    problem.addConstraint(AllDifferentConstraint(), variables)

    def odd_bde(b, d, e):
        return b % 2 == 1 and d % 2 == 1 and e % 2 == 1
    problem.addConstraint(odd_bde, [variables[1], variables[3], variables[4]])
    
    def sum_abc(a, b, c):
        return (a+b+c)>=100
    problem.addConstraint(sum_abc, [variables[0], variables[1], variables[2]])
    
    def sum_de(d, e):
        return (d+e)==150
    problem.addConstraint(sum_de, [variables[3], variables[4]])

    def devisible_f(f):
        return (f%10)%4==0
    problem.addConstraint(devisible_f, [variables[5]])

    # ----------------------------------------------------
    
    print(dict(sorted(problem.getSolution().items)))