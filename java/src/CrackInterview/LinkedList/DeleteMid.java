package CrackInterview.LinkedList;

import Structs.ListFactory;
import Structs.ListNode;

/**
 * Created by xin on 2/19/14.
 */
public class DeleteMid {
    public void delete(ListNode head){
        if(head == null || head.next == null) return;
        ListNode n1 = head.next;
        ListNode n2 = head.next.next;
        while(n2 != null && n2.next != null && n2.next.next != null){
            n1 = n1.next;
            n2 = n2.next.next;
        }
        // delete n1
        n1.val = n1.next.val;
        n1.next = n1.next.next;
    }
    public static  void main(String[] args){
        ListFactory f = new ListFactory();
        int[] intArray = {1,2,3,4,5,6,7,8,9};
        ListNode head = f.array2list(intArray);
        DeleteMid s = new DeleteMid();
        s.delete(head);
        head.printOut();
    }
}
