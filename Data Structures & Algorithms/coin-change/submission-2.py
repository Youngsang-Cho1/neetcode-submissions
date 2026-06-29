class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            res = 1000 * 1000
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin)) # how many coins needed to reach to that value
            memo[amount] = res
            return res
        
        minimum_coins = dfs(amount)
        return -1 if minimum_coins >= 1000 * 1000 else minimum_coins
