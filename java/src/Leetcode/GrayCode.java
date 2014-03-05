package Leetcode;

import java.util.ArrayList;

/**
 * Created by xin on 2/23/14.
 */
public class GrayCode {
    public ArrayList<Integer> grayCode(int n) {
        // recursive 0(n-1) + 1(n-1).reverse
        ArrayList<Integer> result = new ArrayList<Integer>();
        // base case
        if (n == 0){
            result.add(0);
            return result;
        }
        ArrayList<Integer> n1 = grayCode(n - 1);
        result.addAll(n1);
        for (int i = n1.size() - 1; i >= 0; i--) {
            result.add(n1.get(i) + (1 << n - 1));
        }
        return result;
    }

    public static void main(String[] args) {
        GrayCode s = new GrayCode();
        for (int i : s.grayCode(2)) {
            System.out.println(i); // should be 0132
        }
    }
}
