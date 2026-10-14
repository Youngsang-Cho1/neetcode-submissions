class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0
        memo = {}
        def dfs(idx):
            if idx in memo:
                return memo[idx]
            
            if idx == len(s):
                memo[idx] = 1
                return memo[idx]
            
            level_total = 0
            if int(s[idx]) == 0:
                return 0
            elif int(s[idx]) < 10:
                level_total += dfs(idx+1)
            if 10 <= int(s[idx : idx + 2]) <= 26:
                level_total += dfs(idx+2)
            memo[idx] = level_total
            return memo[idx]
        res = dfs(0)
        return res

            


        