
def iterative_swap(a):
    for i in range(1, n//2, 2):
        j = n // 2 + i - 1
        a[i], a[j] = a[j], a[i]
    return a








if __name__ == '__main__':
    inputs = [
        [1,1,1,1,1,2,2,2,2,2],
        [1,2,3,4,5,6,7,8],
    ]
    expect = [
        [1,2,1,2,1,2,1,2,1,2],
        [1,5,3,7,2,6,4,8]
    ]

    for (i,e) in zip(inputs, expect):
        print(e)
        print(iterative_swap(i))
        print()