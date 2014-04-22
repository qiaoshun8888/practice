"""
Algorithm to check if binary_tree is bst
"""
from bst import array2bst

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs.binary_tree import array2tree

def is_bst1(node):
    last = float('-inf')
    for i in node.in_order():
        if i < last:
            return False
        else:
            last = i
    return True

def is_bst2(node):
    """dfs"""
    stack = []
    stack.append(node)
    while stack:
        node = stack.pop()
        if node.left:
            if node.left.data > node.data:
                return False
            stack.append(node.left)
        if node.right:
            if node.right.data < node.data:
                return False
            stack.append(node.right)
    return True

def main():
    node = array2bst([1,2,3,4,5,6,7,8,9])
    print is_bst1(node)
    print is_bst2(node)
    node = array2tree([1,2,3,4,5,6,7,8,9])
    print is_bst1(node)
    print is_bst2(node)


if __name__ == '__main__':
    main()
