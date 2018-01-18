'''
this is just the longest common subsequence of the string and its reverse

First note that the longest palindromic subseq could occur fully on one half of 
the string or the other. This means you can't do anything like only compare 
values on one half to the other.

Given that, you just have to realize that if you start at the ends of the 
string, and those values are the same, then you can greedily chop them off
i.e., just keeping these does not sacrifice the optimality
but if they are not the same you have to try chopping off one from each 
end individually

'''

from longest_common_subsequence import lcs_iterative

def longest_palindromic_subseq(a):
    return lcs_iterative(a, list(reversed(a)))

if __name__ == '__main__':
    inputs = [
        'abab',
        'abaaa',
        'abdcda',
        'asdfggfdsa',
        'asdgfgfdsa',
        'asdfgzgfdsa',
    ]
    expect = [
        3,
        4,
        5,
        10,
        9,
        11
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(longest_palindromic_subseq(i))
        print()
