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
        HashMap<Integer, TreeLinkNode> m = new HashMap<Integer, TreeLinkNode>();
        Queue q = new LinkedList();
        q.add(root);
        int depth = 0; int currentLevel = 1; int nextLevel = 0;
        while(!q.isEmpty()){
            TreeLinkNode node = (TreeLinkNode)q.poll();
            if(m.containsKey(depth)){
                m.get(depth).next = node;
                m.put(depth, node);
            }else{
                m.put(depth, node);
            }
            if(node.left != null){
                q.add(node.left);
                nextLevel ++;
            }
            if(node.right != null){
                q.add(node.right);
                nextLevel ++;
            }
            currentLevel -- ;
            if(currentLevel == 0){
                currentLevel = nextLevel;
                nextLevel = 0;
                depth ++;
            }
        }
    }
    
}
