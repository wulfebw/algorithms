
class MyQueue(object):
    """
    :description: queue data structure. Uses the keep-an-empty-pos trick to determine how full the buffer is

    :time: enqueue, dequeue, full, empty all O(1) b/c keep track of indicies. Assumes limited space array

    """

    def __init__(self, size=10):
        self.queue = [None] * size
        self.size = size
        self.head = 0
        self.tail = 0

    def enqueue(self, val):
        if self.is_full():
            raise OverflowError('queue is full')
        self.queue[self.tail] = val
        self.tail += 1
        self.tail = self.tail % self.size

    def dequeue(self):
        if self.is_empty():
            raise StopIteration
        val = self.queue[self.head]
        self.head += 1
        self.head = self.head % self.size
        return val

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return self.head == self.tail + 1 % self.size

def run():
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(2)
    ele = q.dequeue()
    result = ele == 1
    print('correct result?: {}'.format(result))
    q.dequeue()
    try:
        q.dequeue()
    except StopIteration as e:
        print('correctly raised exception')

    for i in range(9):
        q.enqueue(i)
    ele = q.dequeue()
    q.enqueue(9)
    result = ele == 0
    print('correct result?: {}'.format(result))
    print('queue should be full?: {}'.format(q.is_full()))


if __name__ == '__main__':
    run()
