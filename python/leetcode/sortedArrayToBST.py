# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param num, a list of integers
    # @return a tree node

    def sortedArrayToBST(self, num):
        ''' reverse '''
        if not num:
            return None

        mid = len(num) / 2
        l = num[:mid]
        r = num[mid + 1:]
        root = TreeNode(num[mid])
        if l:
            ln = self.sortedArrayToBST(l)
            root.left = ln
        if r:
            rn = self.sortedArrayToBST(r)
            root.right = rn

        return root
