
import numpy as np

def partition(a):
    """
    given a set, determine if you can partition into two sets s.t. the sum 
    is the same

    ok so if you sum these numbers and they are odd then it's impossible
    so first you compute the sum and check that 

    so now you have an even sum what do you do?
    can you view this as a graph?
    yeah of course but what's the graph
    dag?
    not sure
    so for each number you can either put it in set 1 or set 2
    what's the subproblem?
    at each point in the list know whether you can separte up tot hat point 
    evenly?
    seems like it takes the same form as the longest nondecreasing
    but why?

    find a subset equal to sum/2 b/c the other subset must therefore equal sum/2
    as well
    ok h = sum(s) / 2
    for each number decide whether to add it to the set or not
    ok
    2d array 
    size sum/2 x n+1
    where the rows correspond to sums
    where the cols correspond to whether or not a subset starting at this location
    and moving backward can sum up to the value
    how would you fill this?

    [2,1,1]

    originally
    
    [0,0,0]
    [0,0,0]

    [0,1,1]
    [0,0,0]

    [0,0,0]
    [0,0,0]


    how to fill (2,1)? 0 based indexing
    - not sure
    for each row you go through the entire sequence

    I think it works like this
    for each possible sum value
    you see if you could add up the elements to that sum
    the way you do this efficiently is you if the current sum value (call that i)
    minus the value you're going to add (v[j-1]) could add up to whatever sum 
    results 
    then it should work
    so 
    looking at that example

    [2,1,1]

    0 [1,1,1,1] # all ones here indicate that of course you can add to 0
    1 [0,0,0,0]
    2 [0,0,0,0]

    deciding the first value
    value is 2
    is 2 less than the current sum? no then no

    0 [1,1,1,1] 
    1 [0,0,0,0]
    2 [0,0,0,0]

    next look at 1 
    first of all, if you could have added to the current sum by the 
    prior column
    then you can still add to that value by not considering this value
    so initialize it to the value in the column before which here is 0
    the other condition whereby this cell might be true is that 
    where the current sum minus the current value is achievable without using 
    the current value
    current sum = 1
    current value = 1
    table[0,] 
    0 [1,1,1,1] 
    1 [0,0,0,0]
    2 [0,0,0,0]
    
    ok so how does this work?
    it relies on the fact that the sum is integer only 
    and you basically find out whether you can sum to any value that is 
    less than half of the total

    it does this by creating a table where the rows are the possible sums
    i.e., all values < sum/2
    and the rows correspond to the elements plus a row without anything 

    so example

    [2,1,1]
    sum/2 = 2

    table
      {} {2} {2,1} {2,11} # so the cols reflect the subsets up to that point
      # and whether that subset can add to that sum
    0 [1,1,1,1] # b/c anything can add to 0 if you don't take it
    1 [0,0,0,0] 
    2 [0,0,0,0]
    
    # initialize each new cell to the cell left of it 
    # because if the previous set could add to the value
    # then the new set can as well by not using the new value

    # to fill in (1, {2,1})
    # look at the row minus the element (1 - 1) = 0 // this row
    # then to know whether you could sum to this value at this column 
    # you ask without this column could you sum to this sum minus this column?
    the answer to this question is in part[i - arr[j-1]][j-1]
    this indexing is tricky
    j-1 indexes into the array where the jth element is 
    whereas it indexes into the container where the sum without this value is
    """
    a, s = np.array(a), np.sum(a)
    if s % 2 == 1:
        return False, []
    s, n = int(s/2), len(a)
    t = np.zeros((s+1, n+1))
    t[0,:] = 1
    for i in range(1, s+1): 
        # j indexes into t for the j-1 element of a
        for j in range(1, n+1):
            # if you can sum to the value without this col, then you can with it
            t[i,j] = t[i,j-1] 
            if s >= a[j-1]:
                # again if t[i,j-1] true then stay true
                # become true if the current sum minus the current col value 
                # can be produced using value up to but not including the current
                # value
                t[i,j] = t[i,j] or t[i-a[j-1]][j-1]

    print(t)
    # how do you get the partitioning?
    # move left until final true value
    # subtract that value 
    # repeat
    # gives the indices of the values contributing to the sum
    i, j, idxs = s, n, []

    while True:
        if i == 0:
            break
        while True:
            if t[i,j-1]:
                j -=1
            else:
                break
        # a[j-1] is part of group
        idxs.append(j-1)
        i -= a[j-1]

    # if you want to know whether you can do the partition, just return 
    # whether anything in the last row is true
    return np.any(t[-1,:]), idxs

def test_partition():
    arrs = [
        [2,1,1],
        [],
        [2,1],
        [2,2],
        [2,1,1,1,1,1,1,1,1,1,11]
    ]
    ans = [True, True, False, True, True]
    for i, (arr, e) in enumerate(zip(arrs, ans)):
        print('arr: {}'.format(arr))
        a, idxs = partition(arr)
        print(idxs)
        if a != e:
            print('incorrect: {} expected: {} actual: {}'.format(i, e, a))
        else:
            print('problem {} passed'.format(i))

def test_parition_2():
    arr = np.random.randint(3, size=(100))
    rslt, idxs = partition(arr)
    other = list(set(np.arange(len(arr))).symmetric_difference(idxs))
    print(other)
    print(idxs)
    print(rslt)
    print(np.sum(arr[idxs]))
    print(np.sum(arr[other]))

if __name__ == '__main__':
    # test_partition()
    test_parition_2()