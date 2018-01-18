
import sys
sys.setrecursionlimit(10000)

def compute_optimal_value(v):
    cache = {}

    def recurse(s,e):
        if e - s <= 0:
            return (0,0)
        elif (s,e) in cache.keys():
            return cache[(s,e)]
        else:
            l = recurse(s+1,e)
            r = recurse(s,e-1)

            if (e - s) % 2 == 0: # first player
                if l[0] + v[s] > r[0] + v[e-1]:
                    cache[(s,e)] = (l[0] + v[s], l[1])
                else:
                    cache[(s,e)] = (r[0] + v[e-1], r[1])
            else: # second player
                if l[1] + v[s] > r[1] + v[e-1]:
                    cache[(s,e)] = (l[0], l[1] + v[s])
                else:
                    cache[(s,e)] = (r[0], v[e-1])
            return cache[(s,e)]

    recurse(0, len(v))
    print('keys: {}'.format(len(cache.keys())))
    return cache[(0, len(v))][0]

if __name__ == '__main__':
    inputs = [
        [1,2],
        [0,0,0,0,10000,0,0,0],
        [5,3,7,10],
        [9,9,9,9,9,1,100,10],
        list(range(1000))
    ]
    expect = [
        2,
        10000,
        15,
        127,
        'no idea'
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(compute_optimal_value(i))

