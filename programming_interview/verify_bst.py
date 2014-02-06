'''
1. in-order sorted
2. recursive
'''


def is_bst(root):
    last = float('-inf')
    for i in root.in_order():
        if i <= last:
            return False
        last = i


def is_bst2(root):
    if not root:
        return True
    if root.left:
        if not is_bst2(root.left):
            return False
    if root.right:
        if not is_bst2(rott.right):
            return False
    if root.left:
        if root.data < root.left.data:
            return False
    if root.right:
        if root.data > root.right.data:
            return False
    return True
