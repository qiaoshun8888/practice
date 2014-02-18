package Leetcode;

import Structs.TreeNode;

/**
 * Created by xin on 2/17/14.
 */
public class MaximumDepthofBinaryTree {
    public int maxDepth(TreeNode root){
        if(root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
