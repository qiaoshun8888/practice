package CrackInterview.LinkedList;

import Structs.ListFactory;
import Structs.ListNode;

/**
 * Created by xin on 2/19/14.
 */
public class Partition {
    public void partitionBy(ListNode head, int x){
        if(head == null || head.next == null) return ;
        ListNode pivot = head;
        ListNode runner = head.next;
        while(pivot != null){
            if(pivot.val >x){
                ListNode swapper = null;
                while(runner != null){
                    if(runner.val <= x){
                        swapper = runner;
                    }
                    runner = runner.next;
                }
                if(swapper == null){
                    return;
                }
                else{
                    swapper.val = swapper.val + pivot.val;
                    pivot.val = swapper.val - pivot.val;
                    swapper.val = swapper.val - pivot.val;
                }
            }
            pivot = pivot.next;
        }
    }

    public static  void main(String[] args){
        ListFactory f = new ListFactory();
        int[] intArray = {1,2,3,4,2,5,5,5,3};
        ListNode head = f.array2list(intArray);
        Partition s = new Partition();
        s.partitionBy(head, 3);
        head.printOut();
    }
}
