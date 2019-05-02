

def sum_three(a):
    '''
    Description:
        - by sorting the array we allow for a faster traversal
        - this is an O(n^2) solution, compared with an O(n^3) brute force 
        solution
    '''
    a.sort()
    n = len(a)
    for i in range(n):

        j = i + 1
        k = n - 1
        while j < k:

            total = a[i] + a[j] + a[k]
            if total == 0:
                return True

            elif total < 0:
                j += 1

            else:
                k -= 1

    return False