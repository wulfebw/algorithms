
def mygcd(n, m):
    while m: 
        n, m = m, n%m
    return n

def find_squares(n, m):
    s = mygcd(n, m)
    return int(n/s * m/s), s

if __name__ == '__main__':
    inputs = [
        (7,14),
        (9,12),
        (2,8),
    ]
    expect = [
        (2, 7),
        (12,3),
        (4,2)
    ]

    for (i,e) in zip(inputs, expect):
        print(e)
        print(find_squares(*i))
        print()