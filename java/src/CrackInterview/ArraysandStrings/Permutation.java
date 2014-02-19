package CrackInterview.ArraysandStrings;

import java.util.HashMap;

/**
 * Created by xin on 2/18/14.
 */
public class Permutation {
    public boolean isPermutation(String p, String q) {
        HashMap<Character, Integer> m = new HashMap<Character, Integer>();
        for (Character c : p.toCharArray()) {
            Integer i = 1;
            if (m.containsKey(c)) {
                i += m.get(c);
            }
            m.put(c, i);
        }
        for (Character c : q.toCharArray()) {
            if (!m.containsKey(c)) {
                return false;
            } else {
                m.put(c, m.get(c) - 1);
            }
        }
        for (Integer i : m.values()) {
            if (i != 0) return false;
        }
        return true;
    }

    public static void main(String[] args){
        Permutation s = new Permutation();
        System.out.println(s.isPermutation("test", "estt"));
        System.out.println(s.isPermutation("test", "este"));
    }
}
