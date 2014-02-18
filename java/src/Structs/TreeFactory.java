package Structs;

import java.util.ArrayList;
import java.util.Arrays;

/**
 * Created by xin on 2/17/14.
 */
public class TreeFactory {
    public ArrayList<TreeNode> int2node(int[] intArray) {
        if (intArray.length == 0) return null;
        ArrayList<TreeNode> al = new ArrayList<TreeNode>();
        for (int i = 0; i < intArray.length; i++) {
            al.add(new TreeNode(intArray[i]));
        }
        return al;
    }

    public TreeNode array2tree(int[] intArray) {
        if (intArray.length >= 1) {
            ArrayList<TreeNode> al = int2node(intArray);
            for (int i = intArray.length / 2; i >= 0; i--) {
                if (2 * i < intArray.length){
                    al.get(i).left = al.get(2 * i);
                    al.get(2 * i).parent = al.get(i);
                }
                if (2 * i + 1 < intArray.length){
                    al.get(i).left = al.get(2 * i + 1);
                    al.get(2 * i + 1).parent = al.get(i);
                }
            }
            return al.get(0);
        } else {
            return null;
        }
    }
    public TreeNode bstHelper(int[] intArray, int start, int end){
        if(end < start) return null;
        int mid = start + (end - start) /2 ;
        TreeNode left = bstHelper(intArray, start, mid - 1);
        TreeNode right = bstHelper(intArray, mid + 1, end);
        TreeNode root = new TreeNode(intArray[mid]);
        root.left = left;
        root.right = right;
        if(left != null) left.parent = root;
        if(right != null) right.parent = root;
        return root;
    }
    public TreeNode array2bst(int[] intArray){
        Arrays.sort(intArray);
        TreeNode root = bstHelper(intArray, 0, intArray.length - 1);
        return root;
    }

    public static void main(String[] args) {
        TreeFactory b = new TreeFactory();
        int[] intArray = {1, 2, 3, 4, 5, 6, 7};
        b.array2bst(intArray);
    }
}

