
'''
Recursive solution
'''
def compute_optimal_cut(n, prices):
    cache = dict()

    def recurse(n):
        if n in cache.keys():
            return cache[n][0]
        elif n == 0:
            return 0 
        else:
            bestval = prices[n-1]
            bestcut = 0
            for i in range(1, n-1):
                curval = recurse(i) + recurse(n-i)
                if curval > bestval:
                    bestval = curval
                    bestcut = i
            cache[n] = (bestval, bestcut)
            return bestval

    def compute_cuts(n):
        cut = cache[n][1]
        if cut == 0:
            return [n]
        else:
            return compute_cuts(cut) + compute_cuts(n-cut)

    bestval = recurse(n)
    bestcuts = sorted(compute_cuts(n))
    return bestval, bestcuts

'''
Array-based implemetation

Why does this work?
some components to that 
1. it works because if we know the solution for every length up to n-1, then when 
we compute the solution for n, we just need to look at possible combinations of 
those optimal solutions 
'''
def compute_optimal_value_iterative(n, prices):
    v = [0] + prices
    for i in range(n + 1):
        best = 0
        for j in range(i // 2 + 1):
            best = max(best, v[j] + v[i-j])
        v[i] = best
    return v[n]

if __name__ == '__main__':
    inputs = [
        (1, [1]),
        (4, [0,2,3,3]),
        (7, [1,2,3,4,5,6,6]),
        (8, [1,5,8,9,10,17,17,20])
    ]
    expecteds = [
        (1, [1]),
        (4, [2,2]),
        (7, [1,6]),
        (22, [2,6])
    ]

    for (i, e) in zip(inputs, expecteds):
        # a = compute_optimal_cut(*i)
        # print(e[0])
        # print(a[0])
        # print(e[1])
        # print(a[1])
        # print()

        a = compute_optimal_value_iterative(*i)
        print(e[0])
        print(a)
        print()



