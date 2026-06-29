class Solution:
    def integerBreak(self, n: int) -> int:
        # dp... it has to be 2 or 3... as 5 < 2 x 3 = 6
        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [0] * n
        for i in range(0, n):
            if i in (0,1,2):
                dp[i] = i + 1
            else:
                dp[i] = max(dp[i-2] * 2, dp[i-3] * 3)
        print(dp)
        return dp[-1]
        

        



        