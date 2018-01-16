
import math

def binomial_coef_formula(n, k):
    return int(math.factorial(n) / (math.factorial(n-k) * math.factorial(k)))

def binomial_coef_recursive(n, k):
    cache = dict()

    def recurse(n, k):
        if n == 0: return 0 
        elif k == 0: return 0 
        elif k == 1: return n 
        else:
            val = recurse(n-1,k-1) + recurse(n-1,k)
            cache[n] = val
            return val

    return recurse(n, k)




if __name__ == '__main__':
    inputs = [
        (5,3),
        (8,5),
        (100,4),
        (321,10)
    ]
    expect = [
        10,
        56,
        3921225,
        2778403127425644576
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(binomial_coef_formula(*i))
        print()
