package CrackInterview.StacksandQueues;

import java.util.Stack;

/**
 * Created by xin on 2/22/14.
 */
public class Hanoi {
    public Stack<Integer> t1 = new Stack<Integer>();
    public Stack<Integer> t2 = new Stack<Integer>();
    public Stack<Integer> t3 = new Stack<Integer>();

    public Hanoi(int n){
        for(int i=n; i>=1; i--){
            t1.push(i);
        }
    }
    public boolean canPush(Stack<Integer> t, int x){
        if(x > t.peek()){
            return false;
        }
        return true;
    }
    public void moveHelper(Stack<Integer> from, Stack<Integer> to, int n){
        // n is the number needs to be moved
        if(n == 1){
            to.push(from.pop());
        }else{
            Stack<Integer> rest = t1;
            if(t2 != from && t2 != to){
                rest = t2;
            }else if(t3 != from && t3 != to){
                rest = t3;
            }
            moveHelper(from, rest, n-1);
            moveHelper(from, to, 1);
            moveHelper(rest, to, n-1);
        }

    }
    public void move(){
        moveHelper(t1, t3, t1.size());
    }

    public static void main(String[] args){
        Hanoi h = new Hanoi(10);
        h.move();
        while(h.t3.size() > 0){
            // should be 1,2,3,4,5,6,7,8,9,10,
            System.out.printf("%d, ", h.t3.pop());
        }
    }
}
