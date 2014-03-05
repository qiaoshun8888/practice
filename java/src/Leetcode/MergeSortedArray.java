package Leetcode;

/**
 * Created by xin on 2/23/14.
 */
public class MergeSortedArray {
    public void merge(int A[], int m, int B[], int n) {
        int a = 0, b = 0;
        while (a < m && b < n) {
            if (A[a] > B[b]) {
                // B is smaller, insert, i ++ , b++
                for (int j = A.length - 1; j > a; j--) {
                    A[j] = A[j - 1]; // move back 1 step
                }
                A[a] = B[b];
                b++;
                m++;
            }
            // a move
            a++;
        }
        if (b < n) {
            while (b < n) {
                A[a] = B[b];
                a++;
                b++;
            }
        }
    }

    public static void main(String[] args) {
        MergeSortedArray s = new MergeSortedArray();
        int[] A = {1, 2, 3, 0, 0, 0};
        int[] B = {1, 2, 3};
        s.merge(A, 3, B, 3);
        for (int i = 0; i < A.length; i++) {
            System.out.println(A[i]); // should be 1,1,2,2,3,3
        }
    }
}
