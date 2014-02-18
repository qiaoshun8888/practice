package Leetcode;

import Structs.TreeLinkNode;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by xin on 2/17/14.
 */
public class PopulatingNextRightPointersinEachNode {
    public void connect(TreeLinkNode root) {
        if (root == null) return ;
        HashMap<Integer, TreeLinkNode> nodebyLayer = new HashMap<Integer, TreeLinkNode>();
        Queue q = new LinkedList();
        q.add(root);
        while(q.size() > 0){
            TreeLinkNode node = (TreeLinkNode)q.remove();
            if(node.left != null) q.add(node.left);
            if(node.right != null) q.add(node.right);
        }

    }
}
