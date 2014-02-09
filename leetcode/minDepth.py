# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer

    def minDepth(self, root):
        if not root:
            return 0

        min_depth = float('inf')
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                # it's a leaf
                if depth < min_depth:
                    min_depth = depth

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return min_depth

        # maximum recursion depth exceeded
        # return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
