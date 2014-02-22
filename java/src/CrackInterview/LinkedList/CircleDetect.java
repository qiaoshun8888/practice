package CrackInterview.LinkedList;

import Structs.ListNode;

/**
 * Created by xin on 2/19/14.
 */
public class CircleDetect {
    public boolean isCircle(ListNode head){
        if(head == null || head.next == null || head.next.next == null) return false;
        ListNode n1 = head.next;
        ListNode n2 = head.next.next;
        while(n1 != null && n2.next != null && n2.next.next != null){
            if(n1 == n2){
                return true;
            }
            n1 = n1.next;
            n2 = n2.next.next;
        }
        return false;
    }
}
