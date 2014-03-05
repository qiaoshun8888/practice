package Leetcode;

import Structs.TreeNode;

import java.util.ArrayList;

/**
 * Created by xin on 2/23/14.
 */
public class BinaryTreePreorderTraversal {
    public ArrayList<Integer> preorderTraversal(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        if(root != null){
            result.add(root.val);
            if(root.left != null){
                for(Integer i : preorderTraversal(root.left)){
                    result.add(i);
                }
            }
            if(root.right != null){
                for(Integer i : preorderTraversal(root.right)){
                    result.add(i);
                }
            }
        }
        return result;
    }
}
