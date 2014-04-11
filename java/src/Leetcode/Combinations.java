package Leetcode;

import java.util.ArrayList;

/**
 * Created by xin on 3/9/14.
 */
public class Combinations {
    int k;
    ArrayList<Integer> pool;
    ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();

    public void helper(ArrayList<Integer> combine, ArrayList<ArrayList<Integer>> res) {
        int size = combine.size();
        if (size == this.k) {
            this.res.add((ArrayList<Integer>) combine.clone());
        } else {
            for (Integer i : this.pool) {
                if (size == 0 || combine.get(size - 1) < i) {
                    combine.add(i);
                    helper(combine, res);
                    combine.remove(i);
                }
            }
        }
    }

    public ArrayList<ArrayList<Integer>> combine(int n, int k) {
        this.pool = new ArrayList<Integer>();
        for (int i = 1; i <= n; i++) pool.add(i);
        this.res = new ArrayList<ArrayList<Integer>>();
        this.k = k;
        helper(new ArrayList<Integer>(), res);
        return res;
    }

    public static void main(String[] args) {
        Combinations s = new Combinations();
        for (ArrayList<Integer> i : s.combine(4, 2)) {
            for (int j : i) System.out.printf("%d, ", j);
            System.out.println();
        }
    }
}
