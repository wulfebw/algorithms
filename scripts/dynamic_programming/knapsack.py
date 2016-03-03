import collections 

# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    #return K[n][W]
    return K

def knapSack_recursive(W, wt, val, n):
    cache = collections.defaultdict(lambda: 0)

    def recurse(i, W_r):
        if i >= n:
            return 0

        if cache[(i, W_r)] > 0:
            return cache[(i, W_r)]

        if wt[i] > W_r:
            return recurse(i + 1, W_r)

        max_val = max(val[i] + recurse(i + 1, W_r - wt[i]), recurse(i + 1, W_r))
        cache[(i, W_r)] = max_val
        return max_val

    recurse(0, W)
    return cache
 
# Driver program to test above function
val = [60, 100, 120]
wt = [10, 20, 30]
W = 49
n = len(val)
k = knapSack_recursive(W, wt, val, n)
print k[(0,W)]
for i in range(n+1):
        for w in range(W+1):
            #print k[i][w],
            print k[(i,w)],
        print '\n'
 
# This code is contributed by Bhavya Jain