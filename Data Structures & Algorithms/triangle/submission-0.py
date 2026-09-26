class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        elif len(triangle) == 1:
            return triangle[0][0]
    

        dp =[[float('inf') for i in range(len(triangle[j]))] for j in range (len(triangle))]
        # print(dp)
        
        dp = [0] * 2
        dp[0], dp[1] = triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1]
        
        for i in range(2, len(triangle)): # i = row
            curr_rows = []
            for j in range(len(triangle[i])): # j = col
                if j == 0:
                    curr_rows.append(dp[j] + triangle[i][j])
                elif j == len(triangle[i]) - 1:
                    curr_rows.append(dp[j-1] + triangle[i][j])
                else:
                    curr_rows.append(triangle[i][j] + min(dp[j-1], dp[j]))
            dp = curr_rows
        #print(dp)
        return min(dp)

        
        