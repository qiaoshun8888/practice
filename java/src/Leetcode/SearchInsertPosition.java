package Leetcode;

/**
 * Created by xin on 2/23/14.
 */
public class SearchInsertPosition {
    public int searchInsertHelper(int[] A, int target, int start, int end) {
        if (end < start) return start;
        int mid = start + (end - start) / 2;
        if (target <= A[mid]) {
            return searchInsertHelper(A, target, start, mid - 1);
        } else {
            return searchInsertHelper(A, target, mid + 1, end);
        }
    }

    public int searchInsert(int[] A, int target) {
        return searchInsertHelper(A, target, 0, A.length - 1);
    }
}
