class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        if len(prices) < 2:
            return 0
        
        min_price = inf
        max_profit = 0
        
        for i in range(len(prices)):
            difference = prices[i] - min_price
            if prices[i] < min_price:
                min_price = prices[i]
            elif difference > max_profit:
                max_profit = difference
        
        return max_profit