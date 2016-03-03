
import collections 
import sys

def print_words(words, idxs):
    prev_cut = 0
    cur_cut = idxs[0]
    while cur_cut != prev_cut:
        print ' '.join(words[prev_cut:cur_cut])
        prev_cut = cur_cut
        cur_cut += idxs[cur_cut]
    print ' '.join(words[cur_cut:])
    print '\n'
        
def find_min_print_cost_and_indices(m, words):
    costs = collections.defaultdict(lambda: sys.maxint)
    idxs = {}

    def space_cost(sidx, eidx):
        num_spaces = eidx - sidx - 1
        total_words_length = sum(len(w) for w in words[sidx:eidx])
        c = m - num_spaces - total_words_length
        if c >= 0:
            return c**3
        else:
            return sys.maxint

    def fits_on_last_line(sidx):
        num_spaces = len(words) - sidx - 1
        total_words_length = sum(len(w) for w in words[sidx:])
        return m >= num_spaces + total_words_length

    def recurse(sidx):
        if costs[sidx] < sys.maxint:
            return costs[sidx]

        if fits_on_last_line(sidx):
            min_cost = 0
            min_idx = 0
        else:
            min_cost = sys.maxint
            min_idx = 0
            cost = sys.maxint
            for idx in range(1, len(words[sidx:]) + 1):
                newline_cost = space_cost(sidx, sidx + idx)
                if newline_cost == sys.maxint:
                    break
                future_cost = recurse(sidx + idx)
                cost = newline_cost + future_cost
                if cost < min_cost:
                    min_cost = cost
                    min_idx = idx

        costs[sidx] = min_cost
        idxs[sidx] = min_idx
        return min_cost

    return costs, recurse(0), idxs

if __name__ == '__main__':

    ###########################

    m = 2
    words = ['a', 'b', 'c']
    costs, min_cost, idxs = find_min_print_cost_and_indices(m, words)
    print 'minimum cost: {}'.format(min_cost)
    print_words(words, idxs)

    ###########################

    m = 5
    words = ['-', '-', '-', '-', '----']
    # greedy solution: 
    # - - -
    # -
    # ----
    # cost: 1^3 + 4^3 + 1^3 == 66 (actually 65 ignoring the last line)

    # optimal solution:
    # - -
    # - -
    # ----
    # cost: 2^3 + 2^3 + 1^3 = 17 (actually 16 ignoring the last line)
    costs, min_cost, idxs = find_min_print_cost_and_indices(m, words)
    print 'minimum cost: {}'.format(min_cost)
    print_words(words, idxs)

    ###########################

    m = 11
    dashes = ['-'] * 6
    words = ['-'] * 6
    words.append(''.join(dashes))
    words.append(''.join(dashes))
    # greedy solution: 
    # 6 * -
    # len_5_dash 
    # len_5_dash
    # cost: 0^3 + 5^3 + 0

    # optimal solution:
    # 4 * -
    # 1 * - + len_5_dash 
    # len_5_dash
    # cost: 0^3 + 3^3
    costs, min_cost, idxs = find_min_print_cost_and_indices(m, words)
    print 'minimum cost: {}'.format(min_cost)
    print_words(words, idxs)

    ###########################

    m = 100
    dashes = ['-'] * 50
    words = ['-'] * 50
    words.append(''.join(dashes))
    words.append(''.join(dashes))

    # greedy solution: 
    # 6 * -
    # len_5_dash 
    # len_5_dash
    # cost: 0^3 + 5^3 + 0

    # optimal solution:
    # 4 * -
    # 1 * - + len_5_dash 
    # len_5_dash
    # cost: 0^3 + 3^3
    costs, min_cost, idxs = find_min_print_cost_and_indices(m, words)
    print 'minimum cost: {}'.format(min_cost)
    print_words(words, idxs)


    ###########################

    m = 100
    dashes = ['-'] * 50
    words = ['-'] * 50
    words.append(''.join(dashes))
    words.append(''.join(dashes))
    dashes = ['--------------'] * 50
    words += dashes

    # greedy solution: 
    # 6 * -
    # len_5_dash 
    # len_5_dash
    # cost: 0^3 + 5^3 + 0

    # optimal solution:
    # 4 * -
    # 1 * - + len_5_dash 
    # len_5_dash
    # cost: 0^3 + 3^3
    costs, min_cost, idxs = find_min_print_cost_and_indices(m, words)
    print 'minimum cost: {}'.format(min_cost)
    print_words(words, idxs)

