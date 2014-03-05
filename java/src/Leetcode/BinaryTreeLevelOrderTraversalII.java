package Leetcode;

import Structs.TreeFactory;
import Structs.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by xin on 2/23/14.
 */
public class BinaryTreeLevelOrderTraversalII {
    public ArrayList<ArrayList<Integer>> levelOrderBottom(TreeNode root) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if (root == null) return result;
        // BFS with level count
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);
        ArrayList<Integer> current = new ArrayList<Integer>();
        int currentLevel = 1;
        int nextLevel = 0; // counts
        while (!q.isEmpty()) {
            TreeNode node = q.poll();
            if (node.left != null) {
                q.add(node.left);
                nextLevel++;
            }
            if (node.right != null) {
                q.add(node.right);
                nextLevel++;
            }
            current.add(node.val);
            currentLevel--;
            if (currentLevel == 0) {
                // save current level start new level
                result.add(0, current);
                current = new ArrayList<Integer>();
                currentLevel = nextLevel;
                nextLevel = 0;
            }

        }
        return result;
    }

    public static void main(String[] args) {
        TreeFactory f = new TreeFactory();
        int[] A = {1, 2, 3, 4, 5, 6, 7};
        TreeNode root = f.array2tree(A);
        BinaryTreeLevelOrderTraversalII s = new BinaryTreeLevelOrderTraversalII();
        ArrayList<ArrayList<Integer>> result = s.levelOrderBottom(root);
        for(ArrayList<Integer> r: result){
            for(int i: r){
                System.out.printf("%d, ", i);
            }
            System.out.println(); // should be 4,5,6,7,\n2,3,\n1,
        }

    }
}
