
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree node
    # @return nothing

    def connect(self, root):
        if not root:
            return
        dic = {}
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop(0)
            if depth in dic:
                dic[depth].next = node
            dic[depth] = node
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

    def connect2(self, root):
        if not root:
            return
        dic = {}

        def dfs(root, depth, dic):
            if not root:
                return
            if depth in dic:
                dic[depth].next = root
            dic[depth] = root
            if root.left:
                dfs(root.left, depth + 1, dic)
            if root.right:
                dfs(root.right, depth + 1, dic)
        dfs(root, 1, dic)
