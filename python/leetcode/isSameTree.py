# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs.binary_tree import array2tree


class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean

    def isSameTree(self, p, q):
        if not p and q:
            return False
        elif not q and p:
            return False
        elif not p and not q:
            return True

        if not p.val == q.val:
            return False
        stack1 = [p]
        stack2 = [q]

        while stack1:
            p = stack1.pop()
            q = stack2.pop()
            if not p and not q:
                continue
            if not p.val == q.val:
                return False
            if p.left and q.left:
                stack1.append(p.left)
                stack2.append(q.left)
            elif p.right or q.right:
                return False

            if p.right and q.right:
                stack1.append(p.right)
                stack2.append(q.right)
            elif p.right or q.right:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    p = array2tree([1, None, 1])
    q = array2tree([1, None, 1])
    print s.isSameTree(p, q)
