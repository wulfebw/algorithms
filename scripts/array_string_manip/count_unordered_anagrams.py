
import collections

def count_unordered_substring_naive(a):
    '''
    analysis:
    - 3 for loops
    - in each for loop you sort something that varies in length from n to 1
    - so it might not be tight, but a bound is therefore O(n^4lgn)
        + O(n^3 * nlgn)
        + could actually improve this if you used some additional space
            * sort all substrings: O(n^2 * nlgn) = O(n^3lgn) + O(n^2) space
            * then run this loop O(n^3)
            * so that would be a O(n^3lgn) solution
    - also, this might be wrong because that comparison hides another loop
        + but the O(n^4lgn) is still valid
    '''
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(i+1, n+1):
            substr_len = j - i
            for k in range(i+1, n + 1 - substr_len):
                if sorted(a[i:j]) == sorted(a[k:k+substr_len]):
                    count += 1
    return count

def counter_nonzero_equals(a,b):
    for k,av in a.items():
        if av != 0 and k in b.keys():
            if av != b[k]:
                return False
    return True

def count_unordered_substring(a):
    '''
    analysis:
    - maintains counts instead of sorting 
    - O(n^3)
        + counter comparison is constant cost
    '''
    ctr_1 = collections.Counter()
    ctr_2 = collections.Counter()
    n = len(a)
    count = 0

    for i in range(n):
        for j in range(i+1, n):

            ctr_1.clear()
            ctr_1.update(a[i:j])
            ctr_2.clear()
            ctr_2.update(a[i:j])

            substr_len = j - i
            s = i + 1
            while s + substr_len <= n:
                ctr_2[a[s-1]] -= 1
                ctr_2[a[s-1+substr_len]] += 1
                if counter_nonzero_equals(ctr_1, ctr_2):
                    count += 1
                s += 1

    return count

'''
you could do better in time complexity if you count the counts of 
unique letter counts, but that comes with a fair amout of space
'''

if __name__ == '__main__':

    inputs = [
        'abba',
        'abcd',
        'ifailuhkqq',
        'hucpoltgty',
        'ovarjsnrbf',
        'pvmupwjjjf',
        'iwwhrlkpek'
    ]

    expected = [
        4,
        0,
        3,
        2,
        2,
        6,
        3
    ]

    # fn = count_unordered_substring_naive
    fn = count_unordered_substring
    for (i, e) in zip(inputs, expected):
        actual = fn(i)
        print('expected: {} actual: {}'.format(e, actual))