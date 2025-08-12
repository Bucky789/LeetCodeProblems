from typing import List


def grayCode(n: int) -> List[int]:
    res = [0]

    for i in range(n):
        newNumbers = []

        for x in reversed(res):
            newNumber = x | (1 << i)
            newNumbers.append(newNumber)

        res.extend(newNumbers)

    return res

n = 2
print(grayCode(n))