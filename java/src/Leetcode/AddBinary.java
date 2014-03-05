package Leetcode;

import java.util.Stack;

/**
 * Created by xin on 3/4/14.
 */
public class AddBinary {
    public String addBinary(String a, String b) {
        if (a.length() == 0) return b;
        if (b.length() == 0) return a;
        char[] A = a.toCharArray(), B = b.toCharArray();
        int ae = A.length - 1, be = B.length - 1, tmp = 0;
        Stack<Integer> res = new Stack<Integer>();
        while (ae >= 0 && be >= 0) {
            int atmp = A[ae--] == '1' ? 1 : 0;
            int btmp = B[be--] == '1' ? 1 : 0;
            int r = tmp ^ atmp ^ btmp;
            tmp = tmp & atmp | tmp & btmp | atmp & btmp;
            res.push(r);
        }
        while (ae >= 0) {
            int atmp = A[ae--] == '1' ? 1 : 0;
            int r = tmp ^ atmp;
            tmp = tmp & atmp;
            res.push(r);
        }
        while (be >= 0) {
            int btmp = B[be--] == '1' ? 1 : 0;
            int r = tmp ^ btmp;
            tmp = tmp & btmp;
            res.push(r);
        }
        if (tmp != 0) res.push(tmp);
        StringBuilder sb = new StringBuilder();
        while (!res.isEmpty()) sb.append(res.pop().toString());
        return sb.toString();
    }

    public static void main(String[] args) {
        String a = "11";
        String b = "1";
        AddBinary s = new AddBinary();
        String c = s.addBinary(a, b);
        System.out.println(c);
    }
}
