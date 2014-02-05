'''
# 24
Merge
'''
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs.linkedlist import array2linkedlist as a2l


def merge(ll1, ll2):
    head = ll1
    node1 = ll1
    node2 = ll2
    while ll1.next and ll2:
        if ll2.data < ll1.data:
            tmp = ll1.next
            tmp1 = ll2.next
            ll1.data, ll2.data = ll2.data, ll1.data
            ll1.next = ll2
            ll1.next.next = tmp
            ll2 = tmp1
        else:
            ll1 = ll1.next
    if ll2:
        while ll1.next:
            ll1 = ll1.next
        ll1.next = ll2
    return head

if __name__ == '__main__':
    ll1 = a2l([1, 2, 3, 4, 5, 6, 7])
    ll2 = a2l([2, 3, 4, 5, 67, 89])
    for i in merge(ll1, ll2):
        print i.data
