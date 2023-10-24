#check profit and if we found a lower prices (profit is neg) move i to that num
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 1
    
        while r <= len(prices) - 1:
            if prices[r] - prices[l] > 0:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else: 
                l = r
            r += 1
        
        return maxProfit