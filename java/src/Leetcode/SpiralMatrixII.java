package Leetcode;

/**
 * Created by xin on 3/9/14.
 */
public class SpiralMatrixII {
    public int[][] generateMatrix(int n) {
        int[][] m = new int[n][n];
        int x = 0, y = 0, flag = 0, lx = 0, hx = n - 1, ly = 0, hy = n - 1;
        for (int i = 1; i <= n * n; i++) {
            m[y][x] = i;
            switch (flag) {
                case 0: // >
                    if (++x == hx) {
                        flag = 1;
                        ly++;
                    }
                    break;
                case 1: // v
                    if (++y == hy) {
                        flag = 2;
                        hx--;
                    }
                    break;
                case 2: // <
                    if (--x == lx) {
                        flag = 3;
                        hy--;
                    }
                    break;
                case 3: // ^
                    if (--y == ly) {
                        flag = 0;
                        lx++;
                    }
                    break;
            }
        }
        return m;
    }

    public static void main(String[] args) {
        SpiralMatrixII s = new SpiralMatrixII();
        for (int[] i : s.generateMatrix(5)) {
            for (int j : i) System.out.printf("%d, ", j);
            System.out.println();
        }
//        int[][] t = {
//                {1, 2, 3},
//                {8, 9, 4},
//                {7, 6, 5}
//        };
//        for (int i : s.generateMatrix(t)) System.out.println(i);
    }
}
