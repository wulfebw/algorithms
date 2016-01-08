"""
:keywords: probability, biased, random
"""

import copy
import random

import numpy as np

def random_permutation_priority(arr):
    """
    :description: randomly permute array by assigning each element a random priority and sorting by priority

    :time: O(nlogn) - sorting being the bottleneck
    :space: O(n)
    """
    priorities = []
    for val in arr:
        priorities.append((val, random.random() ** 3)) # increase uniqueness likelihood

    permuted = sorted(priorities, key=lambda (val, p): p)
    arr = [v for v,p in permuted]
    return arr

def random_permutation_swap(arr):
    """
    :description: rand permute via swapping

    :time: O(n)
    :space: O(1)
    """
    size = len(arr)
    for idx, val in enumerate(arr):
        rand = random.randint(idx + 1, size)
        arr[idx], arr[size - rand] =  arr[size - rand], arr[idx]
    return arr

if __name__ == '__main__':
    arr = np.arange(50)
    rand = np.array(random_permutation_swap(arr))
    print rand
