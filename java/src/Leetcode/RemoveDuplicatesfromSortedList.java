package Leetcode;

import CrackInterview.LinkedList.RemoveDuplicates;
import Structs.ListNode;

import java.util.HashMap;

/**
 * Created by xin on 2/23/14.
 */
public class RemoveDuplicatesfromSortedList {
    public ListNode deleteDuplicates(ListNode head) {
        // using HashMap
        if (head == null || head.next == null) return head;
        HashMap<Integer, Boolean> m = new HashMap<Integer, Boolean>();
        m.put(head.val, true);
        ListNode tmp = head;
        ListNode node = head.next;
        while (node != null) {
            if (m.containsKey(node.val)) {
                // duplicated, needs to be deleted
                tmp.next = node.next;
                // move node, don't move tmp
                node = node.next;
            } else {
                m.put(node.val, true);
                // move both node and tmp
                tmp = tmp.next;
                node = node.next;
            }
        }
        return head;
    }

    public static void main(String[] args) {
        ListFactory f = new ListFactory();
        int[] A = {1, 1, 2};
        ListNode head = f.array2list(A);
        RemoveDuplicatesfromSortedList s = new RemoveDuplicatesfromSortedList();
        s.deleteDuplicates(head);
        head.printOut();
        // should be 1, 2
        int[] B = {1, 1, 2, 3, 3};
        head = f.array2list(B);
        s.deleteDuplicates(head);
        head.printOut();
        // should be 1, 2, 3,

    }
}
