package Leetcode;

import java.util.ArrayList;

/**
 * Created by xin on 3/4/14.
 */
public class GenerateParentheses {
    public void helper(int n, int l, int r, StringBuilder sb, ArrayList<String> res) {
        if (l > n || r > n) return;
        else if (l == r && l == n) res.add(new String(sb));
        else if (r > l) return;
        else if (r == l) {
            helper(n, l + 1, r, sb.append('('), res);
            sb.deleteCharAt(sb.length() - 1);
        } else { //r < l
            helper(n, l, r + 1, sb.append(')'), res);
            sb.deleteCharAt(sb.length() - 1);
            if (l < n) {
                helper(n, l + 1, r, sb.append('('), res);
                sb.deleteCharAt(sb.length() - 1);
            }
        }
    }

    public ArrayList<String> generateParenthesis(int n) {
        ArrayList<String> res = new ArrayList<String>();
        helper(n, 0, 0, new StringBuilder(), res);
        return res;
    }

    public static void main(String[] args) {
        GenerateParentheses s = new GenerateParentheses();
        for (String i : s.generateParenthesis(3)) {
            System.out.println(i);
        }
    }
}
