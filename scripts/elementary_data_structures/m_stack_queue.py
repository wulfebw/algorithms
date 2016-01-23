
from m_stack import MyStack
from m_queue import MyQueue

class MyQueueStack(object):
    
    def __init__(self, size=10):
        self.in_queue = MyQueue(size=size)
        self.out_queue = MyQueue(size=size)

    def push(self, val):
        self.in_queue.enqueue(val)
        while not self.out_queue.is_empty():
            self.in_queue.enqueue(self.out_queue.dequeue())
        self.in_queue, self.out_queue = self.out_queue, self.in_queue

    def pop(self):
        self.out_queue.dequeue()

    def is_empty(self):
        return self.in_queue.is_empty() and self.out_queue.is_empty()

    def is_full(self):
        return self.in_queue.is_full() or self.out_queue.is_full()


class MyStackQueue(object):
    """
    :description: queue implemented with stacks

    :time: O(1) amortized time, O(n) worst case though. This is because each element will be enqueued and dequeued twice. If you add all elements to the push stack first and then pop them, then you can get O(n) time on dequeue, though enqueue will always be O(1)
    :space: O(n) because need each stack to hold entirety of queue
    """
    
    def __init__(self, size=10):
        self.push_stack = MyStack(size=size)
        self.pop_stack = MyStack(size=size)

    def enqueue(self, val):
        if self.is_full():
            raise OverflowError

        self.push_stack.push(val)

    def dequeue(self):
        if self.is_empty():
            raise StopIteration

        if self.pop_stack.is_empty():
            while not self.push_stack.is_empty():
                self.pop_stack.push(self.push_stack.pop())
        return self.pop_stack.pop()

    def is_empty(self):
        return self.push_stack.is_empty() and self.pop_stack.is_empty()

    def is_full(self):
        return self.push_stack.is_full() or self.pop_stack.is_full()


def run_queue():
    q = MyStackQueue()
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

def run_stack():
    s = MyStack()
    s.push(5)
    v = s.pop()
    result = v == 5
    print("valid push/pop?: {}".format(result))
    try:
        s.pop()
    except StopIteration as e:
        print('correct exception throw')


if __name__ == '__main__':
    run_stack()