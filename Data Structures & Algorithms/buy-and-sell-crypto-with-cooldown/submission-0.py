class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(idx, buying):
            if idx >= len(prices):
                return 0
            if (idx, buying) in memo:
                return memo[(idx, buying)]

            cooldown = dfs(idx + 1, buying) # skip curr while maintaining the status (buy or sell)
            if buying:
                buy = dfs(idx + 1, not buying) - prices[idx] # subtracting price since buying
                memo[(idx, buying)] = max(buy, cooldown)
            else:
                sell = dfs(idx + 2, not buying) + prices[idx] # subtracting price since buying
                memo[(idx, buying)] = max(sell, cooldown)

            return memo[(idx, buying)]
        return dfs(0, True)
        