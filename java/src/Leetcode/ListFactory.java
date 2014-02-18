package Leetcode;

import Structs.ListNode;

import java.util.List;

/**
 * Created by xin on 2/17/14.
 */
public class ListFactory {
    public ListNode array2list(int[] intArray){
        ListNode head = new ListNode(intArray[0]);
        ListNode node = head;
        for(int i= 1; i< intArray.length ; i ++){
            node.next = new ListNode(intArray[i]);
            node = node.next;
        }
        return head;
    }
}
