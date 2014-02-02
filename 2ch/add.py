"""
A linked list, where each node contains a single digit
The digits are stored in reverse order, such that
the 1's digit is at the head of the list
Write a function that adds the two numbers and returns the sum
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs import linkedlist


def add(node1, node2):
    tmp = 0
    head = node1
    tail = node1
    while node1 and node2:
        tmp += node1.data + node2.data
        node1.data = tmp % 10
        tmp /= 10
        tail = node1

        node1 = node1.next
        node2 = node2.next
    if node2:
        tail.next = node2
        tail.next.data += tmp
    return head


def reverse(node):
    tail = None
    while node:
        nxt = node.next
        node.next = tail
        tail = node
        node = nxt
    return tail


def recursive_revserse(node):
    if not node.next:
        return node, node
    else:
        head, tail = recursive_revserse(node.next)
        node.next = None
        tail.next = node
        return head, tail.next


def reverseadd(node1, node2):
    node1 = recursive_revserse(node1)[0]
    node2 = recursive_revserse(node2)[0]
    return recursive_revserse(add(node1, node2))[0]


def main():
    node1 = linkedlist.array2linkedlist([7, 1, 6])
    node2 = linkedlist.array2linkedlist([5, 9, 2, 3])
    node3 = add(node1, node2)
    for i in node3:
        print i.data
    print ""
    node1 = linkedlist.array2linkedlist([6, 1, 7])
    node2 = linkedlist.array2linkedlist([2, 9, 5])
    node3 = reverseadd(node1, node2)
    for i in node3:
        print i.data


if __name__ == '__main__':
    main()
