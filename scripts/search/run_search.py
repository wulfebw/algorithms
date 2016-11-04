
import backtracking_search
import search_problem
import ucs


if __name__ == '__main__':
    # backtracking
    algo = backtracking_search.BacktrackingSearch()
    problem = search_problem.DAGSearchProblem()
    algo.solve(problem)
    print(algo.cost)
    print(algo.actions)

    # djikstra's
    algo = ucs.UCS()
    #problem = search_problem.GridSearchProblem(size=500, x=20, y=4)
    problem = search_problem.DAGSearchProblem()
    algo.solve(problem)
    print(algo.cost)
    print(algo.actions)
