
import math

def find_position_recursive(n):

    def recurse(idxs):
        if len(idxs) == 1:
            return idxs[0]
        else:
            idxs = idxs[1::2]
            return recurse(idxs)

    return recurse(list(range(1,n+1)))

def find_position(n):
    '''
    it's the lat position in the list that's a power of two 
    the reason is that each time you take the even numbers 
    you're dividing the length of the list by two and 
    throwing out all the numbers that aren't evenly divisible
    so what will be the last number remaining? whichever is the 
    largest number in the list that's a power of two
    '''
    return 2 ** int(math.log(n,2))

if __name__ == '__main__':

    inputs = [
        7,
        8
    ]
    expect = [
        4,
        8
    ]
    for (i,e) in zip (inputs, expect):
        print(e)
        print(find_position(i))
        print()