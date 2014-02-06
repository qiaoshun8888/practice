import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs import linkedlist


def recursive_reverse(ll):
    def recursive_reverse_helper(ll):
        if not ll.next:
            return ll, ll
        else:
            head, last = recursive_reverse_helper(ll.next)
            last.next = ll
            ll.next = None
            return head, ll
    return recursive_reverse_helper(ll)[0]


def reverse(ll):
    head = ll
    if not ll.next:
        return ll
    node1 = ll
    node2 = ll.next
    while node2:
        tmp = node2.next
        node2.next = node1
        node1 = node2
        node2 = tmp
    head.next = None
    return node1


def main():
    ll = linkedlist.array2linkedlist([1, 2, 3, 4])
    for i in recursive_reverse(ll):
        print i.data,
    print ''
    ll = linkedlist.array2linkedlist([1, 2, 3, 4])
    for i in reverse(ll):
        print i.data,
    print ''
ll = linkedlist.array2linkedlist([1, 2, 3, 4])

if __name__ == '__main__':
    main()
