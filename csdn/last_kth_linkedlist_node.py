"""
same as 2ch/kth_last_element.py

Implement an algorithm
To find the kth to last element of as singliy linked list
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs import linkedlist


def kth(node, k):
    if k <= 0:
        return 'wrong k'
    node1 = node
    for i in range(k):
        if not node1.next:
            return -1
        node1 = node1.next
    while node1:
        node = node.next
        node1 = node1.next
    return node.data


def main():

    node = linkedlist.array2linkedlist(
        [1, 2, 3, 4, 5, 6, 7, 8, ])
    print kth(node, 1)
    print kth(node, 100)
    print kth(node, 0)
    print kth(node, 5)
    print kth(node, 5)


if __name__ == '__main__':
    main()
