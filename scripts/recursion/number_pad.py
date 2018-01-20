
PAD = [
    [''],
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i']
]

def possible_words(a):
    '''
    for each number in the list, in the worst case you'll have to perform 
    4 * subsequent calculations
    so if it's 1 it's 4 
    2 = 4^2
    etc 
    so 4^n 
    so O(4^n)
    '''

    if len(a) <= 0:
        return ['']
    else:
        words = []
        for l in PAD[a[0]]:
            words += [l + suffix for suffix in possible_words(a[1:])]
        return words

if __name__ == '__main__':
    inputs = [
        [1,2,3]
    ]
    for i in inputs:
        print(possible_words(i))
        print()