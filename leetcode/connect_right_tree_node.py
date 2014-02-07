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
            if depth not in dic:
                node.next = None
                dic[depth] = [node]
            else:
                node.next = dic[depth][-1]
                dic[depth].append(node)

            if node.left:
                stack.append((node.right, depth + 1))
            if node.right:
                stack.append((node.left, depth + 1))
