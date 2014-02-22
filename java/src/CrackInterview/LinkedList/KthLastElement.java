package CrackInterview.LinkedList;

import Structs.ListFactory;
import Structs.ListNode;

/**
 * Created by xin on 2/19/14.
 */
public class KthLastElement {
    public ListNode findKth(ListNode head, int k){
        ListNode p1 = head;
        for(int i= 0;i<k;i++ ){
            if(p1 == null) return null;
            p1 = p1.next;
        }
        ListNode p2 = head;
        while(p1 != null){
            p1 = p1.next;
            p2 = p2.next;
        }
        return p2;
    }
    public static  void main(String[] args){
        ListFactory f = new ListFactory();
        int[] intArray = {1,2,3,4,2,5,5,5};
        ListNode head = f.array2list(intArray);
        KthLastElement s = new KthLastElement();
        ListNode k = s.findKth(head, 4);
        System.out.println(k.val);
    }
}
