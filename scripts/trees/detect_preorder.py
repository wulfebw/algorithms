'''
how can you tell if a printed output is the result of an inorder traversal?
if the values are nondecreasing

what about preorder? much harder
'''

def check_inorder(a):
    for i,j in zip(a,a[1:]):
        if i>j:
            return False
    return True