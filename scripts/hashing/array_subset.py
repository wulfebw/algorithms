

def check_subset(a1, a2):
    '''
    O(n) method that converts to a2 to a set and checks for subset

    how could you do better than O(n)? you have to iterate all the elements 
    of a2 at the very least
    '''
    return set(a2).issubset(a1)


if __name__ == '__main__':

    inputs = [
        ([1,2,3],[2,3]),
        ([1,2,3],[2,3,4])
    ]

    for i in inputs:
        print(check_subset(*i))
