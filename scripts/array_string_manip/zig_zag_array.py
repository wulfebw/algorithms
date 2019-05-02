

def zig_zag_naive(a):
    a.sort()
    n = len(a)
    for i in range(1, n - 1, 2):
        a[i], a[i+1] = a[i+1], a[i]
    return a

def zig_zag(a):
    i = 0
    n = len(a)
    while i < n - 1:
        # if i even then this value should be less than surrounding
        if i % 2 == 0:
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
            else:
                i += 1
        # if i odd then greater than surrounding
        else:
            if a[i] < a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
            else: 
                i += 1

        return a

def check_zig_zag(a):
    for i, (v1, v2) in enumerate(zip(a, a[1:])):
        if i % 2 == 0:
            if v1 > v2:
                return False
        else:
            if v2 > v1:
                return False
    return True
        
if __name__ == '__main__':
    inputs = [
        [4,3,7,8,6,2,1],
        [1,4,3,2]
    ]

    for i in inputs:
        output = zig_zag(i)
        print(output)
        print(check_zig_zag(output))