package CrackInterview.StacksandQueues;

import java.util.Stack;

/**
 * Created by xin on 2/22/14.
 */
public class MyQueue {
    Stack<Integer> inputStack = new Stack<Integer>();
    Stack<Integer> outputStack = new Stack<Integer>();
    public void enqueue(int x){
        inputStack.push(x);
    }
    public Integer dequeue(){
        if(outputStack.size() == 0){
            if(inputStack.size() == 0) return null;
            else{
                while(inputStack.size() > 0){
                    outputStack.push(inputStack.pop());
                }
            }
        }
        return outputStack.pop();
    }

    public static void main(String[] args){
        MyQueue s = new MyQueue();
        s.enqueue(1);
        s.enqueue(2);
        s.enqueue(3);
        System.out.printf("%d, ", s.dequeue());
        System.out.printf("%d, ", s.dequeue());
        s.enqueue(4);
        s.enqueue(5);
        s.enqueue(6);
        System.out.printf("%d, ", s.dequeue());
        System.out.printf("%d, ", s.dequeue());
        // ouput 1,2,3,4
    }
}
