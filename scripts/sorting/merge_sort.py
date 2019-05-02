
import utils

def merge(a, s, mid, e):
    x = []
    i = s 
    j = mid + 1
    while i <= mid and j <= e:
        if a[i] < a[j]:
            x.append(a[i])
            i += 1 
        else:
            x.append(a[j])
            j += 1

    if i <= mid:
        x.extend(a[i:mid+1])
    else:
        x.extend(a[j:e+1])
    a[s:e+1] = x
    return a

def merge_sort_helper(a, s, e):
    if (e - s) < 1:
        return a
    else:
        mid = (s + e) // 2
        merge_sort_helper(a, s, mid)
        merge_sort_helper(a, mid + 1, e)
        merge(a, s, mid, e)
    return a

def merge_sort(a):
    '''
    - recursion is T(n) = 2*T(n/2) + O(n)
    - which is Θ(nlgn)
    - you can also logic to it by saying 
    - at each level of the recursion, we perform O(n) work in merging
    - so how many levels are there? we divide by 2 each time so there are lgn levels
    - so Θ(nlgn)

    additional notes
    - merge sort is used for sorting stuff when it's too big to fit in memory 
    - it's called external merge sort 
    - say you have B+1 buffer pages 
    - first, you load the data in in B+1 segments and sort those in memory using 
    something like quicksort, but it doesn't matter 
    - next, you end up with N / (B+1) runs of sorted pages 
    - to then sort these you do a B-way merge to merge them 
        + basically, load B of the runs into memory one page at a time into each of the B slots in memory 
        + then sort these in memory into output page 
        + each B-way merge merges B runs 
    - so after lg_B merges you'll have merged everything
    '''
    return merge_sort_helper(a, 0, len(a) - 1)

if __name__ == '__main__':
    utils.test_sorting_algorithm(merge_sort)