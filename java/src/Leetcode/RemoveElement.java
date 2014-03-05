package Leetcode;

/**
 * Created by xin on 2/23/14.
 */
public class RemoveElement {
    public int removeElement(int[] A, int elem) {
        // remove from the begining
        int length = A.length;
        for (int i = 0; i < length; i++) {
            if (A[i] == elem) {
                // copy [i+1:], length --, i don't mvoe
                for (int j = i; j < length - 1; j++) {
                    A[j] = A[j + 1];
                }
                length--;
                i--;
            }
        }
        return length;
    }

    public static void main(String[] args) {
        RemoveElement s = new RemoveElement();
        int[] A = {1, 2, 3, 1, 2, 3, 1, 2, 3};
        System.out.println(s.removeElement(A, 1));
        for(int i= 0; i < A .length;i++) System.out.printf("%d, ", A[i]);
        // should be 6
        // should be 2,3,2,3,2,3,(whatever)...

    }
}
