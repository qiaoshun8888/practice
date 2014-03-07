package Leetcode;

import Structs.TreeFactory;
import Structs.TreeNode;

import java.util.ArrayList;

/**
 * Created by xin on 3/6/14.
 */
public class BinaryTreePostorderTraversal {
    public ArrayList<Integer> postorderTraversal(TreeNode root) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        if (root == null) return res;
        for (int i : postorderTraversal(root.left)) res.add(i);
        for (int i : postorderTraversal(root.right)) res.add(i);
        res.add(root.val);
        return res;
    }

    public static void main(String[] args) {
        TreeFactory f = new TreeFactory();
        int[] A = {1, 2, 3, 4, 5, 6, 7};
        //   1
        // 2  3
        //4 5 6 7
        TreeNode t = f.array2tree(A);
        BinaryTreePostorderTraversal s = new BinaryTreePostorderTraversal();
        for (int i : s.postorderTraversal(t)) {
            System.out.println(i);
        }
        // should be 4526731
    }
}
