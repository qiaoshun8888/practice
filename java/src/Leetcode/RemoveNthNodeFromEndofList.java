package Leetcode;

import Structs.ListNode;
import Structs.ListFactory;

/**
 * Created by xin on 3/9/14.
 */
public class RemoveNthNodeFromEndofList {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode tmp = new ListNode(-1), n1 = head, n2 = tmp;
        tmp.next = head;
        for (int i = 0; i < n; i++) {
            if (n1 == null) return head;
            n1 = n1.next;
        }
        while (n1 != null) {
            n1 = n1.next;
            n2 = n2.next;
        }
        n2.next = n2.next.next;
        return tmp.next;
    }

    public static void main(String[] args) {
        RemoveNthNodeFromEndofList s = new RemoveNthNodeFromEndofList();
        ListFactory f = new ListFactory();
        int[] A = {1, 2, 3, 4, 5};
        ListNode head = f.array2list(A);
        s.removeNthFromEnd(head, 5).printOut();
    }
}
