from typing import List


def getRow(rowIndex: int) -> List[int]:
    row = [1]
    for i in range(1, rowIndex + 1):
        for j in range(len(row) - 1, 0, -1):
            row[j] = row[j] + row[j - 1]
        row.append(1)
    return row


rowIndex = 3
print(getRow(rowIndex))