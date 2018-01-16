'''
Why does this work?
It works because at each point in time we know that 
1. the next number generated will be a multiple of 2, 3, or 5 of an ugly number
hmmm
what else
I think we know that each number you generate is a multiple of 2,3,5 of an ugly 
number, and each time you generate that multiple, you can increment the factor 
that yielded it
but why?
not sure to be honest
it's because for each factor, you iterate the numbers in order
the problem is just figuring out which factor to iterate forward
this approach takes this view explictly, iterating each a step at a time
'''

def ugly_numbers(n):
    ugly = [1]
    i2, i3, i5 = 0, 0, 0
    for i in range(n-1):
        n2 = ugly[i2] * 2
        n3 = ugly[i3] * 3
        n5 = ugly[i5] * 5
        n = min(n2,n3,n5)
        ugly.append(n)
        i2 += 1 if n == n2 else 0 
        i3 += 1 if n == n3 else 0
        i5 += 1 if n == n5 else 0
    return ugly[-1]

if __name__ == '__main__':
    inputs = [
        7,
        10,
        15,
        150
    ]
    expect = [
    8,
    12,
    24,
    5832
    ]

    for (i,e) in zip(inputs, expect):
        print(e)
        print(ugly_numbers(i))
        print()