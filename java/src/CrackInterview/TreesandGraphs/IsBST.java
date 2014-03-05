package CrackInterview.TreesandGraphs;

import Structs.TreeNode;

import java.util.ArrayList;

/**
 * Created by xin on 2/22/14.
 */
public class IsBST {
    public ArrayList<TreeNode> inOrder(TreeNode root) {
        ArrayList<TreeNode> result = new ArrayList<TreeNode>();
        if (root.left != null) {
            for (TreeNode i : inOrder(root.left)) {
                result.add(i);
            }
        }
        result.add(root);
        if (root.right != null) {
            for (TreeNode i : inOrder(root.right)) {
                result.add(i);
            }
        }
        return result;
    }

    public boolean isValidBST(TreeNode root) {
        if (root == null || (root.left == null && root.right == null)) return true;
        Integer tmp = null;
        for (TreeNode i : inOrder(root)) {
            if (tmp != null) {
                if (i.val <= tmp) {
                    return false;
                }
            }
            tmp = i.val;
        }
        return true;
    }

    public static void main(String[] args) {
        IsBST s = new IsBST();
        BinarySearchTree bst = new BinarySearchTree();
        int[] A = {1, 2, 3, 4, 5, 6, 7};
        TreeNode root = bst.sorted2BST(A);
        System.out.println(s.isValidBST(root));

    }
}
