package Leetcode;

/**
 * Created by xin on 2/17/14.
 */
public class UniqueBinarySearchTrees {
    public int dpHelper(int n, int[] m){
        if (n == 0) return 1;
        if (n == 1) return 1;
        if (m[n - 1] != 0) return m[n - 1];
        int res = 0;
        for (int i = 0; i < n; i++) {
            res += numTrees(i) * numTrees(n - 1 - i);
        }
        m[n - 1] = res;
        return res;
    }

    public int numTrees(int n) {
        int[] m = new int[n];
        return dpHelper(n, m);
    }

    public static void main(String[] args) {
        UniqueBinarySearchTrees s = new UniqueBinarySearchTrees();
        System.out.println(s.numTrees(2));
        System.out.println(s.numTrees(3));
        System.out.println(s.numTrees(4));
    }
}
