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

        dic = {head.val: True}
        o = head
        n = head.next
        while n:
            if n.val in dic:
                o.next = n.next
                n = n.next
            else:
                dic[n.val] = True
                n = n.next
                o = o.next
        return head
