# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers

    def postorderTraversal(self, root):

        def helper(root):
            if root:
                if root.left:
                    for i in helper(root.left):
                        yield i
                if root.right:
                    for i in helper(root.right):
                        yield i
                yield root

        return [i.val for i in helper(root)]
