package Leetcode;

/**
 * Created by xin on 2/24/14.
 */
public class RotateImage {
    public void rotate(int[][] matrix) {
        int[][] t = new int[matrix.length][matrix[0].length];
        int j = 0;
        for (int[] r : matrix) {
            int i = 0;
            for (int c : r) {
                t[i][j] = c;
                i++;
            }
            j++;
        }
        j = 0;
        for (int[] r : t) {
            for (int i = 0; i < r.length; i++) {
                //r[i] , r[r.length-i] swap
                matrix[j][i] = r[r.length - 1 - i];
            }
            j++;
        }
    }

    public static void main(String[] args) {
        int[][] matrix = {
                {1, 1, 1},
                {1, 1, 3},
                {1, 3, 3}
        };
        RotateImage s = new RotateImage();
        s.rotate(matrix);
        for (int[] r : matrix) {
            for (int c : r) {
                System.out.printf("%d, ", c);
            }
            System.out.println();
        }
    }
}
