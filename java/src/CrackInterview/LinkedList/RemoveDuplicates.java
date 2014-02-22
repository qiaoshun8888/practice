package CrackInterview.LinkedList;

import Structs.ListFactory;
import Structs.ListNode;

import java.util.HashMap;

/**
 * Created by xin on 2/19/14.
 */
public class RemoveDuplicates {
    public void removeDuplicates(ListNode head) {
        HashMap<Integer, Boolean> m = new HashMap<Integer, Boolean>();
        if (head == null) return;
        ListNode tmp = null;
        ListNode node = head;
        while (node != null) {
            if (m.containsKey(node.val)) {
                tmp.next = node.next;
            } else {
                m.put(node.val, true);
                tmp = node;
            }
            node = node.next;
        }
    }

    public void removeDuplicates2(ListNode head) {
        /**
         * Bug in the tail, I don't understand
         */
        if (head == null || head.next == null) return;
        ListNode tmp = head;
        ListNode pivot = head.next;
        while (pivot != null) {
            ListNode runner = head;
            boolean deleted = false;
            while (runner != pivot) {
                if (runner.val == pivot.val) {
                    // remove pivot
                    tmp.next = pivot.next;
                    pivot = pivot.next;
                    deleted = true;
                    break;
                }
                runner = runner.next;
            }
            if (!deleted) {
                tmp = pivot;
                pivot = pivot.next;
            }
        }
    }

    public static void main(String[] args) {
        ListFactory f = new ListFactory();
        int[] intArray = {1, 2, 3, 4, 2, 5, 5, 5, 5, 7, 5};
        ListNode head = f.array2list(intArray);
        RemoveDuplicates s = new RemoveDuplicates();
        s.removeDuplicates2(head);
        head.printOut();
    }
}
