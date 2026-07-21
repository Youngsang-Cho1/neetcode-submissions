class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(num):
            if num in memo:
                return memo[num]
            elif num == 0 or num == 1:
                memo[num] = 1
                return 1
            #print(memo)
            else:
                memo[num] = (dfs(num-1) + dfs(num-2))
                return memo[num]
        return dfs(n)



        
                
        