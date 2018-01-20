

def find_position(n, k):
    '''
    this is something like an 
    O(n * ?)
    there's a O(n) recursive solution though
    '''
    it = -1
    a = list(range(1,n+1))
    while len(a) > 1:
        it = (it + k) % len(a)
        del a[it]
        it -= 1
    return a[0]

if __name__ == '__main__':
    inputs = [
    (8,2),
    (5,2),
    (4,4)
    ]
    expect = [
    1,
    3,
    2
    ]
    for (i,e) in zip(inputs,expect):
        print(e)
        print(find_position(*i))
        print()