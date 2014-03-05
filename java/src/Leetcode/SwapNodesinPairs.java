package Leetcode;

import Structs.ListNode;

/**
 * Created by xin on 2/23/14.
 */
public class SwapNodesinPairs {
    public ListNode swapPairs(ListNode head) {
        // recursive
        // base case there is not head.next.next
        if (head == null) return null;
        if (head.next == null) return head;
        ListNode tmp = head.next;
        head.next = swapPairs(head.next.next);
        tmp.next = head;
        return tmp;
    }

    public static void main(String[] args) {
        SwapNodesinPairs s = new SwapNodesinPairs();
        ListFactory f = new ListFactory();
        int[] A = {1, 2, 3, 4,};

        ListNode r = s.swapPairs(f.array2list(A));
        r.printOut();f.array2list(A);
    }
}
