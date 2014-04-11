package Leetcode;

/**
 * Created by xin on 3/9/14.
 */
public class RemoveDuplicatesfromSortedArrayII {
    public int removeDuplicates(int[] A) {
        if (A.length == 0) return 0;
        int tmp = A[0], count = 0, remove = 0;
        for (int i = 1; i < A.length; i++) {
            if (remove > 0) A[i - remove] = A[i]; // move for remove
            if (A[i] == tmp) { // duplicate
                if (++count > 1) remove++; // remove for duplicate > 1
            } else count = 0; // count for duplicate
            tmp = A[i];
        }
        return A.length - remove;
    }

    public static void main(String[] args) {
        RemoveDuplicatesfromSortedArrayII s = new RemoveDuplicatesfromSortedArrayII();
        int[] A = {1, 1, 1, 2, 2, 3};
        System.out.println(s.removeDuplicates(A));
    }
}
