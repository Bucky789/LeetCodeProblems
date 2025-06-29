from typing import List


def longestSubarray(nums: List[int]) -> int:
    left = 0
    zeros = 0
    maxLength = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        maxLength = max(maxLength, right - left)

    return maxLength

nums = [1,1,0,1]
print(longestSubarray(nums))