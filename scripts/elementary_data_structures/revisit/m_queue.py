
class SimpleQueue(object):

    def __init__(self, n):
        self.q = [None] * (n + 1)
        self.head = 0 # next pop 
        self.tail = 0 # next insert

    def enqueue(self, v):
        self.q[self.tail] = v
        if self.tail == len(self.q) - 1:
            self.tail = 0 
        else:
            self.tail += 1

    def dequeue(self):
        x = self.q[self.head]
        if self.head == len(self.q) - 1:
            self.head = 0 
        else:
            self.head += 1
        return x

class Queue(object):

    def __init__(self, n_init=10, grow_factor=2):
        self.q = [None] * n_init
        self.head = 0 # next pop
        self.tail = 0 # next insert
        self.size = 0
        self.grow_factor = grow_factor

    def _grow(self):
        n = len(self.q)
        new = [None] * n * self.grow_factor
        head = self.head 
        tail = self.tail
        i = 0
        while head != tail:
            new[i] = self.q[head]
            head = (head + 1) % n
            i += 1
        self.head = 0 
        self.tail = i
        self.q = new

    def enqueue(self, v):
        if self.size == len(self.q) - 1:
            self._grow()

        self.size += 1
        self.q[self.tail] = v
        self.tail = (self.tail + 1) % len(self.q)

    def dequeue(self):
        if self.size == 0:
            raise StopIteration

        self.size -= 1 
        x = self.q[self.head]
        self.head = (self.head + 1) % len(self.q)
        return x

if __name__ == '__main__':

    q = Queue(n_init=2)
    for i in range(10):
        q.enqueue(i)
    print(q.q)

    for _ in range(10):
        print(q.dequeue())
    print(q.q)

    for i in range(10, 10 + 10):
        q.enqueue(i)
    print(q.q)

    for i in range(10, 10 + 10):
        q.enqueue(i)
    print(q.q)
