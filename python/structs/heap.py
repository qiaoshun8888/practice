"""
Heap
    MinHeap
    MaxHeap
"""

from binary_tree import Node as BTNode
from binary_tree import array2tree as a2t


class MinHeap():

    def __init__(self, tree):
        self.root = tree.root
        self.length = tree.length

    def heapify(self, node):
        best = node
        if node.left and node.left.data < best.data:
            best = node.left
        if node.right and node.right.data < best.data:
            best = node.right

        if not best == node:
            node.data, best.data = best.data, node.data
            self.heapify(best)

    def get_node(self, i):
        node = self.root
        for j in bin(i + 1)[3:]:
            if j == '0':
                node = node.left
            if j == '1':
                node = node.right
        return node

    def heap_build(self):
        """
        dfs for 2/n
        """
        for i in range(1, self.length / 2)[::-1]:
            node = self.get_node(i)
            self.heapify(node)

        self.heap_size = self.length

    def pop(self):
        root = self.root
        tmp = root.data

        tail = self.get_node(self.heap_size - 1)
        root.data = tail.data

        self.heap_size -= 1
        self.heapify(root)
        return tmp


def gen_minheap(array):
    h = MinHeap(a2t(array, tree=True))
    h.heap_build()
    return h


def main():
    """
    test minheap
    """
    h = gen_minheap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    for i in h.root.pre_order():
        print i

    print '\n\n'
    print h.pop()
    print h.pop()
    print h.pop()
    print h.pop()


if __name__ == '__main__':
    main()
