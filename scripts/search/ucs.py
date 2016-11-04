
import priority_queue
import search_algorithm

class UCS(search_algorithm.SearchAlgorithm):
    """
    Djikstra's
    Time: O(nlgn) where n is states between start state and goal state in shortest path, lgn factor from the priority queue operations (heapify) 
    """
    def solve(self, problem):
        done = set()
        start = problem.startState()
        goal_state = None
        cache = {start:(0, start)}
        pq = priority_queue.PriorityQueue()
        pq.push(0, start)
        while not pq.is_empty():
            cost_to, s = pq.pop()

            # once we pop a state skip it
            if s in done:
                continue
            done.add(s)

            # goal then must have traversed shortest path
            if problem.isGoal(s):
                self.cost, _ = cache[s]
                goal_state = s
                break

            # add each ns to pq if cost lower now
            for (a,ns,c) in problem.succAndCost(s):
                total = cost_to + c
                if ns not in cache:
                    cache[ns] = (total, s)
                    pq.push(total, ns)
                elif cache[ns][0] > total:
                    cache[ns] = (total, s)
                    pq.push(total, ns)

        # collect actions with backpointers
        self.actions = [goal_state]
        s = goal_state
        while s != start:
            ps = cache[s][1]
            self.actions.append(ps)
            s = ps
        self.actions.reverse()


        

