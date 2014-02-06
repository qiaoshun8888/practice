# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers

    def helper(self, root):
        if root:
            if root.left:
                for i in self.helper(root.left):
                    yield i
            if root.right:
                for i in self.helper(root.right):
                    yield i
            yield root

    def postorderTraversal(self, root):
        res = []
        for i in self.helper(root):
            res.append(i.val)
        return res
