package CrackInterview.ArraysandStrings;

import java.util.ArrayList;

/**
 * Created by xin on 2/18/14.
 */
public class MatrixSetZero {
    public void set(int[][] m) {
        ArrayList<Integer> rows = new ArrayList<Integer>();
        ArrayList<Integer> cols = new ArrayList<Integer>();
        for (int i = 0; i < m.length; i++) {
            for (int j = 0; j < m[0].length; j++) {
                if(m[i][j]==0){
                    rows.add(i);
                    cols.add(j);
                }
            }
        }
        for (int i = 0; i < m.length; i++) {
            for (int j = 0; j < m[0].length; j++) {
                if(rows.contains(i) || cols.contains(j)){
                    m[i][j] = 0;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[][] m = {
                {1, 2, 0, 3, 4, 5},
                {1, 2, 3, 4, 2, 5},
                {1, 2, 1, 3, 0, 5},
                {1, 2, 1, 3, 4, 5},
                {1, 2, 1, 3, 4, 5}
        };
        MatrixSetZero s = new MatrixSetZero();
        s.set(m);
        for (int i = 0; i < m.length; i++) {
            for (int j = 0; j < m[0].length; j++) {
                System.out.printf("%d, ", m[i][j]);
            }
            System.out.println();
        }
    }
}
