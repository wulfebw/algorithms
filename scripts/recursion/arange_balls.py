
from context_timer import ContextTimer

def arrange_balls(n, use_cache=True):
    cache = dict()

    def recurse(n, p):
        if n == 0:
            return 1
        elif use_cache and (n,p) in cache.keys():
            return cache[(n,p)]
        else:
            if p == 'r':
                res = recurse(n-1,'r') + recurse(n-1,'b') + recurse(n-1,'g')
            elif p == 'b':
                res = recurse(n-1,'b') + recurse(n-1,'g')
            else:
                res = recurse(n-1,'g')
            cache[(n,p)] = res
            return res

    return recurse(n, 'r')

def arrange_balls_eq(n):
    return ((n+2)*(n+1))/2

if __name__ == '__main__':
    inputs = [
        1,
        2,
        42
    ]
    expect = [
        3,
        6,
        946
    ]
    for i,e in zip(inputs, expect):
        print(e)
        with ContextTimer():
            print(arrange_balls(i, use_cache=False))
        with ContextTimer():
            print(arrange_balls(i, use_cache=True))
        print()