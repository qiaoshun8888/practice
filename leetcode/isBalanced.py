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
