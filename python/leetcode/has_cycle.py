# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs import linkedlist


class Solution:
    # @param head, a ListNode
    # @return a boolean

    def hasCycle(self, head):
        p1, p2 = head, head
        while p1 and p2 and p1.next and p2.next and p2.next.next:
            p1, p2 = p1.next, p2.next.next
            if p1 == p2:
                return True
        return False
