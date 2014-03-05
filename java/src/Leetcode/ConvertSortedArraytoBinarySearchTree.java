package Leetcode;

import Structs.TreeNode;

/**
 * Created by xin on 2/23/14.
 */
public class ConvertSortedArraytoBinarySearchTree {
    public TreeNode Helper(int[] num, int start, int end) {
        // I've already wrote thousand times
        if (end <= start) {
            // base case
            return null ;
        }
        int mid = start + (end - start) / 2;
        TreeNode l = Helper(num, start, mid - 1);
        TreeNode r = Helper(num, mid + 1, end);
        TreeNode n = new TreeNode(num[mid]);
        n.left = l;
        n.right = r;
        return n;
    }

    public TreeNode sortedArrayToBST(int[] num) {
        if(num.length == 0) return null; // fixed bug
        return Helper(num, 0, num.length - 1);
    }
}
