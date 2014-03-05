package CrackInterview.TreesandGraphs;

import Structs.TreeNode;

/**
 * Created by xin on 2/22/14.
 */
public class BinarySearchTree {
    public TreeNode sorted2BSTHelper(int[] A, int start, int end) {
        if (end < start) return null;
        int mid = start + (end - start) / 2;
        TreeNode root = new TreeNode(A[mid]);
        TreeNode left = sorted2BSTHelper(A, start, mid - 1);
        TreeNode right = sorted2BSTHelper(A, mid + 1, end);
        root.left = left;
        root.right = right;
        return root;
    }

    public TreeNode sorted2BST(int[] A) {
        return sorted2BSTHelper(A, 0, A.length - 1);
    }

    public static  void main(String[] args){
        int[] A = {1,2,3,4,5,6,7,8,9};
        BinarySearchTree s = new BinarySearchTree();
        TreeNode node = s.sorted2BST(A);
        node.depthPrint();
    }
}
