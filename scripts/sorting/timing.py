
from context_timer import ContextTimer

import insertion_sort
import merge_sort
import quick_sort
import selection_sort
import utils

if __name__ == '__main__':
    algos = [
        insertion_sort.insertion_sort,
        merge_sort.merge_sort,
        quick_sort.quick_sort,
        selection_sort.selection_sort,
    ]
    for algo in algos:
        print(algo)
        with ContextTimer():
            utils.test_sorting_algorithm(algo)