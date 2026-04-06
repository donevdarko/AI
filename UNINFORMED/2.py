from searching_framework import *

class Fudbaler(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.board = (8, 6)
        self.opps = ((3, 3), (5, 4))
        self.goalPos = ((7, 2), (7, 3))

    def goal_test(self, state):
        _, ballPos = state
        return ballPos in self.goalPos
    
    def check_valid(self, state):
        manPos, ballPos = state
        x, y = manPos
        if not (0<=x<self.board[0] and 0<=y<self.board[1]):
            return False
        if manPos in self.opps:
            return False
        if ballPos in self.opps:
            return False
        x, y = ballPos
        if not (0<=x<self.board[0] and 0<=y<self.board[1]):
            return False
        
        oppsDir = ((-1, -1), (-1, 0), (-1, 1),
                   (0, -1), (0, 0), (0, 1),
                   (1, -1), (1, 0), (1, 1))
        for defender in self.opps:
            for plocka in oppsDir:
                u = (defender[0] + plocka[0], defender[1] + plocka[1])
                if ballPos == u:
                    return False
        return True


    def successor(self, state):
        successors = dict()

        directions = {
            "up" : (0, 1),
            "down" : (0, -1),
            "right" : (1, 0),
            "up-right" : (1, 1),
            "down-right" : (1, -1)
        }

        manPos, ballPos = state
        x, y = manPos
        bx, by = ballPos

        for action, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            nbx, nby = bx + dx, by + dy
            if (nx, ny) == (bx, by) and self.check_valid(((nx, ny), (nbx, nby))):
                successors[f'Push ball {action}'] = ((nx, ny), (nbx, nby))
            if (nx, ny) != (bx, by) and self.check_valid(((nx, ny), ballPos)):
                successors[f'Move man {action}'] = ((nx, ny), ballPos)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

if __name__ == '__main__':
    manPos = tuple(map(int, input().split(',')))
    ballPos = tuple(map(int, input().split(',')))

    fudbal = Fudbaler((manPos, ballPos))
    
    result = breadth_first_graph_search(fudbal)

    if result is None:
        print("No Solution!")
    else:
        print(result.solution())