

def remove_duplicates(a):
    idxs_to_remove = set()
    n = len(a)
    for i,j in zip(range(n), range(1,n)):
        if a[i] == a[j]:
            idxs_to_remove.add(i)
            idxs_to_remove.add(j)
    if len(idxs_to_remove) == 0:
        return a
    else:
        idxs_to_keep = set(range(n)).difference(idxs_to_remove)
        newstring = ''.join([a[i] for i in idxs_to_keep])
        return remove_duplicates(newstring)


if __name__ == '__main__':
    inputs = [
        'geeksforgeek',
        'aaaaaaaaaaaaaa',
        'aaaaaabbbbb',
        'ababababa',
        'aabaaccaa'
    ]
    expect = [
        'gksforgk',
        '',
        '',
        'ababababa',
        'b'
    ]

    for (i,e) in zip(inputs, expect):
        print(e)
        print(remove_duplicates(i))
        print()