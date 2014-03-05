package CrackInterview.TreesandGraphs;

import Structs.TreeFactory;
import Structs.TreeNode;

import java.util.HashMap;
import java.util.Stack;

/**
 * Created by xin on 2/22/14.
 */
public class BalancedTree {
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        HashMap<TreeNode, Integer> m = new HashMap<TreeNode, Integer>();
        Stack<TreeNode> s = new Stack<TreeNode>();
        s.push(root);
        while (s.size() > 0) {
            TreeNode node = s.pop();
            if (m.containsKey(node)) {
                if (node.left == null && node.right == null) {
                    m.put(node, 0);
                } else if (node.left == null) {
                    if (m.get(node.right) >= 1) {
                        return false;
                    }
                    m.put(node, 1 + m.get(node.right));
                } else if (node.right == null) {
                    if (m.get(node.left) >= 1) {
                        return false;
                    }
                    m.put(node, 1 + m.get(node.left));
                } else {
                    if (Math.abs(m.get(node.left) - m.get(node.right)) > 1){
                        return false;
                    }
                    m.put(node, 1 + Math.max(m.get(node.left), m.get(node.right)));
                }
            } else {
                m.put(node, -1);
                s.push(node);
                if (node.left != null) s.push(node.left);
                if (node.right != null) s.push(node.right);
            }
        }
        return true;
    }

    public static void main(String[] args) {
        TreeFactory f = new TreeFactory();
        int[] a = {1, 2, 3, 4, 5, 6, 7};
        TreeNode root = f.array2tree(a);
        BalancedTree s = new BalancedTree();
        System.out.print(s.isBalanced(root));
    }
}
