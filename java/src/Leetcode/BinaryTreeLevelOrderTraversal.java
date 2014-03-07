package Leetcode;

import Structs.TreeFactory;
import Structs.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by xin on 3/6/14.
 */
public class BinaryTreeLevelOrderTraversal {
    public ArrayList<ArrayList<Integer>> levelOrder(TreeNode root) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        if (root == null) return res;
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        res.add(new ArrayList<Integer>());
        int current = 1, nextLevel = 0;
        queue.offer(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node.left != null) {
                queue.offer(node.left);
                nextLevel++;
            }
            if (node.right != null) {
                queue.offer(node.right);
                nextLevel++;
            }

            res.get(res.size() - 1).add(node.val);
            current--;
            if (current == 0) {
                res.add(new ArrayList<Integer>());
                current = nextLevel;
                nextLevel = 0;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        TreeFactory f = new TreeFactory();
        int[] A = {1, 2, 3, 4, 5, 6, 7};
        TreeNode t = f.array2tree(A);
        BinaryTreeLevelOrderTraversal s = new BinaryTreeLevelOrderTraversal();
        for (ArrayList<Integer> i : s.levelOrder(t)) {
            for (int j : i) {
                System.out.printf("%d, ", j);
            }
            System.out.println();
        }
    }
}
