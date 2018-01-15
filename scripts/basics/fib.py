

def fib1(n):
    """
    Doesn't work because over prints
    """
    prev_1 = 1
    prev_2 = 1
    for i in range(n):
        print(prev_1)
        print(prev_2)
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



def myfibrec(n):
    cache = {0:1, 1:1}

    def recurse(n):
        if n in cache:
            return cache[n]
        else:
            cache[n-1] = recurse(n-1) 
            cache[n-2] = recurse(n-2)
            return cache[n-1] + cache[n-2]

    return recurse(n-1)

def myfib2(n):
    # just returns the nth fib number
    prev, cur = 1, 1 # at this point, prev is the first and cur is the second
    for _ in range(1, n): 
        prev, cur = cur, prev + cur
        # after the first iteration, prev is the second, cur is the third
        # updating each n - 1 times will therefore leave cur as the n + 1
        # number in the sequence and prev as the nth number in the sequence
    # return the previous because at this point 
    # the cur has been updated n+1 times
    return prev 

def myfib(n):
    # print the fib numbers up to and including the nth number
    # start at 1s
    prev, cur = 1, 1
    print(1, prev)
    # each step in this for loop computes the next number
    # i.e., a is just a placeholder for the last, with b serving as the 
    # current value
    # why only to n-1? because you print once before the for loop, so the 
    # loop must execute one less time than the desired number
    for i in range(1, n):
        prev, cur = cur, prev + cur
        print(i + 1, prev)

    return prev # 


def myfib3(n):
    # what's the key?
    # the key is that prev contains the number to print (after)
    # or cur the number to print before
    # and that prev starts as the first number, so you have to iterate 
    # one less time to get the nth number

    # initialize such that prev is the first number
    # this means that by iterating n - 1 times, we will print the first 
    # n numbers 
    prev, cur = 1, 1 
    print(prev)
    for _ in range(1, n):
        prev, cur = cur, prev + cur
        print(prev)
        
    return prev

if __name__ == '__main__':
    # fib_rec(10)
    # print(list(fib3(10)))
    v1 = myfib(10)
    v2 = myfib2(10)
    v3 = myfibrec(10)
    v4 = myfib3(10)
    # print(v1)
    # print(v2)
    # print(v3)
    # print(v4)
