
import numpy as np

def zeros_and_ones(v):
    v = np.array(v)
    m, n = v.shape
    maxs = np.zeros((m, n))
    maxs[:,0], maxs[0,:] = v[:,0], v[0,:]
    for i in range(1, m):
        for j in range(1, n):
            # value is one, consider possible increment
            if v[i,j] == 1:
                uv, lv, dv = v[i-1,j], v[i,j-1], v[i-1,j-1]
                um, lm, dm = maxs[i-1,j], maxs[i,j-1], maxs[i-1,j-1]
                max_prev = max([um,lm,dm])
                if (uv == 1 and lv == 1 and dv == 1 
                    and um == lm and lm == dm):
                    maxs[i,j] = max_prev + 1
                elif um == 0 and lm == 0 and dm == 0:
                    maxs[i,j] = 1
                else:
                    maxs[i,j] = max_prev
            # value is zero so just take the max of the left, up, diagonal
            else:
                maxs[i,j] = np.max([maxs[i-1,j], maxs[i,j-1], maxs[i-1,j-1]])


    # at this point each cell gives the largest square up and left of it 
    # traverse backward greedily to find the corner of the largest sqaure
    # at that point, the i-size, j-size block will be the largest square
    largest = maxs[-1,-1]
    i, j = maxs.shape
    i, j = i-1, j-1
    while True:
        if i == 0:
            break
        if maxs[i-1, j] == largest:
            i-=1
        else:
            break

    while True:
        if j == 0:
            break
        if maxs[i, j-1] == largest:
            j-=1
        else:
            break

    # at this point i,j give the bottom right index of the square, just return
    print()
    print(v)
    print(maxs)
    return i, j, int(maxs[i,j])
    
def test_zeros_and_ones():
    # 1 
    questions = []
    answers = []
    q = [[1,1,1],
        [1,1,1],
        [1,1,1]]
    a = (2,2,3)
    questions.append(q)
    answers.append(a)

    # 2 
    q = [[0,1,0],
        [0,1,1],
        [0,1,1]]
    a = (2,2,2)
    questions.append(q)
    answers.append(a)

    # 3
    q = [[0,0,1,1],
        [0,0,1,1],
        [1,1,0,0],
        [1,1,0,0]]
    a = (1,3,2)
    questions.append(q)
    answers.append(a)

    # 4
    q = [[0,0,0,0,0],
        [0,1,1,1,1],
        [0,1,1,1,0],
        [0,1,1,1,0],
        [0,0,0,0,0]]
    a = (3,3,3)
    questions.append(q)
    answers.append(a)

    # 5
    q = [[0,0,1,1,1,1],
        [0,0,1,1,1,1],
        [1,1,1,1,1,1],
        [1,1,1,1,1,1],
        [1,1,1,0,0,0],
        [1,1,1,0,0,0]]
    a = (3,5,4)
    questions.append(q)
    answers.append(a)

    # 6
    q = [[0,0,0,0,0],
        [0,1,1,1,0],
        [0,1,0,1,0],
        [0,1,1,1,0],
        [0,0,0,0,0]]
    a = (1,1,1)
    questions.append(q)
    answers.append(a)

    for i, (q, a) in enumerate(zip(questions, answers)):
        actual = zeros_and_ones(q)
        if actual != a:
            print('test {} failed. expected: {}, got: {}'.format(i, a, actual))
        else:
            print('test {} passed'.format(i))

"""
    # let's think of it as a message passing problem
    # in that case, each cell in the array is a variable
    # passing messages left to right
    # top to bottom
    # first question is, can you just do one pass?
    # consider an example
    # [1,1,1]
    # [1,1,1]
    # [1,1,1]
    # how would you do it in this case?
    # use a separate matrix that tracks?
    # the largest up to that point?
    # can you break it up by row?
    # if it's square then what?
    # ok so maintain an equal shape array
    # where each cell tracks the largest square up to that point
    # the size?
    # and then you work backward at the end to identify the square
    # when both left and right are 1, add 1
    # doesn't work b/c need to know the current size?

    # [1,1,1]
    # [1,1,1]
    # [1,1,1]

    # [0,0,0]
    # [0,0,0]
    # [0,0,0]

    # [1,1,0]
    # [0,0,0]
    # [0,0,0]

    # [1,1,0]
    # [1,2,0]
    # [0,0,0]

    # [1,1,1]
    # [1,2,0]
    # [0,0,0]

    # [1,1,1]
    # [1,2,2]
    # [0,0,0]

    # [1,1,1]
    # [1,2,2]
    # [1,0,0]

    # [1,1,1]
    # [1,2,2]
    # [1,2,0]

    # [1,1,1]
    # [1,2,2]
    # [1,2,3]

    # ok what about 
    # [0,1,0]
    # [0,1,1]
    # [0,1,1]

    # [0,1,0]
    # [0,0,0]
    # [0,0,0]

    # [0,1,1]
    # [0,0,0]
    # [0,0,0]

    # [0,1,1]
    # [0,1,0]
    # [0,0,0]

    # [0,1,1]
    # [0,1,1]
    # [0,0,0]

    # [0,1,1]
    # [0,1,1]
    # [0,1,2]

    # so at this point the strategy seems to be 
    # move left to right
    # top to bottom
    # have a separate array of equal size
    # each cell tracks the larget sqaure of ones up to that point
    # the rules for setting the value in a cell are 
    # the value of the next cell equals the max of the left and up 
    # and if both of left and up are 1, then the max  + 1
    # have to hanlde the 
    # 0 1
    # 1
    # case
    # how? check if the diagonal is also one?
    # sure why not
    # ok so it's then if left up and diagonal are all ones
    # then the max of them plus one else just the max

    # [0,0,1,1]
    # [0,0,1,1]
    # [1,1,0,0]
    # [1,1,0,0]

    # [0,0,1,1]
    # [0,0,1,2]
    # [1,1,1,2]
    # [1,2,2,2]

    # ok what about 
    # ok to increment they all must be the same
    # they all must be one in value
    # otherwise just take the max

    # [0,0,0,0,0]
    # [0,1,1,1,1]
    # [0,1,1,1,0]
    # [0,1,1,1,0]
    # [0,0,0,0,0]

    # [0,0,0,0,0]
    # [0,1,1,1,1]
    # [0,1,2,2,2]
    # [0,1,2,3,3]
    # [0,1,2,3,3]

    # ok what about

    # [0,0,1,1,1,1]
    # [0,0,1,1,1,1]
    # [1,1,1,1,1,1]
    # [1,1,1,1,1,1]
    # [1,1,1,0,0,0]
    # [1,1,1,0,0,0]

    # [0,0,1,1,1,1]
    # [0,0,1,2,2,2]
    # [1,1,1,2,3,3]
    # [1,2,2,2,3,4]
    # [1,2,3,3,3,4]
    # [1,2,3,3,3,4]

    # ok seems to work
    # so that's
    # track max up to that point in a same size container
    # the rules for incrementing are 
    # increment if left, right, diagonal are all the same value and all are 1 
    # otherwise just take the max
    # well what about

    # [0,0,0,0,0]
    # [0,1,1,1,0]
    # [0,1,0,1,0]
    # [0,1,1,1,0]
    # [0,0,0,0,0]

    # [0,0,0,0,0]
    # [0,1,1,1,0]
    # [0,1,1,1,0]
    # [0,1,1,1,0]
    # [0,0,0,0,0]

    # ok seems good lets do it
    # well how do you get back?
    # start in bottom right
    # follow the largest number until it is no longer the largest 
    # and you'll be at the corner
"""

def longest_nondecreasing_subsequence(seq):
    """
    the question is what space do you need to keep?
    is it just a same size container?

    [0,1,2,1]

    [1,0,0,0]
    [0,2,0,0]
    [0,0,3,0]
    [0,0,0,3]

    ok so at this pt it seems you can iterate the list
    if the value at some location is geq to previous value 
    increment in the other container
    otherwise set the max value at this location to one

    so that prob doesn't work but why?
    yeah it doesn't work because a subsequence entails removing elements
    i.e., it's not a substring problem 

    ok so trying that again
    [0,1,0,2] -> should be [0,1,2] of length 3
    seem like need more space then 
    know that the best I can do is nlgn probably 
    seems like this is edit distance?
    i think the strategy is to like place copies of it next to itself
    ok well how would I do it on the example?
    
    [0,1,0]
    what's the subproblem?
    knowing the max nondecreasing length at each previous point along with ?
    well it definitely seems like you need a 2d array to do it
    the options are really keep or delete each number right?
    so what if you ...
    hmm
    ok
    [0,2,0,0] -> [0,0,0] = 3

    [1,2,1,2]
    [1,0,0,0]
    [0,0,0,0]
    [0,0,0,0]
    
    ok so the answer takes the form of a nested for loop and a container
    of equal length to the sequence
    [0,2,0,0] -> [0,0,0] = 3
    
    L = [0,0,0,0]

    for i = 1 to n 
        for j = 0 to i # not inclusive

    i=0
    L=[1,0,0,0]

    i=1
    first look at 
    [0,2]
    then 
    [2]
    because 


    """
    pass 



if __name__ == '__main__':
    test_zeros_and_ones()

