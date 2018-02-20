
class Stack(object):

    def __init__(self):
        self.s = []

    def pop(self):
        return self.s.pop()

    def push(self, v):
        self.s.append(v)

    def top(self):
        if len(self.s) == 0:
            return None
        else:
            return self.s[-1]

if __name__ == '__main__':

    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.top())