
import sys

class Node(object):

    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l 
        self.r = r

def inorder(r):
    if r.l:
        inorder(r.l)
    sys.stdout.write('{} '.format(r.v))
    if r.r:
        inorder(r.r)

def postorder(r):
    if r.l:
        postorder(r.l)
    if r.r:
        postorder(r.r)
    sys.stdout.write('{} '.format(r.v))

def postorder2bst(a):
    '''
    O(n) runtime, same logic as preorder2bst but reversed
    i.e., reverse the list order
    and also flip the comaprisons from < to >

    not sure if this is correct really
    '''
    a = a[::-1]
    root = Node(a[0])
    s = [root]
    for v in a[1:]:
        n = Node(v)

        if n.v > s[-1].v:
            s[-1].r = n
            s.append(n)
        else:
            prev = s[-1]
            while len(s) > 0 and s[-1].v > n.v:
                prev = s.pop()
            prev.l = n 
            s.append(n)
    return root

if __name__ == '__main__':

    inputs = [
        [4,5.5,6.75,6.5,6,5,8,10,9,7]
    ]
    for i in inputs:
        root = postorder2bst(i)
        print(' '.join(str(v) for v in i))
        postorder(root)
        print()
        inorder(root)
        
