# coding=utf-8
'''
# 7
with or without cycle

not tested
should be correct, at least the method is correct

'''
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs import linkedlist


def is_joined_without_cycle(ll1, ll2):
    '''
    if ll1 and ll2 is joined
    they must share the same head or tail
    '''
    if ll1.head == ll2.head:
        return True
    node1 = ll1.head
    while node1.next:
        node1 = node1.next
    node2 = ll2.head
    while node2.next
        node2 == node2.next
    if node1 == node2:
        return True
    return False


def is_joined_with_cycle(ll1, ll2):
    '''
    if ll1 and ll2 is joined with cycle
    use two pointer, one for ll1, one for ll2
    ll1 move 1 node each step
    ll2 move 2 nodes each step
    they should equal once eventually
    '''

    p1 = ll1.head
    p2 = ll2.head
    while p1.next and p2.next and p2.next.next:
        '''
        this loop might be endless
        '''
        if p1 == p2:
            return True
        p1 = p1.next
        p2 = p2.next.next
    if p1 == p2 or p1 == p2.next:
        return True
    return False
