#coding=utf-8
"""
To partition a linked list around a value x
Such that all nodes less than x come before all nodes greater than or equal to x
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs import linkedlist

def partition(node, x):
    r = None
    head = node
    while node:
        if node.data >= x:
            if not r:
                r = node
        else:
            if r:
                node.data, r.data = r.data, node.data
                node = r
                r = None
        node = node.next
    return head

def main():
    node = linkedlist.array2linkedlist([1,2,5,6,7,3,2,4,9,24,2,3,54,67,0])
    partition(node, 6)
    for i in node:
        print i.data,

if __name__ == '__main__':
    main()
