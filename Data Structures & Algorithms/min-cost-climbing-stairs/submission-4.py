from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [*cost]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        #print(dp)
        
        return min(dp[-2], dp[-1])