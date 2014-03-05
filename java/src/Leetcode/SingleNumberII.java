package Leetcode;

/**
 * Created by xin on 2/23/14.
 */
public class SingleNumberII {
    public int singleNumber(int[] A) {
        int num = 0;
        for (int p = 0; p < Integer.SIZE; p++) {
            int tmp = 0;
            for (int i : A) {
                if ((i & (1 << p)) != 0) tmp += 1; // add get p th bit of i
            }
            if (tmp % 3 != 0) num += 1 << p;
        }
        return num;
    }

    public static void main(String[] args) {
        SingleNumberII s = new SingleNumberII();
        int[] A = {-2, -2, 1, 1, -3, 1, -3, -3, -4, -2};
        System.out.println(s.singleNumber(A)); // should be -4
    }
}
