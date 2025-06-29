from typing import List


def equalPairs(grid: List[List[int]]) -> int:
    n = len(grid)
    rows = []
    for row in grid:
        rows.append(row[:])

    count = 0
    for i in range(n):
        col = []
        for j in range(n):
            col.append(grid[j][i])
        for row in rows:
            if row == col:
                count += 1
    return count


grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(equalPairs(grid))