from typing import List


def canJump(nums: List[int]) -> bool:
    maxReach = 0
    for i, jump in enumerate(nums):
        if i > maxReach:
            return False
        maxReach = max(maxReach, i + jump)
    return True

nums = [2,3,1,1,4]
print(canJump(nums))