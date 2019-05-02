#!/bin/python3

import sys

def count_changes(a):
    c = 0
    s = 0 
    e = len(a) - 1
    while s < e:
        if a[s] != a[e]:
            c += 1
        s += 1
        e -= 1
    return c

def convert_to_palindrome(a):
    a = [int(v) for v in a]
    n = len(a)
    changed = [False for _ in range(n)]
    s = 0 
    e = n - 1
    while s < e:
        if a[s] != a[e]:
            if a[s] > a[e]:
                a[e] = a[s]
                changed[e] = True
            else:
                a[s] = a[e]
                changed[s] = True
        s += 1
        e -= 1
    return a, changed

def set_to_9(a, k, changed):
    n = len(a)
    s = 0
    e = n - 1
    while s < e and k > 0:
        if a[s] != 9:
            if k == 1 and not(changed[s] or changed[e]):
                break
            a[s] = 9
            a[e] = 9
            k -= 2
            if changed[s] or changed[e]:
                k += 1
    return a
    
def richieRich(s, n, k):
    n_changes = count_changes(s)
    if n_changes > k:
        return -1
    s, changed = convert_to_palindrome(s)
    k = k - sum(changed)
    s = set_to_9(s, k, changed)
    return ''.join([str(v) for v in s])
    
    

n,k = [int(v) for v in input().strip().split()]
s = input().strip()
result = richieRich(s, n, k)
print(result)
