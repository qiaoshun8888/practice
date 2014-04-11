package Leetcode;

/**
 * Created by xin on 3/9/14.
 */
public class Searcha2DMatrix {
    public boolean searchMatrix(int[][] matrix, int target) {
        // search from the top right corner
        if (matrix.length == 0) return false;
        else if (matrix[0].length == 0) return false;
        int w = matrix[0].length, h = matrix.length, i = 0, j = w - 1;
        while (true) {
            if (i >= h || j < 0) return false;  // false case
            if (target == matrix[i][j]) {
                return true;
            } else if (target > matrix[i][j]) {
                i++;
            } else if (target < matrix[i][j]) {
                j--;
            }
        }
    }

    public static void main(String[] args) {
        int[][] t = {
                {1, 3, 5, 7},
                {10, 11, 16, 20},
                {23, 30, 34, 50}
        };
        Searcha2DMatrix s = new Searcha2DMatrix();
        System.out.println(s.searchMatrix(t, 3));
        System.out.println(s.searchMatrix(t, 20));
        System.out.println(s.searchMatrix(t, 40));
        System.out.println(s.searchMatrix(t, 70));
    }
}
