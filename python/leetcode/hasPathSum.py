# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean

    def hasPathSum(self, root, sum):
        if not root:
            return False

        def dfshelper(root, sum):
            if not root.left and not root.right:
                if sum == root.val:
                    return True
            sum -= root.val
            if root.left:
                if dfshelper(root.left, sum):
                    return True
            if root.right:
                if dfshelper(root.right, sum):
                    return True
            sum += root.val
            return False

        if dfshelper(root, sum):
            return True
        else:
            return False
