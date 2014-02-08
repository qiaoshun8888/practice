class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    dic = {}

    def levelOrderBottom(self, root):
        def helper(root, depth):
            if root:
                if depth in self.dic:
                    self.dic[depth].append(root.val)
                else:
                    self.dic[depth] = [root.val]
                if root.left:
                    helper(root.left, depth + 1)
                if root.right:
                    helper(root.right, depth + 1)

        helper(root, 0)
        res = []
        for i in sorted(self.dic.keys())[::-1]:
            res.append(self.dic[i])
        return res


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def main():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n1.left = n2
    s = Solution()
    print s.levelOrderBottom(n1)

if __name__ == '__main__':
    main()
