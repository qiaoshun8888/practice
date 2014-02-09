# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers

    def pathSum(self, root, sum):
        if not root:
            return []
        result = []
        stack = [(root, sum, [])]
        while stack:
            node, sum, path = stack.pop()
            path = list(path)
            path.append(node.val)
            if not node.left and not node.right:
                if node.val == sum:
                    result.append(path)
            if node.left:
                stack.append((node.left, sum - node.val, path))
            if node.right:
                stack.append((node.right, sum - node.val, path))
        return result
