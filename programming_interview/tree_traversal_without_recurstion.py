
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs.binary_tree import array2tree


def in_order(root):
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        if not hasattr(node, 'visit'):
            node.visit = True
            if node.right:
                stack.append(node.right)
            stack.append(node)
            if node.left:
                stack.append(node.left)
        else:
            print node.data,


def pre_order(root):
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        if not hasattr(node, 'visit'):
            node.visit = True
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            stack.append(node)
        else:
            print node.data,


def post_order(root):
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        if not hasattr(node, 'visit'):
            node.visit = True
            stack.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        else:
            print node.data,


if __name__ == '__main__':
    node = array2tree(range(14))
    for i in node.post_order():
        print i,
    print ''
    node = array2tree(range(14))
    post_order(node)
