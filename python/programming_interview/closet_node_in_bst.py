import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ch4.bst import array2bst


def closest_node(root, x):
    def bst_find(root, x):
        if not root:
            return None
        else:
            if x == root.data:
                return root
            elif x > root.data:
                return bst_find(root.right, x)
            else:
                return bst_find(root.left, x)

    node = bst_find(root, x)
    n1 = node.left
    while n1.right:
        n1 = n1.right
    # print n1.data, 'n1'
    n2 = node.right
    while n2.left:
        n2 = n2.left
    # print n2.data, 'n2'

    if x - n1.data > n2.data - x:
        return n2.data
    else:
        return n1.data

if __name__ == '__main__':
    root = array2bst([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 16, 17, 18])
    for i in root:
        print i.data
    print closest_node(root, 13)
