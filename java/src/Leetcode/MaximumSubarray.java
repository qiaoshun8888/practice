package Leetcode;

/**
 * Created by xin on 2/23/14.
 */
public class MaximumSubarray {
    public int maxSubArray(int[] A) {
        int current = 0;
        int best = Integer.MIN_VALUE;
        for (int i : A) {
            current += i;
            if (current > best) best = current;
            if (current < 0) current = 0;
        }
        return best;
    }


    public static void main(String[] args) {
        int[] A = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        MaximumSubarray s = new MaximumSubarray();
        System.out.println(s.maxSubArray(A)); // should be 6
    }
}
