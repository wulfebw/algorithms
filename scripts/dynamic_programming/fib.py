

def fib_iterative(n):
    prev, cur = 0, 1
    for i in range(n):
        prev, cur = cur, prev + cur
    return prev

def fib_recursive(n):
    cache = dict()

    def recurse(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1 
        elif n in cache.keys():
            return cache[n]
        else:
            val = recurse(n-1) + recurse(n-2)
            cache[n] = val
            return val

    return recurse(n)


if __name__ == '__main__':
    inputs = [
        0,
        1,
        2,
        3,
        4,
        5,
        6
    ]
    expect = [
        0, 
        1, 
        1, 
        2,
        3,
        5,
        8
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(fib_recursive(i))