# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers

    def levelOrder(self, root):
        '''bfs'''
        if not root:
            return []
        dic = {}
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop(0)
            if depth not in dic:
                dic[depth] = [node.val]
            else:
                dic[depth].append(node.val)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        res = []
        for i in sorted(dic.keys()):
            res.append(dic[i])
        return res
