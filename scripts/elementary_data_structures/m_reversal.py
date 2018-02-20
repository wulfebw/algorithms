"""
Some different ways to reverse a string. 

The way that uses reversed is the fastest on the data used. The fastest way should be the slicing manner: [::-1]. The reason it's not is because the timing function calls ''.join no matter what (even though it's not necessary with [::-1]).
"""

import time

def reverse_string(string):
    """
    - only iterate half way
    """
    string_len = len(string)
    list_string = list(string)
    end = string_len - 1
    halfway = string_len / 2
    for idx in range(halfway):
        list_string[idx], list_string[end - idx] = list_string[end - idx], list_string[idx]
    return list_string

def reverse_string_generator(string):
    # iterate from len - 1 to 0 backward
    for i in range(len(string) - 1, -1, -1):
        yield string[i]

def reverse_slice(string):
    return string[::-1]

def reverse_reversed(string):
    return reversed(string)

def run(f, iterations):
    strings = ['abcdeasdfasdfasdf', 'abcd', 'ab', 'abcdefg', 'a']
    for i in range(iterations):
        for s in strings:
            ''.join(f(s))

if __name__ == '__main__':
    functions = [reverse_string, reverse_string_generator, reverse_slice, reverse_reversed]
    iterations = 500000
    for f in functions:
        start = time.time()
        run(f, iterations)
        end = time.time()
        print 'function: {}\ttime: {}'.format(f, end - start)


