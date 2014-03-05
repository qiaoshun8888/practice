package Leetcode;

import Structs.TreeNode;

import java.util.ArrayList;

/**
 * Created by xin on 2/23/14.
 */
public class BinaryTreeInorderTraversal {
    public ArrayList<Integer> inorderTraversal(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        if(root != null){
            if(root.left != null){
                for(Integer i : inorderTraversal(root.left)){
                    result.add(i);
                }
            }
            result.add(root.val);
            if(root.right != null){
                for(Integer i : inorderTraversal(root.right)){
                    result.add(i);
                }
            }
        }
        return result;
    }
}
