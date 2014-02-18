package Leetcode;

import Structs.ListNode;

/**
 * Created by xin on 2/17/14.
 */
public class LinkedListCycle {
    public boolean hasCycle(ListNode head) {
        if(head == null) return false;
        ListNode n1 = head;
        ListNode n2 = head;
        while(n1.next != null && n2.next != null && n2.next.next != null){
            n1 = n1.next;
            n2 = n2.next.next;
            if(n1 == n2) return true;
        }
        return false;
    }
}
