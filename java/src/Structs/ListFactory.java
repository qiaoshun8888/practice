package Structs;

/**
 * Created by xin on 2/19/14.
 */
public class ListFactory {
    public ListNode array2list(int[] intArray){
        ListNode node = new ListNode(-1);
        ListNode head = node;
        for(int i = 0; i< intArray.length ; i++){
            node.next = new ListNode(intArray[i]);
            node = node.next;
        }
        return head.next;
    }

}
