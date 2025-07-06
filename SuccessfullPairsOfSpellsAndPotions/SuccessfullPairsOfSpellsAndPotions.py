from typing import List


def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    potions.sort()
    m = len(potions)
    result = []

    def binarySearch(target):
        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if potions[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left  

    for spell in spells:
        minRequired = (success + spell - 1) // spell  
        idx = binarySearch(minRequired)
        result.append(m - idx)

    return result

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
print(successfulPairs(spells,potions,success))