# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param a ListNode
    # @return a ListNode

    def swapPairs(self, head):
        if not head or not head.next:
            return head

        n1 = head
        n2 = head.next
        new_head = head.next
        while n1 and n2:
            t1 = n2.next
            t2 = None
            if t1:
                t2 = t1.next

            n2.next = n1
            if t1 and not t2:
                n1.next = t1
            else:
                n1.next = t2
            n1 = t1
            n2 = t2
        return new_head
