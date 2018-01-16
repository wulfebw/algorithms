

def lcss(arr):
    best, cur = 0, 0
    for v in arr:
        cur += v
        cur = max(0, cur)
        if cur > best:
            best = cur 
    return best

if __name__ == '__main__':
    inputs = [
        [-1,2,3,4,-6,-7,8,9],
        [1,2,3,-5],
    ]
    expect = [
        17,
        6
    ]
    for (i,e) in zip(inputs, expect):
        print(e)
        print(lcss(i))
        print()