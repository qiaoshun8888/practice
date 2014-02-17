# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode

    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        # dic = {head.val: True}
        showed = set([head.val])
        o = head
        n = head.next
        while n:
            if n.val in showed:
                o.next = n.next
            else:
                showed.add(n.val)
                o = o.next
            n = n.next
        return head
