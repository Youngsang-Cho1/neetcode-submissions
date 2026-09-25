from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(idx):
            if idx >= len(cost):
                return 0
            return cost[idx] + min(dp(idx + 1), dp(idx + 2))
        return min(dp(0), dp(1))
        
        