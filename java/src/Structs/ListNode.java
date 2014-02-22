package Structs;

/**
 * Created by xin on 2/17/14.
 */
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val){
        this.val = val;
    }
    public void printOut(){
        ListNode n = this;
        while(n != null){
            System.out.printf("%d, ", n.val);
            n = n.next;
        }
        System.out.println();
    }
}
