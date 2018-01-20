


def add_spaces(a):
    '''
    recurrence relation? 
    so for a string of length 5, this function gets called 5 times
    each time it is called it iterates over all the possible suffixes twice
    the number of possible suffixes is 2^(n-1)
    so I'd say the complexity is O(2^n)
    '''
    print('here')
    if len(a) <= 1:
        return a
    else:
        suffixes = add_spaces(a[1:])
        strings = [a[0] + ' ' + v for v in suffixes]
        strings += [a[0] + v for v in suffixes]
        return strings

if __name__ == '__main__':
    inputs = [
        # 'abc',
        'abcde'
    ]
    for i in inputs:
        print(add_spaces(i))