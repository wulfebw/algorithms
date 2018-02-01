'''
the problem is to determine if you can pair up the values in an array 
so that their sum modulo k is 0 

count the number of modulo k values in the array 
then see if you can pair up those values
'''


import collections

def check_for_pairs(a, k):

    ctr = collections.defaultdict(list)
    for v in a:
        ctr[v % k] += [v]

    if len(ctr[0]) % 2 == 1:
        return False

    keys = list(range(1, k))
    for s, e in zip(keys, keys[::-1]):
        if len(ctr[s]) != len(ctr[e]):
            return False
    return True

if __name__ == '__main__':

    # inputs = [
    #     ([9,7,5,3], 6),
    #     ([91,74,66,48], 10)
    # ]

    x = '''76 37 91 52 62 20 6 85 34 40 73 100 82 52 71 89 32 48 51 26 93 25 69 13 23 88 34 63 56 38 9 84 74 99 35 35 18 92 72 4 83 44 55 64 95 26 5 26 25 55 51 17 31 71 81 53 58 66 68 66 4 76 1 29 26 87 16 95 30 87 98 12 82 5 28 76 30 32 54 54 38 56 22 21 27 3 25 36 68 92 53 23 19 5'''
    x = [int(v) for v in x.split()]

    res, ctr = check_for_pairs(x, 3)
    print(res)
    print('lengths: {}'.format(len(x)))
    print(sum(len(v) for v in ctr.values()))