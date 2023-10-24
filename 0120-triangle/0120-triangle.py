class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS = len(triangle)
        dp = triangle
        dp[ROWS - 1] = triangle[ROWS - 1]
        for r in range(ROWS - 2, -1, -1): 
            for c in range(len(triangle[r])):
                dp[r][c] = dp[r][c] + min(dp[r + 1][c], dp[r + 1][c + 1])
                
        return dp[0][0]