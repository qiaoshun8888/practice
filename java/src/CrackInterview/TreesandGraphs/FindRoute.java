package CrackInterview.TreesandGraphs;

import Structs.TreeNode;

import java.util.Stack;

/**
 * Created by xin on 2/22/14.
 */
public class FindRoute {
    public boolean hasRouteHelper(TreeNode from, TreeNode to) {
        if (from == null) return false;
        Stack<TreeNode> s = new Stack<TreeNode>();
        s.push(from);
        while (!s.isEmpty()) {
            TreeNode node = s.pop();
            if (node == to) return true;
            if (node.left != null) s.push(node.left);
            if (node.right != null) s.push(node.right);
        }
        return false;
    }

    public boolean hasRoute(TreeNode p, TreeNode q) {
        // use parent it's easy  2 *O(h)
        // else it's 2 * O(n)
        return hasRouteHelper(p, q) || hasRouteHelper(q, p);
    }
}
