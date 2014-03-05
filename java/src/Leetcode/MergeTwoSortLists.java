package Leetcode;

import Structs.ListNode;

/**
 * Created by xin on 2/23/14.
 */
public class MergeTwoSortLists {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null) return l2;
        if(l2 == null) return l1;
        ListNode head =  new ListNode(0);
        ListNode runner = head;
        while(l1 != null && l2!= null){
            if(l1.val > l2.val){
                // l2 smaller than l1
                runner.next = l2;
                l2 = l2.next;
            }else{
                runner.next = l1;
                l1 = l1.next;
            }
            runner = runner.next;
        }
        // leftover
        if(l1!=null) runner.next = l1;
        if(l2!=null) runner.next = l2;
        return head.next;
    }


    public static void main(String[] args){
        ListFactory f = new ListFactory();
        int[] A = {1,2,3,4,5};
        int[] B = {2,3,4,5,6};
        ListNode l1 = f.array2list(A);
        ListNode l2 = f.array2list(B);
        MergeTwoSortLists s = new MergeTwoSortLists();
        ListNode r0 = s.mergeTwoLists(l1, l2);
        r0.printOut(); // should be 1,2,2,3,3,4,4,5,5,6
    }
}
