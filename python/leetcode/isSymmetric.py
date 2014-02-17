# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a boolean

    def isSymmetric(self, root):
        '''
        use stack dfs
        '''
        if not root:
            return True
        stack1 = [root]
        stack2 = [root]
        while stack1 or stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if not node1.val == node2.val:
                return False

            if node1.left and node2.right:
                stack1.append(node1.left)
                stack2.append(node2.right)
            else:
                if node1.left or node2.right:
                    return False

            if node1.right and node2.left:
                stack1.append(node1.right)
                stack2.append(node2.left)
            else:
                if node1.right or node2.left:
                    return False
        return True
