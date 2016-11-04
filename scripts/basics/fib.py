

def fib1(n):
    """
    Doesn't work because over prints
    """
    prev_1 = 1
    prev_2 = 1
    for i in range(n):
        print prev_1
        print prev_2
        prev_1 = prev_1 + prev_2
        prev_2 = prev_2 + prev_1

def fib2(n):
    """
    Works but you have to iterate until range(n-2)
    """
    a = 1
    b = 1
    yield a 
    yield b
    for i in range(n - 2):
        b, a = a + b, b
        yield b

def fib3(n):
    """
    Works and prints correct n
    """
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

def fib_rec(n):
    """
    Recursive cache version
    """
    cache = {1:1, 2:1}
    def recurse(n):
        if n in cache:
            return cache[n]
        else:
            val = recurse(n-1) + recurse(n-2)
            cache[n] = val
            return val

    return recurse(n)
    

if __name__ == '__main__':
    fib_rec(10)
    print(list(fib3(10)))
