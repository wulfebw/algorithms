import utils

def selection_sort(a):
    '''
    analysis
    lower bound: O(n^2) b/c choose(n,2) argument
    upper bound: Ω(n^2) b/c same argument
    therefore: θ(n^2)
    '''
    n = len(a)
    for i in range(n - 1):
        smallest = a[i]
        smallest_idx = i
        for j in range(i + 1, n):
            if a[j] < smallest:
                smallest = a[j]
                smallest_idx = j

        a[smallest_idx], a[i] = a[i], a[smallest_idx]
    return a

if __name__ == '__main__':
    utils.test_sorting_algorithm(selection_sort)