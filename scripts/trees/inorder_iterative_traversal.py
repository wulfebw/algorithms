


def inorder_iterative_traversal(r):
    s = []
    while len(s) > 0 or r:

        if r:
            s.append(r)
            r = r.l

        else:
            if len(s) > 0:
                top = s.pop()
                print(top.v)
                r = top.r

if __name__ == '__main__':
    inputs = 