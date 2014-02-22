package CrackInterview.StacksandQueues;

import java.util.Stack;

/**
 * Created by xin on 2/20/14.
 */
public class MinStack {
    Stack<Integer> _data = new Stack<Integer>();
    Stack<Integer> _min = new Stack<Integer>();

    public void push(int x) {
        _data.push(x);
        if (_min.size() ==0 || Integer.compare(x, _min.peek()) <= 0) {
            _min.push(x);
        }
    }

    public Integer get_min() {
        if (_min.size() <= 0) {
            return null;
        } else {
            return _min.peek();
        }
    }

    public Integer pop() {
        Integer res = null;
        if (_data.size() > 0) {
            res = _data.pop();
            if (Integer.compare(res, _min.peek()) == 0) {
                _min.pop();
            }
        }
        return res;
    }

    public static void main(String[] args){
        MinStack m = new MinStack();
        m.push(1);
        System.out.println(m.get_min());
        m.push(2);
        System.out.println(m.get_min());
        m.pop();
        System.out.println(m.pop());
        System.out.println(m.get_min());
        m.push(3);
        System.out.println(m.get_min());
        m.push(2);
        System.out.println(m.get_min());
        m.push(1);
        System.out.println(m.get_min());
        m.pop();
        System.out.println(m.get_min());


    }
}
