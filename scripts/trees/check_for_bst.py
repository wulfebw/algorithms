

def inorder(r):
    values = []
    if r.left:
        values += inorder(r.left)
    values += [r.data]
    if r.right:
        values += inorder(r.right)
    return values

def isBST(root):
    values = inorder(root)
    for i,j in zip(values, values[1:]):
        if i >= j:
            return False
    return True

'''
check for bst by collecting items in order and checking that they are 
sorted, which is O(n)

can you do better than that?
no because for you to check if it's valid you have to look at every item
'''