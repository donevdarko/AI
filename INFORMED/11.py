from searching_framework import Problem, astar_search

class Zadaca(Problem):
    def __init__(self, initial, size, end, walls,goal=None):
        super().__init__(initial)
        self.end=end
        self.walls=walls
        self.size=size
        self.dir = {
            "Up" : (0, 1),
            "Down" : (0, -1),
            "Left" : (-1, 0),
            "Right 2" : (2, 0),
            "Right 3" : (3, 0)
        }
    
    def successor(self, state):
        x, y = state
        successors = {}

        for action, (dx, dy) in self.dir.items():
            nx = x + dx
            ny = y + dy

            if 0<=nx<self.size and 0<=ny<self.size and (nx, ny) not in self.walls:
                if action == "Right 2" and (x+1, ny) not in self.walls:
                    successors[action] = (nx, ny)
                if action == "Right 3" and (x+1, ny) not in self.walls and (x+2, ny) not in self.walls:
                    successors[action] = (nx, ny)
                if action not in ("Right 2", "Right 3"):
                    successors[action] = (nx, ny)
        
        return successors
    
    def actions(self, state):
        return self.successor(state).keys()
    
    def result(self, state, action):
        return self.successor(state)[action]
    
    def h(self, node):
        x, y = node.state
        gx, gy = self.end
        return (abs(y - gy) + abs(x - gx)/3)
    
    def goal_test(self, state):
        x, y = state
        gx, gy = self.end
        return (x == gx and y == gy)

        

if __name__ == '__main__':
    # your code here
    size = int(input())
    numWalls = int(input())
    walls = tuple([tuple(map(int, input().split(","))) for _ in range(numWalls)])
    person = tuple(map(int, input().split(",")))
    house = tuple(map(int, input().split(",")))

    problem = Zadaca(person, size, house, walls)

    result = astar_search(problem)

    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")

    