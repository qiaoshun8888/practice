package Leetcode;

import java.util.LinkedList;

/**
 * Created by xin on 2/17/14.
 * Bug of overflow!!
 */
public class ReverseInteger {
    public int reverse(int x) {
        boolean neg = false;
        if (x < 0) {
            x = -x;
            neg = true;
        }
        LinkedList<Integer> ll = new LinkedList<Integer>();
        while (x >= 10) {
            ll.add(x % 10);
            x = x / 10;
        }
        ll.add(x);
        x = 0;
        while (ll.size() > 0) {
            Integer i = ll.pop();
            x = 10 * x + i;
        }
        if (neg) return -x;
        return x;
    }

    public static void main(String[] args) {
        int x = 123;
        ReverseInteger s = new ReverseInteger();
        System.out.println(s.reverse(x));

        x = -123;
        System.out.println(s.reverse(x));

    }
}
