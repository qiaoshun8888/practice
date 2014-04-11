package Leetcode;

/**
 * Created by xin on 3/9/14.
 */
public class SearchinRotatedSortedArrayII {

    public boolean search(int[] A, int target) {
        if (A == null) return false;
        return helper(A, 0, A.length - 1, target);
    }

    private boolean helper(int[] A, int s, int e, int target) {
        if (s < e) {
            int m = s + (e - s) / 2;
            if (A[m] == target) return true;

            // Rotation point in the right
            if (A[s] < A[m]) {
                if (target > A[m])
                    return helper(A, m + 1, e, target);
                else {
                    return helper(A, s, m - 1, target) || helper(A, m + 1, e, target);
                }
            }
            // Rotation point in the left
            else if (A[s] > A[m]) {
                if (target < A[m])
                    return helper(A, s, m - 1, target);
                else {
                    return helper(A, m + 1, e, target) || helper(A, s, m - 1, target);
                }
            }
            // Rotation point in right or unknown.
            else {
                return helper(A, s, m - 1, target) || helper(A, m + 1, e, target);
            }
        }
        return A[s] == target;
    }

    public static void main(String[] args) {
        int[] A = {2, 2, 2, 0, 2, 2};
        SearchinRotatedSortedArrayII s = new SearchinRotatedSortedArrayII();
//        System.out.println(s.offset(A, 0, A.length - 1));
        System.out.println(s.search(A, 0));
//        System.out.println(s.search(A, 0));
    }
}
