from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    
    # ----------------------------------------------------
    # ---Prochitajte gi informaciite od vlezot
    
    n = int(input())

    trees = tuple([tuple(map(int, input().split(" "))) for _ in range(n)])

    size = 6

    cols = tuple(input().split(" "))
    
    # -----------------------------------------------------
    # ---Izberete promenlivi i domeni so koi bi sakale da rabotite-----

    for tree in trees:
        x, y = tree
        tents = []
        for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx = x + dx
            ny = y + dy
            if 0<=nx<size and 0<=ny<size and (nx, ny) not in trees:
                tents.append((nx, ny))
        problem.addVariable(tree, tents)
    
    # -----------------------------------------------------
    # ---Potoa dodadete ogranichuvanjata-------------------
    
    def not_together(val1, val2):
        x1, y1 = val1
        x2, y2 = val2
        if abs(x1 - x2) + abs(y1 - y2) == 1:
            return False
        if x1 == x2+1 and y1 == y2+1:
            return False
        if x1 == x2+1 and y1 == y2-1:
            return False
        if x1 == x2-1 and y1 == y2+1:
            return False
        if x1 == x2-1 and y1 == y2-1:
            return False
        return True


    for i, tent1 in enumerate(trees):
        for j, tent2 in enumerate(trees):
            if j<=i:
                continue
            #problem.addConstraint(not_together, (tent1, tent2))

    problem.addConstraint(AllDifferentConstraint(), trees)

    for i, col in enumerate(cols):
        

        
        def colsDiff(*vals, i=i, col=col):
            total=0
            for val in vals:
                x, y = val
                if x == i:
                    total+=1


            if total!=int(col):
                return False
            return True
        problem.addConstraint(colsDiff, trees)

    
    # -----------------------------------------------------
    # ---Potoa pobarajte reshenie--------------------------

    solution = problem.getSolution()
    
    # -----------------------------------------------------
    # ---Na kraj otpechatete gi poziciite na shatorite-----

    if solution is not None:
        for sol in solution.values():
            first, second = sol
            print(f'{first} {second}')
    
