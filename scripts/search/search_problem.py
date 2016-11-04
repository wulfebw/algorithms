class SearchProblem(object):
    # Return the start state.
    def startState(self): raise NotImplementedError("Override me")

    # Return whether |state| is a goal state or not.
    def isGoal(self, state): raise NotImplementedError("Override me")

    # Return a list of (action, newState, cost) tuples corresponding to edges
    # coming out of |state|.
    def succAndCost(self, state): raise NotImplementedError("Override me")

# A simple search problem on a square grid:
# Start at init position, want to go to (0, 0)
# cost 2 to move up/left, 1 to move down/right
class GridSearchProblem(SearchProblem):
    def __init__(self, size, x, y): self.size, self.start = size, (x,y)
    def startState(self): return self.start
    def isGoal(self, state): return state == (0, 0)
    def succAndCost(self, state):
        x, y = state
        results = []
        if x-1 >= 0: results.append(('North', (x-1, y), 1))
        if x+1 < self.size: results.append(('South', (x+1, y), 2))
        if y-1 >= 0: results.append(('West', (x, y-1), 1))
        if y+1 < self.size: results.append(('East', (x, y+1), 1))
        return results

class DAGSearchProblem(SearchProblem):
    def __init__(self): 
        self.adj = {0:[1,2],
                    1:[4,5],
                    2:[3],
                    3:[4,8],
                    4:[5,6],
                    5:[7],
                    6:[7],
                    7:[8],
                    8:[]}
        self.start = 0
    def startState(self): return self.start
    def isGoal(self, state): return state == 8
    def succAndCost(self, state):
        assert state in self.adj
        cost = 1000 if (state == 3 or state == 5) else 1
        return [('right', ns, cost) for ns in self.adj[state]]
