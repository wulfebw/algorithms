

import bst_revisited as bst

def test_build_and_traversal():
    tree = bst.BST()
    tree.build_complete_tree(4)
    values = tree.inorder_tree_walk()
    print('inorder')
    print(tree.inorder_tree_walk())
    print('preorder')
    print(tree.preorder_tree_walk())
    print('postorder')
    print(tree.postorder_tree_walk())

def test_querying():
    tree = bst.BST()
    tree.build_complete_tree(4)
    print(tree.inorder_tree_walk())
    print(tree.search(7))
    print(tree.search(1))
    print(tree.search(14))
    print(tree.search(30))

    print('\nmin and max')
    print(tree.min())
    print(tree.max())

    print('\nsucc and pred')
    print(tree.search(3).succ())
    print(tree.search(3).pred())
    print(tree.search(11).succ())
    print(tree.search(11).pred())
    print(tree.search(7).succ())
    print(tree.search(14).pred())

def test_delete():
    tree = bst.BST()
    tree.build_complete_tree(4)
    print(tree.inorder_tree_walk())
    print(tree.root)
    print(tree.root.left)
    print(tree.root.right)
    tree.delete_value(7)
    print(tree.root)
    print(tree.root.left)
    print(tree.root.right)
    print(tree.inorder_tree_walk())
    tree.delete_value(8)
    print(tree.root)
    print(tree.inorder_tree_walk())

def test_build_balanced_tree():
    tree = bst.BST()
    values = range(37)
    tree.build_balanced_tree(values)
    # tree.print()
    values = [27, 59, 336, 364, 492, 540, 545, 846, 886, 925, 1087, 1313, 1393, 1421, 1530, 1729, 1873, 2305, 2362, 2567, 2777, 2862, 3058, 3069, 3135, 3367, 3426, 3526, 3750, 3784, 3895, 3926, 3929, 4022, 4043, 4067, 4324, 4370, 4421, 4919, 5011, 5123, 5198, 5211, 5368, 5386, 5434, 5736, 5782, 5788, 5857, 6091, 6124, 6229, 6327, 6413, 6429, 6505, 6649, 6808, 6862, 6915, 6996, 7084, 7178, 7276, 7281, 7373, 7763, 7793, 8042, 8167, 8315, 8335, 8456, 8537, 8690, 8814, 8980, 9170, 9172, 9582, 9802, 9956]
    tree.build_balanced_tree(values)
    tree.print()

def test_k_smallest():
    tree = bst.BST()
    values = range(37)
    tree.build_balanced_tree(values)
    values = tree.k_smallest(5)
    print(values)
    print(len(values))
    values = tree.k_smallest(37)
    print(values)
    print(len(values))


if __name__ == '__main__':
    # test_build_and_traversal()
    # test_querying()
    # test_delete()
    # test_build_balanced_tree()
    test_k_smallest()