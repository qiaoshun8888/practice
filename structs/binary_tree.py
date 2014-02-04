# coding=utf-8


def array2tree(l, need_array=False):
    for k, v in enumerate(l):
        l[k] = Node(v)
    for i in range(len(l) / 2):
        if 2 * i + 1 < len(l):
            l[i].left = l[i * 2 + 1]
            l[i * 2 + 1].parent = l[i]
        if 2 * i + 2 < len(l):
            l[i].right = l[i * 2 + 2]
            l[i * 2 + 2].parent = l[i]
    if need_array:
        return l
    return l[0]


class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None

    def in_order_next(self):
        # print self.parent, 'in_order_next'
        if self.right:
            node = self.right
            while node.left:
                node = node.left
            return node
        else:
            node = self
            parent = self.parent
            while parent and parent.right == node:
                node = parent
                parent = parent.parent
            return parent

    def pre_order(self):
        yield self.data
        if self.left:
            for i in self.left.pre_order():
                yield i
        if self.right:
            for i in self.right.pre_order():
                yield i

    def in_order(self):
        if self.left:
            for i in self.left.in_order():
                yield i
        yield self.data
        if self.right:
            for i in self.right.in_order():
                yield i

    def post_order(self):
        if self.left:
            for i in self.left.post_order():
                yield i
        if self.right:
            for i in self.right.post_order():
                yield i
        yield self.data

if __name__ == '__main__':
    l = array2tree([1, 2, 3, 4, 5, 6, 7], True)

    n1 = l[0]
    for i in n1.pre_order():
        print i,
    print ""

    for i in n1.in_order():
        print i,
    print "inorder"

    node = l[3]
    while node:
        print node.data,
        node = node.in_order_next()
    print "inorder2"

    for i in n1.post_order():
        print i,
    print ""

    # print array2tree([10, 6, 14, 4, 8, 12, 6]).data
