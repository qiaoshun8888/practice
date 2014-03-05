package CrackInterview.TreesandGraphs;

import Structs.TreeFactory;
import Structs.TreeNode;

import java.util.HashMap;

/**
 * Created by xin on 2/23/14.
 */
public class FirstCommonAncsetor {
    public int get_depth(TreeNode p) {
        TreeNode tmp = p;
        int p_depth = 0;
        while (tmp.parent != null) {
            p_depth++;
            tmp = tmp.parent;
        }
        return p_depth;
    }

    public TreeNode moveUP(TreeNode p, int uplevel) {
        for (int i = 0; i < uplevel; i++) {
            p = p.parent;
        }
        return p;
    }

    public TreeNode find(TreeNode p, TreeNode q) {
        if (p == null || q == null) return null;
        // they all have parent property
        int p_depth = get_depth(p);
        int q_depth = get_depth(q);
        if (p_depth > q_depth) {
            moveUP(p, p_depth - q_depth);
        } else {
            moveUP(q, q_depth - p_depth);
        }
        while(p != q){
            p = p.parent;
            q = q.parent;
            if(p == q){
                return p;
            }
        }
        return null;
    }

    public static void main(String[] args){
        FirstCommonAncsetor s = new FirstCommonAncsetor();
        TreeFactory f = new TreeFactory();
        int[] A = {1,2,3,4,5,6,7};
        TreeNode node = f.array2tree(A);
        // should be 2,1,
        System.out.printf("%d, ", s.find(node.left.right, node.left.left).val);
        System.out.printf("%d, ", s.find(node.left.right, node.right.left).val);

    }
}
