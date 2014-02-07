# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer

    def maxDepth(self, root):
        # if not root:
        #     return 0
        # else:
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        if not root:
            return 0
        best = 0
        stack = []
        stack.append((root, 1))
        while stack:
            node, depth = stack.pop()
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

            if not node.left and not node.right:
                if depth > best:
                    best = depth
        return best
