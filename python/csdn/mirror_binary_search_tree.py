"""
# 15
mirror a binary search tree
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ch4 import bst


def mirror(root):
    if root.left:
        mirror(root.left)
    if root.right:
        mirror(root.right)
    root.left, root.right = root.right, root.left
    return root


def main():
    root = bst.array2bst([1, 2, 3, 4, 5, 6, 7])
    for i in root:
        print i.data,
    print ""
    root = mirror(root)
    for i in root:
        print i.data,


if __name__ == '__main__':
    main()
