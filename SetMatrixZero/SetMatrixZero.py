from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])
    zeroRows = set()
    zeroCols = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zeroRows.add(i)
                zeroCols.add(j)

    for i in zeroRows:
        for j in range(n):
            matrix[i][j] = 0

    for j in zeroCols:
        for i in range(m):
            matrix[i][j] = 0


    print(matrix)


matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)