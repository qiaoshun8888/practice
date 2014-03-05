package Leetcode;

import java.util.ArrayList;
import java.util.HashMap;

/**
 * Created by xin on 2/23/14.
 */
public class RomantoInteger {
    private HashMap<Character, Integer> m = new HashMap<Character, Integer>();

    public RomantoInteger() {
        this.m.put('M', 1000);
        this.m.put('D', 500);
        this.m.put('C', 100);
        this.m.put('L', 50);
        this.m.put('X', 10);
        this.m.put('V', 5);
        this.m.put('I', 1);
    }

    public int romanToInt(String s) {
        int result = 0;
        char[] sArray = s.toCharArray();

        for (int i = 0; i < sArray.length; i++) {
            // reverse order
            int currentValue = this.m.get(sArray[i]);
            if (i >= sArray.length - 1) {
                // has no nextValue
                result += currentValue;
                break;
            }
            int nextValue = this.m.get(sArray[i + 1]);

            if (currentValue < nextValue) {
                // plus the nextValue - currentValue, move i
                result += nextValue - currentValue;
                i++;
            } else {
                // normal thing
                result += currentValue;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        RomantoInteger s = new RomantoInteger();
        System.out.println(s.romanToInt("MDCCCLXXXIV")); // should be 4

    }
}
