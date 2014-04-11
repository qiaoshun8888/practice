package Leetcode;

import java.util.ArrayList;

/**
 * Created by xin on 3/9/14.
 */
public class PascalsTriangleII {

    public ArrayList<Integer> getRow(int rowIndex) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        res.add(1);
        if (rowIndex == 0) return res;
        else if (rowIndex > 1) {
            ArrayList<Integer> rec = getRow(rowIndex - 1);
            for (int i = 1; i < rec.size(); i++) {
                res.add(rec.get(i) + rec.get(i - 1));
            }
        }
        res.add(1);
        return res;
    }

    public static void main(String[] args) {
        PascalsTriangleII s = new PascalsTriangleII();
        for (int i : s.getRow(1)) System.out.println(i);
    }
}

//1
//1,1
//1,2,1
//1,3,3,1
//1,4,6,4,1
//1,5,10,10,5,1

