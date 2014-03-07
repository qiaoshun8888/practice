package Leetcode;

/**
 * Created by xin on 3/5/14.
 */
public class ContainerWithMostWater {
    public int maxArea(int[] height) {
        int l = 0, r = height.length - 1, best = 0;
        while (l < r) {
            best = Math.max(Math.min(height[l], height[r]) * (r - l), best);
            if (height[l] < height[r]) l++;
            else r--;
        }
        return best;
    }

    public static void main(String[] args) {
        ContainerWithMostWater s = new ContainerWithMostWater();
        int[] A = {1, 3, 1, 3, 1};
        System.out.println(s.maxArea(A));
    }
}
