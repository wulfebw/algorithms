
import numpy as np
import time

def find_largest_string_sort(data):
    """
    O(nlgn) (assuming this is correct)
    is it correct?
    the largest possible number will clearly have the largest digit at its start
    because it will be the same length no matter what
    so it is therefore just a question of which numbers have the largest 
    starting digits
    so sure it seems correct
    """
    sorted_data = sorted(data, reverse=True)
    return ''.join(sorted_data)

def find_largest_radix_sort(data):
    """
    O(nlgn) also because the bins have to contain a constant
    number of elements and they don't
    if those assumptions hold then you might be able to do it though
    """
    bins = [[] for _ in range(100)]
    for v in data:
        bins[99 - int(v[:2])].append(v)
    
    for idx, b in enumerate(bins):
        bins[idx] = sorted(b, reverse=True)

    return ''.join(''.join(v for v in bin) for bin in bins)

def time_f(f, data, num_runs=10):
    st = time.time()
    for r in range(num_runs):
        f(data)
    et = time.time()
    print(et - st)

if __name__ == '__main__':
    data = ['9','10','11','12']
    data = ['0000009','101010','9999']
    data = [str(v) for v in np.random.randint(low=0, high=100000000, size=1000000)]
    largest_radix_sort = find_largest_radix_sort(data)
    largest_string_sort = find_largest_string_sort(data)
 
    assert largest_radix_sort == largest_string_sort
    
    time_f(find_largest_radix_sort, data)
    time_f(find_largest_string_sort, data)
