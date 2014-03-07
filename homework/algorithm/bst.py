class TreeNode():

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bst(listA):
    length = len(listA)
    if length == 0:  # base case None
        return None
    n, height = 1, 0
    while length >= n:  # get the height
        n = n << 1
        height += 1
    if len(listA) >= 3 * 2 ** (height - 2) - 1:  # check node number
        mid = 2 ** (height - 1) - 1  # left can be full
    else:
        mid = -2 ** (height - 2)  # right should be full
    root = TreeNode(listA[mid])  # root node
    root.left = bst(listA[:mid])  # recursion
    root.right = bst(listA[mid + 1:])  # recursion
    return root

if __name__ == '__main__':
    root = bst([1, 2])
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            queue.append(node.left)
            queue.append(node.right)
            print node.val
