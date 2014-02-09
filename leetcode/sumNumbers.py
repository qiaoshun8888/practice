# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer

    def sumNumbers(self, root):
        if not root:
            return 0

        result = 0
        stack = [(root, root.val)]
        while stack:
            node, val, depth = stack.pop()
            if not node.left and not node.right:
                result += val
            else:
                if node.left:
                    stack.append((node.left, val * 10 + node.left.val))
                if node.right:
                    stack.append((node.right, val * 10 + node.right.val))
        return result
