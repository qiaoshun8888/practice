package Leetcode;

import Structs.TreeNode;

import java.util.Stack;

/**
 * Created by xin on 2/23/14.
 */
public class SymmetricTree {
    public boolean isSymmetric(TreeNode root) {
        // DFS right first and left first should be the same
        if (root == null) return true; // empty tree consider symmetric
        Stack<TreeNode> sl = new Stack<TreeNode>();
        Stack<TreeNode> sr = new Stack<TreeNode>();
        sl.push(root);
        sr.push(root);
        while (!sl.isEmpty() && !sr.isEmpty()) {
            TreeNode nl = sl.pop();
            TreeNode nr = sr.pop();
            if (nl.val != nr.val) return false;
            if (nl.left != null && nr.right != null) {
                sl.push(nl.left);
                sr.push(nr.right);
            } else if (nl.left != null || nr.right != null) {
                return false;
            }
            if (nr.left != null && nl.right != null) {
                sr.push(nr.left);
                sl.push(nl.right);
            } else if (nr.left != null || nl.right != null) {
                return false;
            }
        }
        return sl.isEmpty() && sr.isEmpty();
    }
}
