# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean

    def isBalanced(self, root):
        '''still wrong
        def helper(root):
            if not root:
                return True, 0, 0
            lb, lmin, lmax = helper(root.left)
            rb, rmin, rmax = helper(root.right)
            ma = 1 + max(lmax, rmax)
            mi = 1 + min(lmin, rmin)
            if not lb:
                return False, ma, mi
            if not rb:
                return False, ma, mi
            if max(lmax, rmax) - min(lmin, rmin) > 1:
                return False, ma, mi
            return True, ma, mi
        return helper(root)[0]

        # def min_max_depth(root):
        #     if not root:
        #         return 0
        #     lminimum, lmaximum = min_max_depth(root.left)
        #     rminimum, rmaximum = min_max_depth(root.right)
        #     minimum = 1 + min(lminimum, rminimum)
        #     maximum = 1 + max(lmaximum, rmaximum)
        #     return minimum, maximum
        # minimum, maximum = min_max_depth(root)
        # if maximum - minimum > 1:
        #     return False
        # else:
        #     return True
