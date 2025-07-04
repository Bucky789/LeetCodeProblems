from typing import Counter, List


def findLHS(nums: List[int]) -> int:
    count = Counter(nums)
    maxLength = 0

    for num in count:
        if num + 1 in count:
            maxLength = max(maxLength, count[num] + count[num + 1])
    
    return maxLength

nums = [1,3,2,2,5,2,3,7]
print(findLHS(nums))