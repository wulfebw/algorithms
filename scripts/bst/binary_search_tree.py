import numpy as np

class Node(object):

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def insert(self, element):
        if element <= self.value:
            if self.left is None:
                self.left = Node(element)
            else:
                self.left.insert(element)
        else:
            if self.right is None:
                self.right = Node(element)
            else:
                self.right.insert(element)

    def inorder_walk(self):
        if self.left is not None:
            self.left.inorder_walk()

        print self.value,

        if self.right is not None:
            self.right.inorder_walk() 

    def preorder_walk(self):
        print self.value,

        if self.left is not None:
            self.left.preorder_walk()
        
        if self.right is not None:
            self.right.preorder_walk() 

    def postorder_walk(self):
        if self.left is not None:
            self.left.postorder_walk()

        if self.right is not None:
            self.right.postorder_walk()

        print self.value,

    def search(self, value):
        if self.value == value:
            return self

        elif self.value > value and self.left is not None:
            return self.left.search(value)

        elif self.right is not None:
            return self.right.search(value)

        else:
            return None

    def maximum(self):
        if self.right is None:
            return self.value
        else:
            return self.right.maximum()

    def minimum(self):
        if self.left is None:
            return self.value
        else:
            return self.left.minimum()

    def delete(self, value):
        pass

class BST(object):

    def __init__(self, root):
        self.root = root

    def tree_insert(self, element):
        self.root.insert(element)

    def inorder_tree_walk(self):
        print '\n'
        self.root.inorder_walk()
        print '\n'

    def preorder_tree_walk(self):
        print '\n'
        self.root.preorder_walk()
        print '\n'

    def postorder_tree_walk(self):
        print '\n'
        self.root.postorder_walk()
        print '\n'

    def tree_search(self, value):
        return self.root.search(value)

    def tree_min(self):
        return self.root.minimum()

    def tree_max(self):
        return self.root.maximum()

    def tree_delete(self, value):
        self.root.delete(value)

    def tree_succ(self):
        pass

    def tree_pred(self):
        pass

    def tree_delete(self, value):
        pass

    @classmethod
    def from_list(cls, lst):
        if len(lst) < 1:
            raise ValueError

        root = Node(lst[0])
        for element in lst[1:]:
            root.insert(element)
        return cls(root)

if __name__ == '__main__':
    
    arr = np.random.permutation([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7])
    bst = BST.from_list(arr)
    bst.inorder_tree_walk()
    bst.preorder_tree_walk()
    bst.postorder_tree_walk()
    node = bst.tree_search(10)
    if node is not None:
        print node.value
    else:
        print 'not found'
    print bst.tree_max()
    print bst.tree_min()


