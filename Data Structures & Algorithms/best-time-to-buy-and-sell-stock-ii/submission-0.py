class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #One pass greedy algo
        #buy if next is higher always sell if holding on that one
        #[1,4,9,5,8]

        profit_sum = 0
        #boolean to track if holding stock
        stock = prices[0]
        #loop through prices
        for i in range(1, len(prices)):
            if prices[i] > stock:
                profit_sum = profit_sum + prices[i] - stock
                stock = prices[i]
            else:
                stock = prices[i]
        return profit_sum

        