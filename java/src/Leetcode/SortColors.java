package Leetcode;

/**
 * Created by xin on 2/23/14.
 */
public class SortColors {
    public void swap(int[] A, int l, int r) {
        A[l] = A[l] + A[r];
        A[r] = A[l] - A[r];
        A[l] = A[l] - A[r];
    }

    public int swap_zero(int[] A, int lr, int z) {
        while (lr > z && A[lr] == 0 && z < A.length) {
            // fixed 0,0 input by z<A.length
            // fixed 0,1,0 by lr > z
            swap(A, lr, z);
            z++;
        }
        return z;
    }

    public void sortColors(int[] A) {
        // counting sort using HashMap.
        // one-pass algorithm. 3 pointer, 1 for left most non-0
        // 1 for left runner, 1 for right runner
        int z = 0, l = 0, r = A.length - 1;
        while (l <= r) { // fixed input 1,0,2 by l<=r
            // encounter 0 swap with z, and move z
            z = swap_zero(A, l, z);
            z = swap_zero(A, r, z);
            for (int i : A) {
                System.out.printf("%d, ", i); // 0,0,1,1,1,1,2,2,2,2
            }
            System.out.println();
            if (A[l] != 2) l++;
            if (A[r] != 1) r--;
            if (l < r && A[l] == 2 && A[r] == 1) { // fixed input 2,1 by l<r
                swap(A, l, r); // swap l2, r1
                l++;
                r--;
            }
        }
    }

    public static void main(String[] args) {
        int[] A = {0,1,0};
        SortColors s = new SortColors();
        s.sortColors(A);
        for (int i : A) {
            System.out.printf("%d, ", i); // 0,0,1,1,1,1,2,2,2,2
        }
    }
}

