package Leetcode;

/**
 * Created by xin on 3/6/14.
 */
public class PlusOne {
    public int[] plusOne(int[] digits) {
        int tmp = 1;
        for (int i = digits.length - 1; i >= 0; i--) {
            digits[i] += tmp;
            tmp = digits[i] / 10;
            digits[i] = digits[i] % 10;
        }
        if (tmp > 0) {
            int[] res = new int[digits.length + 1];
            res[0] = tmp;
            for (int i = 0; i < digits.length; i++) res[i + 1] = digits[i];
            return res;
        } else {
            return digits;
        }
    }

    public static void main(String[] args) {
        PlusOne s = new PlusOne();
        int[] t = {9,9,9};
        for (int i : s.plusOne(t)) System.out.println(i);
    }
}
