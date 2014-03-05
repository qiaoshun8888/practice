package Leetcode;

import Structs.TreeFactory;
import Structs.TreeNode;

import java.util.LinkedList;

/**
 * Created by xin on 2/17/14.
 */
public class SameTree {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        LinkedList<TreeNode> stack1 = new LinkedList<TreeNode>();
        LinkedList<TreeNode> stack2 = new LinkedList<TreeNode>();
        stack1.push(p);
        stack2.push(q);
        while (stack1.size() > 0 && stack2.size() > 0) {
            TreeNode n1 = stack1.pop();
            TreeNode n2 = stack2.pop();
            if (n1.val != n2.val) {
                return false;
            }
            if (n1.left != null && n2.left != null) {
                stack1.push(n1.left);
                stack2.push(n2.left);
            } else if (n1.left != null || n2.left != null) {
                return false;
            }
            if (n1.right != null && n2.right != null) {
                stack1.push(n1.right);
                stack2.push(n2.right);
            } else if (n1.right != null || n2.right != null) {
                return false;
            }
        }
        return stack1.size() == 0 && stack2.size() == 0;
    }

    public static void main(String[] args) {
        int[] A = {1, 2, 3, 4, 5, 6, 7};
        TreeFactory tf = new TreeFactory();
        TreeNode p = tf.array2tree(A);
        TreeNode q = tf.array2tree(A);
        SameTree s = new SameTree();
        boolean result = s.isSameTree(p, q);
        System.out.println(result);


    }
}
