package Leetcode;

/**
 * Created by xin on 2/17/14.
 */
public class BestTimetoBuyandSellStockII {
    public int maxProfit(int[] prices) {
        int sum = 0;
        for(int i = 1; i < prices.length; i ++){
            if(prices[i] > prices[i-1])sum += prices[i] - prices[i-1];
        }
        return sum;
    }
    public static void main(String[] args){
        BestTimetoBuyandSellStockII s = new BestTimetoBuyandSellStockII();
        int[] prices =  {1,2};
        int res = s.maxProfit(prices);
        System.out.println(res);
    }
}
