class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = len(text1) 
        col = len(text2)
        dp = [[0 for _ in range (col + 1)] for _ in range (row + 1)]
        
        for i in range(0, row):
            for j in range(0, col):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                elif dp[i][j-1] > dp[i-1][j]:
                    dp[i][j] = dp[i][j-1]
                else:
                     dp[i][j] = dp[i-1][j]
        print(dp)
        return dp[row - 1][col - 1]
        