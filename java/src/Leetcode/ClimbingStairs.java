package Leetcode;

import java.util.HashMap;

/**
 * Created by xin on 2/23/14.
 */
public class ClimbingStairs {
    public int dpHelper(int n, HashMap<Integer, Integer> dp) {
        if (n == 1) return 1;
        if (n == 2) return 2;
        if (dp.containsKey(n)) return dp.get(n);
        int tmp = dpHelper(n - 1, dp) + dpHelper(n - 2, dp);
        dp.put(n, tmp);
        return tmp;
    }

    public int climbStairs(int n) {
        return dpHelper(n, new HashMap<Integer, Integer>());
    }

    public static void main(String[] args){
        // Fibonacci numbers
        ClimbingStairs s = new ClimbingStairs();
        System.out.println(s.climbStairs(1)); // should be 1
        System.out.println(s.climbStairs(2)); // should be 2
        System.out.println(s.climbStairs(3)); // should be 3
        System.out.println(s.climbStairs(10)); // should be 55
    }
}
