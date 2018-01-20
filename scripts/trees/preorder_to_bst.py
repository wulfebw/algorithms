
class Node(object):

    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l 
        self.r = r

def preorder(r):
    print(r.v)
    if r.l:
        preorder(r.l)
    if r.r:
        preorder(r.r)

def preorder2bst(a):
    '''
    The idea is that you store everything in a stack as you go 
    when you run into something smaller than the top of the stack 
    you know for sure this is the left child of the top element on the stack 
    so you set the left child on the current top, and push the new node on the stack 
    when you get to an element larger than the current top you know that the 
    element _above_ the first element in the stack that's larger than the new 
    element is the parent of the new element
    '''
    root = Node(a[0])
    s = [root]
    for v in a[1:]:
        n = Node(v)

        if s[-1].v > n.v:
            s[-1].l = n
            s.append(n)

        else:
            prev = s[-1]
            while len(s) > 0 and s[-1].v < n.v:
                prev = s.pop()
            prev.r = n 
            s.append(n)

    return root
    
def preorder2leaves(a):
    '''
    same idea as preorder2bst, except tracking different information
    '''
    root = Node(a[0])
    s = [root]
    leaves = []
    for v in a[1:]:
        n = Node(v)

        if s[-1].v > n.v:
            s[-1].l = n
            s.append(n)

        else:
            prev = s[-1]
            while len(s) > 0 and s[-1].v < n.v:
                prev = s.pop()
                leaves.append(prev)
            leaves.pop()
            prev.r = n 
            s.append(n)

    leaves.extend(s)        
    return leaves

def test_preorder2bst():
    inputs = [
        [10,5,1,7,40,50],
    ]
    for i in inputs:
        r = preorder2bst(i)
        preorder(r)

def test_preorder2leaves():
    inputs = [
        [10,5,1,7,40,50],
    ]
    for i in inputs:
        leaves = preorder2leaves(i)
        print([l.v for l in leaves])

if __name__ == '__main__':
    test_preorder2bst()
    test_preorder2leaves()