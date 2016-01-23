

class MyDeque(object):
    """
    :description: double ended data structure. Implemented by keeping a front pointer to an open position in the front of the array and a back pointer to an open position at the back of the array. Insert at either end by just placing a value at the back or front. Remove from from by decrementing and indexing. Remove from back back incrementing and indexing. 

    :time: push/pop back/front all in O(1) time

    """

    def __init__(self, size=10):
        self.d = [None] * size
        self.size = size
        self.front = 1
        self.back = 0

    def push_front(self, val):
        if self.is_full():
            raise OverflowError

        self.d[self.front] = val
        self.front = (self.front + 1) % self.size
            
    def pop_front(self):
        if self.is_empty():
            raise StopIteration

        self.front = (self.front - 1) % self.size
        return self.d[self.front]

    def push_back(self, val):
        if self.is_full():
            raise OverflowError

        self.d[self.back] = val
        self.back = (self.back - 1) % self.size

    def pop_back(self):
        if self.is_empty():
            raise StopIteration
        
        self.back = (self.back + 1) % self.size
        return self.d[self.back]

    def is_empty(self):
        return (self.front - 1) % self.size == self.back

    def is_full(self):
        return self.front == self.back

def run():
    d = MyDeque(size=3)
    d.push_front(1)
    ele = d.pop_front()
    result = ele == 1
    print('correct result?: {}'.format(result))
    d.push_back(2)
    ele = d.pop_back()
    result = ele == 2
    print('correct result?: {}'.format(result))
    d.push_front(1)
    d.push_front(2)
    ele = d.pop_back()
    result = ele == 1
    print('correct result?: {}'.format(result))
    d.push_front(1)
    result = False
    try:
        d.push_back(1)
    except OverflowError as e:
        result = True
    print('correct result?: {}'.format(result))
    ele = d.pop_front()
    result = ele == 1
    print('correct result?: {}'.format(result))
    ele = d.pop_back()
    result = ele == 2
    print('correct result?: {}'.format(result))

def test_is_full():
    d = MyDeque(3)
    d.push_front(1)
    d.push_front(2)
    result = False
    try:
        d.push_front(3)
    except OverflowError as e:
        result = True
    print 'push_front is full works is: {}'.format(result)
    result = False
    try:
        d.push_back(3)
    except OverflowError as e:
        result = True
    print 'push_back is full works is: {}'.format(result)

if __name__ == '__main__':
    run()
    test_is_full()
