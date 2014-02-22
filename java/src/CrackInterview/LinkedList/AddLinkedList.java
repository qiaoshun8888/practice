package CrackInterview.LinkedList;

import Structs.ListFactory;
import Structs.ListNode;

/**
 * Created by xin on 2/19/14.
 */
public class AddLinkedList {
    public ListNode reverse(ListNode head){
        if(head == null || head.next == null) return head;
        ListNode tmp = head;
        ListNode tmp2 = head.next;
        head.next = null;
        head = tmp2;
        while(head != null){
            tmp2 = head.next;
            head.next = tmp;
            tmp = head;
            head = tmp2;
        }
        return tmp;
    }
    public ListNode add(ListNode p, ListNode q) {
        if (p == null) return q;
        if (q == null) return p;
        ListNode head = new ListNode(0);
        ListNode node = head;
        while (p != null && q != null) {
            node.val += p.val + q.val;
            node.next = new ListNode(node.val / 10);
            node.val = node.val % 10;
            node = node.next;
            p = p.next;
            q = q.next;
        }
        while (p != null) {
            node.val += p.val;
            node.next = new ListNode(node.val / 10);
            node.val = node.val % 10;
            node = node.next;
            p = p.next;
        }
        while (q != null) {
            node.val += q.val;
            node.next = new ListNode(node.val / 10);
            node.val = node.val % 10;
            node = node.next;
            q = q.next;
        }
        return head;
    }

    public static  void main(String[] args){
        ListFactory f = new ListFactory();
        int[] intArray = {1,2,3};
        ListNode p = f.array2list(intArray);
        ListNode q = f.array2list(intArray);
        AddLinkedList s = new AddLinkedList();
        ListNode k = s.add(p, q);
        k.printOut();
        ListNode r = s.reverse(p);
        r.printOut();
    }
}
