

def stretch(lst, n, size):

    if len(lst) < size * n:
        lst = lst + [None] * 2 * len(lst)

    for i, j in zip(range(size - 1, -1, -1), range((size - 1) * n, -1, -n)):
        lst[j:j+n] = [lst[i]] * n

    return lst 

if __name__ == '__main__':
    lst = [16,7,4,4,24,11,None,None,None]
    n = 3
    size = 6
    print(stretch(lst, n, size))

