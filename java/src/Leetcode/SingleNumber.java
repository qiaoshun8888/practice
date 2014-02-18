package Leetcode;

/**
 * Created by xin on 2/17/14.
 */
public class SingleNumber {
    public int singleNumber(int[] A){
        int j = 0;
        for (int i : A){
            j = j ^i ;
        }
        return j;
    }
    public static void main(String[] args){
        int[] A = {1,2,2,3,1};
        SingleNumber s = new SingleNumber();
        System.out.println(s.singleNumber(A));

    }
}
