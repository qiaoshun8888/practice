class Solution:
    # @param prices, a list of integer
    # @return an integer

    def maxProfit(self, prices):
        profit = 0
        for k, i in enumerate(prices):
            if k >= 1:
                if i - prices[k - 1] > 0:
                    profit += i - prices[k - 1]
        return profit

        # '''
        # brutal
        # '''
        # best = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         if prices[j] - prices[i] > best:
        #             best = prices[j] - prices[i]
        # return best

if __name__ == '__main__':
    s = Solution()
    print s.maxProfit([1, 2])
    # 0 -1 1 -2 1
    # 1
