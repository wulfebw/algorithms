
import sys

def rod_cut(p, n):

    r = {}
    for idx in range(1, n + 1):
        r[idx] = -sys.maxint

    def recurse(n):
        # return cache
        if n in r and r[n] >= 0:
            return r[n]

        # reached the end then the revenue is 0
        if n == 0:
            q = 0

        # otherwise compute revenue recursively
        else:
            q = -sys.maxint
            for idx in range(1, n + 1):
                revenue_for_cut = p[idx]
                future_revenue = recurse(n - idx)
                q = max(q, revenue_for_cut + future_revenue)
            r[n] = q

        # return costs
        return q

    max_revenue = recurse(n)
    return r, max_revenue


if __name__ == '__main__':
    # prices for cuts of idx length
    p = {1:1, 2:2, 3:5, 4:7}
    # rod length
    n = 4
    # greedy solution:
    # cuts at [1]
    # revenue: 1 + 5 = 6

    # optimal solution:
    # no cuts
    # revenue: 7

    revenues, max_revenue = rod_cut(p, n)
    print max_revenue
    print revenues



    p = {}
    n = 20
    for idx in range(n + 1):
        p[idx] = idx
    p[2] = 100

    revenues, max_revenue = rod_cut(p, n)
    print max_revenue
    print revenues





