
import utils

def insertion_sort(a):
    '''
    The idea is to iterate the list 
    for each element move from right to left until finding a position to stop 
    it's in-place as a result

    analysis:
    - in the worst case, the two for loops execute in their entirety
    - this is equivalent to comparing each element to each other element 
    - which is choose(n,2) elements, which is O(n^2)

    other points:
    - the key is to realize that the inner loop swaps one by one
    '''
    for i in range(1, len(a)):
        for j in range(i - 1, -1, -1):
            if a[j+1] < a[j]:
                a[j+1], a[j] = a[j], a[j+1]
            else:
                break
    return a

if __name__ == '__main__':
    utils.test_sorting_algorithm(insertion_sort)