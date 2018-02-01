



class DirectAddressTable(object):
    """
    :description: a table where the values stored are the keys

    :time: O(1) for insert, retrieve, delete
            
    """

    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def insert(self, k, v):
        self.table[k] = v

    def get(self, k):
        return self.table[k]

    def delete(self, k):
        self.table[k] = None

    def find_max(self):
        """
        :time: O(n) 
        """
        return max(self.table)


class HashTable(object):
    """
    :description: hash table handling collisions through chaining

    :time: O(1 + alpha) average case for get, delete. O(1) time for set.
            Defining n = total elements inserted, m = number of slots, alpha = n / m = essentially the average number of elements for each hash location and therefore the average number of elements in each linked list or array implementing chaining. It takes 1 operation to index into the list plus on average alpha operations to find an element. This holds even when the retrieval is successful (which is notable because the likelihood of a search taking place on a given list depends on the size of the list)

            The O(1 + alpha)


            O(1) worst case for set. O(n) worst case for get. O(n) worst case for delete.
    :space: O(1) ? not sure. You have to store the stuff but I think that just counts as O(1)
    """

    def __init__(self, size):
        self.table = [[]] * size
        self.size = size

    def set(self, k, v):
        self.table[self.hash(k)].append((k,v))

    def get(self, k):
        for (stored_k, v) in self.table[self.hash(k)]:
            if stored_k == k:
                return v
        return None

    def delete(self, k):
        remove_idx = None
        for idx, (stored_k, v) in enumerate(self.table[self.hash(k)]):
            if stored_k == k:
                remove_idx = idx
                break
        del self.table[self.hash(k)][remove_idx]

    def hash(self, k):
        return k % self.size


def run():
    h = HashTable(size=17)
    k = 1001020120314702
    v = 'HI!'
    h.set(k,v)
    result = h.get(k) == 'HI!'
    print 'correctly retrieved value?: {}'.format(result)
    h.delete(k)
    result = h.get(k) == None
    print 'correctly removed value?: {}'.format(result)
    h.set(1, 'first')
    h.set(18, 'second')
    result = h.get(18) == 'second'
    print 'correctly retrieved chained value?: {}'.format(result)


if __name__ == '__main__':
    run()

"""
:additional notes:
- prove that if you store n keys in m slots, then a universe of keys size |U| can result in at least O(n) worst case search time
    - |U| > n * m => |U| / m > n => there exist for each slot at least n distinct keys
- 
"""