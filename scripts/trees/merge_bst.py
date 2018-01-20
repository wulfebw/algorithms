'''
tried a recursive solution, but that didn't work
need to use the stack traversal method 
iterative inorder traversal

so a simple solution is to collect the values in order 
to merge those lists
then to build to bst
this is O(n) time and O(n) space
'''

'''
first solution 
O(n+m) time O(n+m) space
'''

class Node(object):

    def __init__(self, v, l=None, r=None):
        self.data = v
        self.left = l 
        self.right = r

def inorder(r):
    values = []
    if r.left:
        values += inorder(r.left)
    values += [r.data]
    if r.right:
        values += inorder(r.right)

def merge(first, second):
    i1 = 0
    i2 = 0
    result = []
    while i1 < len(first) and i2 < len(second):
        if first[i1] < second[i2]:
            result.append(first[i1])
            i1 += 1
        else:
            result.append(second[i2])
            i2 += 1
    if i1 >= len(first):
        result += second[i2:]
    else:
        result += first[i1:]
    return result

def mergeBST(r1,r2):
    v1 = inorder(r1)
    v2 = inorder(r2)
    v = merge(v1, v2)

'''
second solution: O(n+m) time O(h1 + h2) space
basically perform 2 simultaneous inorder traversals 
'''

def mergeBST(r1,r2):
    s1 = []
    s2 = []

    while len(s2) > 0 or len(s1) > 0 or r1 or r2:

        if r1:
            s1.append(r1)
            r1 = r1.left
        if r2:
            s2.append(r2)
            r2 = r2.left
        if not r1 and not r2:
            if len(s1) > 0 and len(s2) == 0:
                top = s1.pop()
                print(top.data)
                r1 = top.right
            elif len(s1) == 0 and len(s2) > 0:
                top = s2.pop()
                print(top.data)
                r2 = top.right
            elif len(s1) > 0 and len(s2) > 0:
                if s1[-1].data < s2[-1].data:
                    top = s1.pop()
                    print(top.data)
                    r1 = top.right
                else:
                    top = s2.pop()
                    print(top.data)
                    r2 = top.right





