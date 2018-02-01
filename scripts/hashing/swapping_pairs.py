'''
this reduces to the problem of finding two elements, one in each array,
that sum to a desired value
'''

def swap_pairs(a1, a2):
    s1 = sum(a1)
    s2 = sum(a2)
    d = (s1 - s2) // 2

    vals = set()
    for v in a1:
        vals.add(-(d - v))
    for v in a2:
        if v in vals:
            return True
    return False


if __name__ == '__main__':
    inputs = [
        ([4,1,2,1,1,2],[3,6,3,3]),
        ([5,7,4,6],[1,2,3,8])
    ]
    for i in inputs:
        print(swap_pairs(*i))
