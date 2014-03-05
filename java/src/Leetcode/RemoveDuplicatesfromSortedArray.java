package Leetcode;

/**
 * Created by xin on 2/23/14.
 */
public class RemoveDuplicatesfromSortedArray {
    public int removeDuplicates(int[] A) {
        if (A.length <= 1) return A.length;
        int tmp = A[0], deleteCount = 0;
        for (int i = 1; i < A.length; i++) {
            if (A[i] != tmp) {
                if (deleteCount > 0) { // move ahead deleteCount, delete
                    A[i - deleteCount] = A[i];
                }
            } else {
                deleteCount++;
            }
            tmp = A[i];
        }
        return A.length - deleteCount;
    }

    public static void main(String[] args) {
        int[] A = {1, 1, 1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6};
        RemoveDuplicatesfromSortedArray s = new RemoveDuplicatesfromSortedArray();
        int length = s.removeDuplicates(A);
        System.out.println(length); // should be 6;
        for (int i = 0; i < length; i++) System.out.printf("%d, ", A[i]); // should be 1,2,3,4,5,6
    }
}
