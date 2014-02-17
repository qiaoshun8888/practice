
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

        '''still wrong
        def helper(root):
            if not root:
                return True, 0, 0
            lb, lmin, lmax = helper(root.left)
            rb, rmin, rmax = helper(root.right)
            ma = 1 + max(lmax, rmax)
            mi = 1 + min(lmin, rmin)
            if not lb:
                return False, ma, mi
            if not rb:
                return False, ma, mi
            if max(lmax, rmax) - min(lmin, rmin) > 1:
                return False, ma, mi
            return True, ma, mi
        return helper(root)[0]

        # def min_max_depth(root):
        #     if not root:
        #         return 0
        #     lminimum, lmaximum = min_max_depth(root.left)
        #     rminimum, rmaximum = min_max_depth(root.right)
        #     minimum = 1 + min(lminimum, rminimum)
        #     maximum = 1 + max(lmaximum, rmaximum)
        #     return minimum, maximum
        # minimum, maximum = min_max_depth(root)
        # if maximum - minimum > 1:
        #     return False
        # else:
        #     return True
        '''
