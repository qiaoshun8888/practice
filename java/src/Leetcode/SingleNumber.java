package Leetcode;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/**
 * Created by xin on 2/17/14.
 */
public class SingleNumber {
    public int singleNumber(int[] A){
        // using XOR
        // what if there is no single number
        // and what if there is single number 0
        // i consider it's a bug
        int j = 0;
        for (int i : A){
            j = j ^i ;
        }
        return j;
    }
    public Integer singleNumber2(int[] A){
        // using hashmap
        HashMap<Integer, Boolean> m = new HashMap<Integer, Boolean>();
        for(int i : A){
            if(m.containsKey(i)){
                m.remove(i);
            } else{
                m.put(i, true);
            }
        }
        Set<Integer> s = m.keySet();
        Integer tmp = null;
        for(Integer i : s){
            tmp = i;
        }
        return tmp;
    }
    public static void main(String[] args){
        int[] A = {1,2,2,3,1};
        SingleNumber s = new SingleNumber();
        System.out.println(s.singleNumber2(A));

    }
}
