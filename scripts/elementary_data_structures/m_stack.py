

class MyStack(object):
    """
    :description: stack data structure. self.top holds the index of the last item to be added or 0 if there is none.

    :time: O(1) for push, pop, is_empty. The reason being that we keep track of the location of the position to add and the position to take from in the array

    """

    def __init__(self, size=100):
        self.stack = []
        self.top = 0
        self.size = size

    def push(self, val):
        if self.is_full():
            raise OverflowError

        self.stack.append(val)
        self.top += 1

    def pop(self):
        if self.top == 0:
            raise StopIteration
        
        ele = self.stack[self.top - 1]
        self.top -= 1
        return ele

    def is_empty(self):
        return self.top == 0

    def is_full(self):
        return self.top + 1 == self.size

def run():
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
    run()
