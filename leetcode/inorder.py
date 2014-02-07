# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers

    def inorderTraversal(self, root):

        def helper(root):
            if root:
                for i in helper(root.left):
                    yield i
                yield root
                for i in helper(root.right):
                    yield i
        res = []
        for i in helper(root):
            res.append(i.val)
        return res
