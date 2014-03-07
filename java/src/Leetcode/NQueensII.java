package Leetcode;

import java.lang.reflect.Array;
import java.util.ArrayList;

/**
 * Created by xin on 3/5/14.
 */
public class NQueensII {
    public boolean isValid(int[] board, int col, int row) {
        for (int j = 0; j < col; j++) {
            if (board[j] == row) return false;
            else if (Math.abs(j - col) == Math.abs(board[j] - row)) return false;
        }
        return true;
    }

    public void helper(int[] board, int col, ArrayList<int[]> res) {
        if (col >= board.length) {
            res.add(board.clone());
        }
        for (int i = 1; i <= board.length; i++) {
            if (isValid(board, col, i)) {
                board[col] = i;
                helper(board, col + 1, res);
                board[col] = 0;
            }
        }
    }

    public int totalNQueens(int n) {
        ArrayList<int[]> res = new ArrayList<int[]>();
        helper(new int[n], 0, res);
        return res.size();
    }

    public static void main(String[] args) {
        NQueensII s = new NQueensII();
        System.out.println(s.totalNQueens(8));
    }
}
