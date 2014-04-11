package Leetcode;

import Structs.TreeNode;

import java.nio.file.Path;

/**
 * Created by xin on 3/9/14.
 */
public class PathSum {
//    Wrong answer: need root-to-leaf
//    public boolean hasPathSum(TreeNode root, int sum) {
//        if (root == null) return false; // null case
//        if (root.val == sum) return true; // base case
//        else {
//            return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
//        }
//    }

    public boolean hasPathSum(TreeNode root, int sum) {
        if (root == null) return false; // empty case
        if (root.left == null && root.right == null) return sum == root.val; // base case
        return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
    }

    public static void main(String[] args) {
//                 5
//                / \
//               4   8
//              /   / \
//             11  13  4
//            /  \      \
//           7    2      1
        TreeNode n5 = new TreeNode(5);
        TreeNode n4 = new TreeNode(4);
        TreeNode n8 = new TreeNode(8);
        TreeNode n11 = new TreeNode(11);
        TreeNode n13 = new TreeNode(14);
        TreeNode n4_2 = new TreeNode(4);
        TreeNode n7 = new TreeNode(7);
        TreeNode n2 = new TreeNode(2);
        TreeNode n1 = new TreeNode(1);
        n5.left = n4;
        n5.right = n8;
        n4.left = n11;
        n8.left = n13;
        n8.right = n4_2;
        n4_2.right = n1;
        n11.left = n7;
        n11.right = n2;

        PathSum s = new PathSum();
        System.out.println(s.hasPathSum(n5, 22));
    }
}
