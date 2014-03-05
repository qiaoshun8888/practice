package Leetcode;

/**
 * Created by xin on 2/23/14.
 */
public class BestTimetoBuyandSellStock {
    public int maxProfit(int[] prices) {
        if(prices.length == 0) return 0; // fixed for empty input
        for (int i = prices.length - 1; i > 0; i--) {
            prices[i] -= prices[i - 1];
        }
        prices[0] = 0;
        int best = 0;
        int current = 0;
        for (int i = 0; i < prices.length; i++) {
            current += prices[i];
            if (current > best) best = current;
            if (current < 0) current = 0;
        }
        return best;
    }

    public static void main(String[] args) {
        BestTimetoBuyandSellStock s = new BestTimetoBuyandSellStock();
        int[] A = {};
        System.out.println(s.maxProfit(A));
    }
}
