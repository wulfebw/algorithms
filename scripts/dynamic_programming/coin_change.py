
from context_timer import ContextTimer

def find_change_recursive_inefficient(n, vals):
    '''
    this is a recursive solution that misses the point
    run time is 
    a function of the number of ways that you can form the amount
    you instead need to formualte it in terms of the coins and the amount 
    '''

    cache = dict()
    def recurse(n):
        if n == 0: # valid solution
            return set([tuple()])
        elif n < 0: # invalid
            return set()
        elif n in cache.keys():
            return cache[n]
        else:
            total = set()
            for v in vals:
                curways = recurse(n-v)
                cache[n-v] = curways
                for way in curways:
                    newtuple = tuple(sorted(way + (v,)))
                    total.add(newtuple)
            cache[n] = total
            return cache[n]

    return len(recurse(n))

# Dynamic Programming Python implementation of Coin Change problem
def find_change_iterative(S, m, n):
    # We need n+1 rows as the table is consturcted in bottom up
    # manner using the base case 0 value case (n = 0)
    table = [[0 for x in range(m)] for x in range(n+1)]
 
    # Fill the enteries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1
 
    # Fill rest of the table enteries in bottom up manner
    for i in range(1, n+1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
 
            # Count of solutions excluding S[j]
            y = table[i][j-1] if j >= 1 else 0
 
            # total count
            table[i][j] = x + y
 
    return table[n][m-1]


if __name__ == '__main__':

    inputs = [
        (4, set([1,2,3])),
        (10, set([2,5,3,6])),
        (50, set([1,2,3,4,5])),
        (100, set([2,3,4,5,6,7,8,9]))
    ]
    expect = [
        4,
        5,
        3765,
        8471
    ]

    for (i,e) in zip(inputs, expect):
        print(e)
        with ContextTimer():
            print(find_change_recursive(*i))
        with ContextTimer():
            print(find_change_iterative(list(i[1]),len(i[1]),i[0]))
        print()
        print()
