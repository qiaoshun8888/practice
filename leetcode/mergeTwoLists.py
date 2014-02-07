# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param two ListNodes
    # @return a ListNode

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        head1 = l1
        head2 = l2
        p1 = l1
        p2 = l2
        tail1 = l1
        tail2 = l2
        while p1 and p2:
            tail1 = p1
            tail2 = p2
            if p1.val > p2.val:
                p1.val, p2.val = p2.val, p1.val
                tmp1 = p1.next
                tmp2 = p2.next
                p1.next = p2
                p2.next = tmp
                p1 = tmp1
                p2 = tmp2
            else:
                p1 = p1.next
        if p2:
            tail1.next = p2
        return head1
