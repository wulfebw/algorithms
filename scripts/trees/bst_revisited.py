'''
Binary Search Tree implementation
What's a bst?
it's a tree consisting of nodes that adhere to the binary search tree property 
which is that for a parent p and left and right children l and r 
l.value <= p.value <= r.value
'''

import collections
import numpy as np
import sys

class Node(object):
    
    def __init__(
            self, 
            value=0, 
            parent=None,
            left=None,
            right=None):
        self.value = value 
        self.parent = parent
        self.left = left 
        self.right = right

    def tree_walk(self, order='inorder'):
        # left
        if self.left:
            left_values = self.left.tree_walk(order=order)
        else:
            left_values = []

        # right
        if self.right:
            right_values = self.right.tree_walk(order=order)
        else:
            right_values = []

        # order them
        if order == 'inorder':
            values = left_values + [self.value] + right_values
        elif order == 'preorder':
            values = [self.value] + left_values + right_values
        else:
            values = left_values + right_values + [self.value]

        return values
         
    def insert(self, z):
        if z.value < self.value:
            if self.left:
                self.left.insert(z)
            else:
                self.left = z
                z.parent = self
        else:
            if self.right:
                self.right.insert(z)
            else:
                self.right = z
                z.parent = self

    def search(self, v):
        if self.value == v:
            return self 
        elif v < self.value:
            if self.left:
                return self.left.search(v)
        else:
            if self.right:
                return self.right.search(v)
        return None

    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self

    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self

    def succ(self):
        # if right tree exists, then minimum of that tree
        if self.right:
            return self.right.min()
        # otherwise, traverse the tree upward, and the first time we move right 
        # the resulting node is the successor
        else:
            y = self.parent
            x = self
            while y.parent and y.right == x:
                x = y 
                y = y.parent
            return y 

    def pred(self):
        # same idea: if there's a left child, then the max of that subtree
        if self.left:
            return self.left.max()
        # otherwise, traverse upward, and when we first turn left, return that node
        else:
            y = self.parent 
            x = self
            while y.parent and y.left == x:
                x = y 
                y = y.parent
            return y 

    def delete(self):

        # one or no children: replace with right child, which is None in no child case
        if not self.left:
            replace = self.right
        elif self.left and not self.right:
            replace = self.left
        # 2 children case
        else:
            # if successor is right child, replace self with that child
            replace = self.succ()
            # if it's not the right child, then need to do some fixing up
            if replace != self.right:
                # parent of succ must be up and to the right
                replace.parent.left = replace.right
            # set the left child of replace to that of self
            replace.left = self.left

        # perform the replacement
        if not self.parent:
            pass
        elif self.value < self.parent.value:
            self.parent.left = replace
        else:
            self.parent.right = replace

        return replace

    def build_balanced_tree(self, values):
        '''
        assumes values are sorted
        if you make this assumption, then you can create the tree like this 
        in O(n) time, 
        but if they aren't already sorted then it takes o(nlgn) time because 
        either you have to sort them, or you can just insert them one by 
        one which takes n * lgn time
        '''
        n = len(values)
        if n == 1:
            self.value = values[0]
        else:
            mid = n // 2
            self.value = values[mid]
            if len(values[:mid]) > 0:
                self.left = Node().build_balanced_tree(values[:mid])
            if len(values[mid+1:]) > 0:
                self.right = Node().build_balanced_tree(values[mid+1:])
        return self

    def k_smallest(self, k):
        if k <= 0:
            return []
        values = []
        if self.left:
            left_values, k = self.left.k_smallest(k)
            values += left_values
        if k > 0:
            k -= 1
            values += [self.value]
        if k > 0 and self.right:
            right_values, k = self.right.k_smallest(k)
            values += right_values
        return values, k

    def __repr__(self):
        return 'Node: value: {}'.format(self.value)

class BST(object):
    
    def __init__(self, root=Node(0)):
        self.root = root

    def inorder_tree_walk(self):
        return self.root.tree_walk('inorder')

    def preorder_tree_walk(self):
        return self.root.tree_walk('preorder')

    def postorder_tree_walk(self):
        return self.root.tree_walk('postorder')

    def insert(self, node):
        self.root.insert(node)

    def search(self, value):
        return self.root.search(value)

    def min(self):
        return self.root.min()

    def max(self):
        return self.root.max()

    def delete_value(self, value):
        node = self.root.search(value)
        replace = node.delete()
        if node == self.root:
            self.root = replace

    def build_complete_tree(self, h):
        '''
        does not yield a balanced tree, revisit
        '''
        n_nodes = 2 ** h - 1
        mid = n_nodes // 2
        self.root = Node(mid)
        for v in range(n_nodes):
            if v != mid:
                self.root.insert(Node(v))

    def build_balanced_tree(self, values):
        values = list(sorted(values))
        self.root.build_balanced_tree(values)

    def k_smallest(self, k):
        '''
        truncated inorder traversal
        '''
        values, _ = self.root.k_smallest(k)
        return values

    def bfs(self):
        q = collections.deque()
        q.appendleft(self.root)
        seen = []
        while len(q) > 0:
            cur = q.pop()
            seen.append(cur)
            if cur.left:
                q.appendleft(cur.left)
            if cur.right:
                q.appendleft(cur.right)
        return seen

    def print(self):
        nodes = self.bfs()
        h = 1
        for cur, nxt in zip(nodes, nodes[1:]):
            if nxt.value < cur.value:
                h += 1
        
        for cur, nxt in zip(nodes, nodes[1:]):
            n_space = 2 ** (h - 1)
            space = ' ' * n_space
            sys.stdout.write('{}{}'.format(space, cur.value))
            if nxt.value < cur.value:
                h -= 1
                print()
        print()



