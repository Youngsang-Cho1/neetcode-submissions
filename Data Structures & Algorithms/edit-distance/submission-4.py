class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for j in range(len(word1) + 1)] for i in range(len(word2) + 1)]
        for i in range(len(word2)+1):
            dp[i][0] = i
        for j in range(len(word1)+1):
            dp[0][j] = j
        #   i i i i i
        # j
        # j
        # j

        for i in range(1, len(word2)+1):
            for j in range(1, len(word1)+1):
                if word2[i-1] != word1[j-1]: # if the char do not match
                    diag = dp[i-1][j-1] # go to prefix (diag)
                    left = dp[i][j-1] 
                    top = dp[i-1][j] 
                    dp[i][j] = min(diag, top, left) + 1
                else:
                    dp[i][j] = dp[i-1][j-1]
        #print(dp)
        ans = dp[len(word2)][len(word1)]
        return ans