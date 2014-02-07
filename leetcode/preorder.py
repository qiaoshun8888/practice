# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers

    def preorderTraversal(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if hasattr(node, 'visited'):
                res.append(node.val)
            else:

                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                node.visited = True
                stack.append(node)
        return res

