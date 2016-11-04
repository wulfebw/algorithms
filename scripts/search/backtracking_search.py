
import sys

import search_algorithm

class BacktrackingSearch(search_algorithm.SearchAlgorithm):
    """
    BacktrackingSearch is a search algorithm that only works 
    on DAGs (though does work with negative weight edges)
    and uses memoization to be somewhat efficient.

    runtime is O(|V|^2) because for each vertex you look at all of its children, but you know that you'll only ever have to compute the cost of a node one time. So in the worst case every node is connect to every subsequent node, giving n^2 run time. Edges don't play a role because limiting factor is nodes. The collection of actions at the end takes O(n).

    In terms of space you have to track the best costs and pointers to the best next state (or you could check each next node at the end)
    """

    def solve(self, problem):
        cache = {}
        ptrs = {}
        def recurse(s):
            mincost = sys.maxint
            bestns = None
            for (a,ns,c) in problem.succAndCost(s):
                if ns in cache:
                    if mincost > c + cache[ns]:
                        mincost = c + cache[ns]
                        bestns = ns
                elif problem.isGoal(ns):
                    cache[ns] = 0
                    if mincost > c:
                        mincost = c
                        bestns = ns
                else:
                    val = recurse(ns)
                    if mincost > val + c:
                        mincost = val + c
                        bestns = ns
            cache[s] = mincost
            ptrs[s] = bestns
            return mincost

        start_state = problem.startState()
        recurse(start_state)
        self.cost = cache[start_state]

        s = start_state
        self.actions = [s]
        while not problem.isGoal(s):
            s = ptrs[s]
            self.actions.append(s)

        # can alternatively do with only the cost cache
        # s = start_state
        # self.actions = [s]
        # while not problem.isGoal(s):
        #     bestns = None
        #     mincost = sys.maxint
        #     for (a,ns,c) in problem.succAndCost(s):
        #         if cache[ns] < mincost:
        #             bestns = ns
        #             mincost = cache[ns]
        #     self.actions.append(bestns)
        #     s = bestns
