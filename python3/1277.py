from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        n = len(matrix)    # number of rows
        m = len(matrix[0]) # number of columns
        
        dp = [[0] * m for _ in range(n)]
        
        count = 0
        
        for i in range(n):
            dp[i][0] = matrix[i][0]
            count += dp[i][0]
        
        for j in range(1, m):
            dp[0][j] = matrix[0][j]
            count += dp[0][j]
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                count += dp[i][j]
        
        return count


