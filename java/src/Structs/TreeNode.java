package Structs;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by xin on 2/17/14.
 */
public class TreeNode {
    public int val;
    public TreeNode left,right,parent;
    public TreeNode(int val){
        this.val = val;
    }
    public void bfsPrint(){
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(this);
        while(q.size() > 0){
            TreeNode node = q.poll();
            System.out.printf("%d, ", node.val);
            if(node.left != null) q.add(node.left);
            if(node.right != null) q.add(node.right);
        }
    }
    public void depthPrint(){
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(this);
        int currentLevel = 0;
        int nextLevelTotal = 0;
        int currentLevelLeft = 1;
        while(!q.isEmpty()){
            TreeNode node = q.poll();
            System.out.printf("%d, ", node.val);

            if(node.left != null) {
                q.add(node.left);
                nextLevelTotal ++;
            }
            if(node.right != null) {
                q.add(node.right);
                nextLevelTotal ++;
            }
            currentLevelLeft --;
            if(currentLevelLeft <= 0){
                System.out.println();
                currentLevel ++;
                currentLevelLeft = nextLevelTotal;
                nextLevelTotal = 0;
            }
        }
    }
}
