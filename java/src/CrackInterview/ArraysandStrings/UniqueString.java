package CrackInterview.ArraysandStrings;

import java.util.HashMap;

/**
 * Created by xin on 2/18/14.
 */
public class UniqueString {
    public boolean isUnique(String s){
        char[] sa = s.toCharArray();
        HashMap<Character, Integer> counting = new HashMap<Character, Integer>();
        for(Character i : sa ){
            if(counting.containsKey(i)){
                return false;
            }
            Integer c = 1;
            counting.put(i, c);
        }
        return true;
    }
    public static void main(String[] args){
        UniqueString s = new UniqueString();
        System.out.println(s.isUnique("tes"));
    }
}
