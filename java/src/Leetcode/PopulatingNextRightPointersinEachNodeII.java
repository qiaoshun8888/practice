package Leetcode;

import Structs.TreeLinkNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by xin on 3/9/14.
 */
public class PopulatingNextRightPointersinEachNodeII {
    public void connect(TreeLinkNode root) {
        if (root == null) return;
        Queue<TreeLinkNode> q = new LinkedList<TreeLinkNode>();
        q.offer(root);
        TreeLinkNode tmp = null;
        int currentLevel = 1, nextLevel = 0;
        while (!q.isEmpty()) {
            TreeLinkNode node = q.poll();
            if (node.left != null) {
                q.offer(node.left);
                nextLevel++;
            }
            if (node.right != null) {
                q.offer(node.right);
                nextLevel++;
            }

            if (tmp != null) tmp.next = node; // connect
            tmp = node; // set tmp for next node
            if (--currentLevel == 0) {
                // next level
                currentLevel = nextLevel;
                nextLevel = 0;
                tmp = null;
            }

        }
    }

    public static void main(String[] args) {
        ArrayList<TreeLinkNode> ns = new ArrayList<TreeLinkNode>();
        for (int i = 1; i <= 7; i++) {
            TreeLinkNode n = new TreeLinkNode(i);
            ns.add(n);
            if (i / 2 > 0) {
                if (i % 2 == 0) {
                    ns.get(i / 2).left = n;
                } else {
                    ns.get(i / 2).right = n;
                }
            }
        }
        TreeLinkNode t = ns.get(0);
        PopulatingNextRightPointersinEachNodeII s = new PopulatingNextRightPointersinEachNodeII();
        s.connect(t);
    }
}
