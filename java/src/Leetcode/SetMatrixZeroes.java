package Leetcode;

/**
 * Created by xin on 3/6/14.
 * constant space. Use the first col and row as storage.
 */
public class SetMatrixZeroes {
    public void setZeroes(int[][] matrix) {
        if (matrix.length == 0) return;
        if (matrix[0].length == 0) return;
        boolean firstRowZero = false, firstColZero = false;
        for (int i = 0; i < matrix.length; i++) {
            if (matrix[i][0] == 0) {
                firstColZero = true;
                break;
            }
        }
        for (int i = 0; i < matrix[0].length; i++) {
            if (matrix[0][i] == 0) {
                firstRowZero = true;
                break;
            }
        }
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        for (int i = 1; i < matrix.length; i++) {
            for (int j = 1; j < matrix[0].length; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }
        if (firstColZero) {
            for (int i = 0; i < matrix.length; i++) {
                matrix[i][0] = 0;
            }
        }
        if (firstRowZero) {
            for (int i = 0; i < matrix[0].length; i++){
                matrix[0][i] = 0;
            }
        }
    }

    public static void main(String[] args) {
        int[][] t = {
                {0, 1, 1},
                {1, 1, 1},
                {0, 1, 0}
        };
        SetMatrixZeroes s = new SetMatrixZeroes();
        s.setZeroes(t);
        for (int[] i : t) {
            for (int j : i) {
                System.out.printf("%d, ", j);
            }
            System.out.println();
        }
    }
}
