package Leetcode;

import java.util.ArrayList;

/**
 * Created by xin on 2/23/14.
 */
public class Permutations {
    public ArrayList<ArrayList<Integer>> permuteHelper(int[] num, int end) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        // recursively
        if (end == 0) {// base case
            ArrayList<Integer> r = new ArrayList<Integer>();
            r.add(num[end]);
            result.add(r);
            return result;
        }
        ArrayList<ArrayList<Integer>> n1 = permuteHelper(num, end - 1);
        for (ArrayList<Integer> r : n1) {
            r = new ArrayList<Integer>(r); // do I need copy here?
            r.add(num[end]);
            result.add(r);
            for (int i = 0; i < r.size() - 1; i++) {
                ArrayList<Integer> tmp = new ArrayList<Integer>(r); // copy to tmp fixed copy to r
                tmp.set(i, tmp.get(i) + tmp.get(r.size() - 1));// swap r.get(i) r.get(r.size()-1)
                tmp.set(tmp.size() - 1, tmp.get(i) - tmp.get(tmp.size() - 1));
                tmp.set(i, tmp.get(i) - tmp.get(tmp.size() - 1));
                result.add(tmp);
            }
        }
        return result;
    }

    public ArrayList<ArrayList<Integer>> permute(int[] num) {
        if (num.length == 0) return null; // empty input
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        // recursively
        return permuteHelper(num, num.length - 1);
    }

    public static void main(String[] args) {
        Permutations s = new Permutations();
        int[] A = {1, 2, 3};
        for (ArrayList<Integer> r : s.permute(A)) {
            for (int i : r) {
                System.out.printf("%d, ", i);
            }
            System.out.println();
        }
    }
}
