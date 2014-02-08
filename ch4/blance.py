"""
a function to check if a binary_tree is balanced
"""


import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs.binary_tree import Node

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

        if not root:
            return True

        def depth(node):
            if not node:
                return 0
            else:
                return node.depth

        stack = [root]
        while stack:
            node = stack.pop()
            # print node.data
            if hasattr(node, 'visited'):
                if depth(node.left) == -1:
                    return False
                elif depth(node.right) == -1:
                    return False
                elif depth(node.right) > depth(node.left) + 1:
                    return False
                elif depth(node.left) > depth(node.right) + 1:
                    return False
                else:
                    node.depth = max(depth(node.left), depth(node.right)) + 1
            else:
                node.visited = True
                stack.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if not node.left and not node.right:
                node.depth = 1
        return root.depth > 0
        # recursion fail at 995
        # def helper(root):
        #     if not root:
        #         return True, 0, 0
        #     lb, lmax, lmin = helper(root.left)
        #     rb, rmax, rmin = helper(root.right)
        #     if not lb:
        # return False, 0, 0 # don't care
        #     if not rb:
        # return False, 0, 0 # don't care
        #     tmax = max(lmax, rmax)
        #     tmin = min(lmin, rmin)
        #     if tmax - tmin > 1:
        # return False, 0, 0 # don't care
        #     return True, tmax + 1, tmin + 1
        # return helper(root)[0]


# def is_balance(node):
#     ''' totally wrong!!! in 1-2-3-4 tree '''
#     ed = []
#     def dfs(node, deep):
#         if node not in ed:
#             ed.append(node)
#             if not node.left and not node.right:
#                 yield deep
#             else:
#                 if node.left:
#                     for i in dfs(node.left, deep + 1):
#                         yield i
#                 if node.right:
#                     for i in dfs(node.right, deep + 1):
#                         yield i
#     m = float('-inf')
#     n = float('inf')
#     for i in dfs(node, 0):
#         if i > m:
#             m = i
#         if i < n:
#             n = i
#         if m - n >= 2:
#             return False
#     return True
def main():
    head = Node(0)
    n1 = head
    for i in range(100000):
        tmp = Node(1)
        n1.left = tmp
        n1 = n1.left
    s = Solution()
    print s.isBalanced(head)
    # print is_balance(n1)

if __name__ == '__main__':
    main()
