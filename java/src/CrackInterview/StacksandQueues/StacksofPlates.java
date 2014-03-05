package CrackInterview.StacksandQueues;

import java.util.ArrayList;
import java.util.Stack;

/**
 * Created by xin on 2/22/14.
 */
public class StacksofPlates {
    int StackMAX = 10;

    class Stacks{
        public ArrayList<Stack<Integer>> _data = new ArrayList<Stack<Integer>>();
        public int size() {
            return _data.size();
        }
        public Stack<Integer> peek(){
            if(_data.size() > 0){
                return _data.get(_data.size() -1);
            }
            else{
                return null;
            }
        }
        public void removeLast(){
            if(_data.size()>0) _data.remove(_data.size() -1);
        }
        public Stack<Integer> peekAt(int x){
            if(_data.size() > x){
                return _data.get(x);
            }
            else{
                return null;
            }
        }
        public void push(Stack<Integer> x){
            _data.add(x);
        }
    }
    Stacks ss = new Stacks();

    public void push(int x) {
        if (ss.size() > 0 && ss.peek().size() < StackMAX) {
            // already has stack
            // not full
            ss.peek().push(x);
        } else {
            Stack<Integer> s = new Stack<Integer>();
            s.push(x);
            ss.push(s);
        }
    }

    public Integer pop(){
        if(ss.size() == 0 || ss.peek().size() == 0){
            return null;
        }
        else{
            Integer tmp =  ss.peek().pop();
            if(ss.peek().size() == 0){
                ss.removeLast();
            }
            return tmp;
        }
    }

    public Integer popAt(int x){
        if(x <= ss.size() -1){
            return ss.peekAt(x).pop();
        }else{
            return null;
        }
    }

    public static void main(String[] args){
        StacksofPlates s = new StacksofPlates();
        s.push(1);
        s.pop();
        System.out.println(s.pop());
        for(int i  = 0; i < 100; i++){
            s.push(i);
        }
        System.out.println(s.pop());
        System.out.println(s.popAt(5));
    }
}
