class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = 1
                    if j - i > end - start:
                        start = i
                        end = j
        return s[start:end+1]




        
        