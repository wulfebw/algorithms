
import search_problem
import backtracking_search

class PyramidProblem(search_problem.SearchProblem):
    def __init__(self):
        self._transitions = {'root': ('a', 'a'),
                             'a':('b','c'),
                             'b':('d','e'),
                             'c':('e','f'),
                             'd':('g','h'),
                             'e':('h','i'),
                             'f':('i','j'),
                             'g':(),
                             'h':(),
                             'i':(),
                             'j':()}
        self._costs = {'a':137,'b':42,'c':-15,'d':-4,
            'e':13,'f':45,'g':21,'h':14,'i':-92,'j':33}
    def startState(self):
        return 'root'
    def isGoal(self, state):
        if self._transitions[state] == ():
            return True
    def succAndCost(self, state):
        actions = ['left', 'right']
        next_states = self._transitions[state]
        if next_states == ():
            return []
        costs = [self._costs[next_states[0]], self._costs[next_states[1]]]
        return zip(actions, next_states, costs)

if __name__ == '__main__':
    problem = PyramidProblem()
    algo = backtracking_search.BacktrackingSearch()
    algo.solve(problem)
    print(algo.cost)
    print(algo.actions)

