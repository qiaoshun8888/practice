package Leetcode;

import java.util.ArrayList;

/**
 * Created by xin on 2/24/14.
 */
public class GenerateParentheses {
    public ArrayList<String> generateParenthesis(int n) {
        ArrayList<String> result = new ArrayList<String>();
        if (n == 0) return result;
        if (n == 1) {
            result.add("()");
            return result;
        }
        // recursively
        for (String i : generateParenthesis(n - 1)) {
            for (int j = 0; j < i.length() - 1; j++) {
                for (int k = j; k < i.length(); k++) {
                    if (i.charAt(j + 1) == '(') continue;
                    if (k > 1 && i.charAt(k - 1) == ')') continue;
                    StringBuilder sb = new StringBuilder();
                    sb.append(i.substring(0, j));
                    sb.append('(');
                    sb.append(i.substring(j, k));
                    sb.append(')');
                    if (k <= i.length()) sb.append(i.substring(k, i.length()));
                    result.add(new String(sb));
                    System.out.printf("%d, %d, %s, %s\n", j, k, sb, i);
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        GenerateParentheses s = new GenerateParentheses();
        for (String i : s.generateParenthesis(3)) {
            System.out.println(i);
        }
    }
}
