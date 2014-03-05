package CrackInterview.TreesandGraphs;

import Structs.TreeFactory;
import Structs.TreeNode;

import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by xin on 2/22/14.
 */
public class DepthLinkedList {
    public LinkedList<LinkedList<TreeNode>> generate(TreeNode root) {
        if (root == null) return null;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);
        LinkedList<LinkedList<TreeNode>> res = new LinkedList<LinkedList<TreeNode>>();
        LinkedList<TreeNode> currentLevel = new LinkedList<TreeNode>();
        int currentLevelLeft = 1;
        int nextLevelTotal = 0;
        while (!q.isEmpty()) {
            TreeNode node = q.poll();
            currentLevel.add(node);
            if (node.left != null) {
                q.add(node.left);
                nextLevelTotal++;
            }
            if (node.right != null) {
                q.add(node.right);
                nextLevelTotal++;
            }
            currentLevelLeft--;
            if (currentLevelLeft == 0) {
                res.add(currentLevel);
                currentLevel = new LinkedList<TreeNode>();
                currentLevelLeft = nextLevelTotal;
                nextLevelTotal = 0;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        DepthLinkedList s = new DepthLinkedList();
        TreeFactory f = new TreeFactory();
        int[] a = {1, 2, 3, 4, 5, 6, 7};
        TreeNode node = f.array2tree(a);
        LinkedList<LinkedList<TreeNode>> res = s.generate(node);
        for (int i = 0; i < res.size(); i++) {
            for (int j = 0; j < res.get(i).size(); j++) {
                System.out.printf("%d, " , res.get(i).get(j).val);
            }
            System.out.println();
        }
        // should be
        // 1,
        // 2, 3
        // 4, 5, 6, 7
    }
}
