package CrackInterview.TreesandGraphs;

import Structs.TreeFactory;
import Structs.TreeNode;

import java.util.LinkedList;
import java.util.Stack;

/**
 * Created by xin on 2/22/14.
 */
public class InOrderNextNode {
    public TreeNode next(TreeNode node) {
        if (node == null || (node.parent == null && node.right == null)) return null;
        //has right child
        if (node.right != null) {
            // return right node left * child
            node = node.right;
            while (node.left != null) {
                node = node.left;
            }
            return node;
        }
        if (node.parent.left == node) {
            //is parent's left child
            return node.parent;
        } else {
            // is parent's right child
            while (node.parent.left != node && node.parent != null) {
                node = node.parent;
            }
            // find until it's parent's left
            if (node.parent.left == node) {
                return node.parent;
            } else {
                // if none return null
                return null;
            }
        }
    }

    public static void main(String[] args) {
        int[] A = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        TreeFactory f = new TreeFactory();
        TreeNode node = f.array2bst(A);
        InOrderNextNode s = new InOrderNextNode();
        System.out.println(node.right.right.right.val);
        System.out.println(s.next(node.right.right.right).val);
        // should be 9, null
    }
}
