package Leetcode;

import java.util.HashMap;

/**
 * Created by xin on 2/23/14.
 */
public class IntegertoRoman {
    private int[] AvailableInt = {1000, 500, 100, 50, 10, 5, 1};
    private HashMap<Integer, Character> m = new HashMap<Integer, Character>();

    public IntegertoRoman() {
        this.m.put(1000, 'M');
        this.m.put(500, 'D');
        this.m.put(100, 'C');
        this.m.put(50, 'L');
        this.m.put(10, 'X');
        this.m.put(5, 'V');
        this.m.put(1, 'I');
    }

    public String intToRoman(int num) {
        StringBuilder sb = new StringBuilder();
        for (int i : this.AvailableInt) {
            if (num / i < 4) { // normal append
                for (int j = 0; j < num / i; j++) {
                    sb.append(this.m.get(i));
                }
            } else {
                if (sb.length() > 0 && sb.charAt(sb.length() - 1) == this.m.get(i * 5)) {
                    // fixed input = 4
                    // 5 times ahead, means 9
                    sb.setCharAt(sb.length() - 1, this.m.get(i));
                    sb.append(this.m.get(i * 10));
                } else {
                    // 4
                    sb.append(this.m.get(i));
                    sb.append(this.m.get(i * 5));
                }

            }
            num = num % i;
        }
        return new String(sb);
    }

    public static void main(String[] args) {
        IntegertoRoman s = new IntegertoRoman();
        System.out.println(s.intToRoman(4));
    }

}
