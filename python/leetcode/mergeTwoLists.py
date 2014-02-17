# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs.linkedlist import Node as ListNode
from structs.linkedlist import array2linkedlist


class Solution:
    # @param two ListNodes
    # @return a ListNode

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode(None)
        runner = head
        while l1 and l2:
            if l1.val > l2.val:
                runner.next = l2
                l2 = l2.next
            else:
                runner.next = l1
                l1 = l1.next
            runner = runner.next
        if l1:
            runner.next = l1
        if l2:
            runner.next = l2
        # print head.next.data
        return head.next

if __name__ == '__main__':
    l1 = array2linkedlist([3, 5])
    l2 = array2linkedlist([1, 2, 4])
    if l1:
        for i in l1:
            i.val = i.data
    if l2:
        for i in l2:
            i.val = i.data
    s = Solution()
    r = s.mergeTwoLists(l1, l2)
    if r:
        for i in r:
            print i.val
