from typing import List


def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    
    if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
        return 0  # No path if start or end is blocked
    
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0  # Blocked cell
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
    
    return dp[m-1][n-1]

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid))