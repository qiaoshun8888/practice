package Leetcode;

import java.util.ArrayList;

/**
 * Created by xin on 2/23/14.
 */
public class PascalsTriangle {
    public ArrayList<ArrayList<Integer>> generate(int numRows) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if (numRows == 0) return result; //fixed input = 0;
        ArrayList<Integer> current = new ArrayList<Integer>();
        current.add(1);
        result.add(current);
        for (int i = 1; i < numRows; i++) {
            current = new ArrayList<Integer>();
            current.add(1);
            for (int j = 0; j < result.get(i - 1).size() - 1; j++) {
                current.add(result.get(i - 1).get(j) + result.get(i - 1).get(j + 1));
            }
            current.add(1);
            result.add(current);
        }
        return result;
    }

    public static void main(String[] args) {
        /**
         *
         * [1],
         * [1,1],
         * [1,2,1],
         * [1,3,3,1],
         * [1,4,6,4,1]
         */

        PascalsTriangle s = new PascalsTriangle();
        ArrayList<ArrayList<Integer>> result = s.generate(5);
        for (int i = 0; i < result.size(); i++) {
            for (int j = 0; j < result.get(i).size(); j++) {
                System.out.printf("%d, ", result.get(i).get(j));
            }
            System.out.println();
        }
    }
}
