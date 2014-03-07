package Leetcode;

import Structs.ListNode;
import Structs.ListFactory;

/**
 * Created by xin on 3/5/14.
 */
public class LinkedListCycleII {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null || head.next.next == null) return null;
        ListNode n1 = head.next;
        ListNode n2 = head.next.next;
        int n = 1, c = 1;
        while (n1 != null && n2 != null) {
            if (n1 == n2) {
                // assume we moved n steps, k + c
                // move k steps from head, and move k from k+c, should meet at k
                while (n1 != head) {
                    n1 = n1.next;
                    head = head.next;
                }
                return head;
            } else {
                if (n2.next == null) return null;
                n1 = n1.next;
                n2 = n2.next.next;
                n++;
            }
        }
        return null;
    }

    public static void main(String[] args) {
        ListFactory f = new ListFactory();
        int[] A = {1, 2, 3, 4, 5, 6, 7};
        ListNode t = f.cycleList(A, 3);
        LinkedListCycleII s = new LinkedListCycleII();
        System.out.println(s.detectCycle(t).val);
    }
}
