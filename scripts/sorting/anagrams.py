
import collections
import numpy as np

def find_anagrams_naive(data):
    sorted_data = []
    for d in data:
        sorted_data.append(sorted(d))

    for i, d in enumerate(sorted_data):
        for j, o in enumerate(sorted_data):
            if i != j and d == o:
                print data[i]

def find_anagrams(data):
    counts = collections.defaultdict(int)
    sorted_data = []
    for value in data:
        sorted_value = tuple(sorted(value))
        counts[sorted_value] += 1
        sorted_data.append(sorted_value)

    anagrams = []
    for (v, sv) in zip(data, sorted_data):
        if counts[sv] > 1:
            anagrams.append(v)
    return anagrams

def generate_data(num_samples):
    return [str(v) for v in np.random.randint(
        low=0, high=100, size=num_samples)]

if __name__ == '__main__':
    # data = ['asdf', 'fdsa', '1']
    data = generate_data(500)
    anagrams = find_anagrams(data)
    print len(anagrams)