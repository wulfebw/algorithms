
class RedBlackNode(object):

    def __init__(self, key, right=None, left=None, parent=None, color=True):
        self.key = key 
        self.right = right
        self.left = left 
        self.parent = parent
        self.color = color # red = True, black = False

    def insert(self, z):
        