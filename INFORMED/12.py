from searching_framework import Problem, astar_search

class Zadaca(Problem):
    def __init__(self, initial, size, allowed, goal=None):
        super().__init__(initial)
        self.size = size
        self.allowed = allowed
        self.dir = {
            "Up 1" : (0, 1),
            "Up 2" : (0, 2),
            "Up-left 1": (-1, 1),
            "Up-left 2": (-2, 2),
            "Up-right 1": (1, 1),
            "Up-right 2": (2, 2),
            "Wait" : (0, 0)
        }

    def successor(self, state):
        successors = {}
        man, house, direction = state
        x, y = man
        hx, hy = house
        for action, (dx, dy) in self.dir.items():
            nx = x + dx
            ny = y + dy
            if direction == "right":
                if hx == self.size[0]:
                    direction = "left"
                    nhx = hx - 1
                else:
                    nhx = hx + 1
            if direction == "left":
                if hx == 0:
                    direction = "right"
                    nhx = hx + 1
                else:
                    nhx = hx - 1
            if 0<=nx<self.size[0] and 0<=ny<self.size[1] and (nx, ny) in self.allowed or (nx, ny) in (nhx, hy):
                successors[action] = ((nx, ny), (nhx, hy), direction)
        return successors
    
    def actions(self, state):
        return self.successor(state).keys()
    
    def result(self, state, action):
        return self.successor(state)[action]
    
    def goal_test(self, state):
        person, house, dir = state
        return person==house
    
    def h(self, node):
        person, house, dir = node.state
        x, y = person
        hx, hy = house
        return max(abs(x - hx), abs(y - hy))

if __name__ == '__main__':
    allowed = [(1,0), (2,0), (3,0), (1,1), (2,1), (0,2), (2,2), (4,2), (1,3), (3,3), (4,3), (0,4), (2,4), (2,5), (3,5), (0,6), (2,6), (1,7), (3,7)]
    
    # your code here

    size = (5, 9)
    person = tuple(map(int, input().split(",")))
    house = tuple(map(int, input().split(",")))
    direction = input()

    problem = Zadaca((person, house, direction), size, allowed)

    result = astar_search(problem)

    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")